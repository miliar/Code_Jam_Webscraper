//
//  First.cpp
//  codejam
//
//  Created by Adam Bielski on 08.05.2016.
//  Copyright © 2016 Adam Bielski. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solve(int K, vector<int>& senators) {
    vector<string> solutions;
    int sum = 0;
    map<int, vector<char>, std::greater<int>> counts;
    for (int i=0; i<senators.size(); ++i) {
        sum += senators[i];
        if (counts.count(senators[i]))
            counts[senators[i]].push_back('A' + i);
        else counts[senators[i]] = vector<char>{char('A'+i)};
    }
    
    int i=0;
    if (sum%2==1)
        i = 1;
    string temp_solution;
    string out_solution;
    while (!counts.empty()) {
        auto iter = counts.begin();
        char a = iter->second[0];
        iter->second.erase(std::remove(iter->second.begin(), iter->second.end(), a), iter->second.end());
        if (iter->second.size() == 0)
            counts.erase(iter->first);
        int count = iter->first-1;
        if (count > 0) {
            if (counts.count(count))
                counts[count].push_back(a);
            else counts[count] = vector<char>{a};
        }
        temp_solution += a;
        i++;
        if (i%2==0) {
            solutions.push_back(temp_solution);
            temp_solution = "";
        }
    }
    if (i%2==1)
        solutions.push_back(temp_solution);
    return solutions;
}

int main(int argc, char** argv) {
    
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        //std::string in;
        int K;
        cin >> K;
        vector<int> senators;
        for (int j=0; j<K; ++j) {
            int k;
            cin >> k;
            senators.push_back(k);
        }
        vector<string> result = solve(K, senators);
        cout << "Case #" << i+1 << ": ";
        for (int i=0; i<result.size()-1; ++i)
            cout << result[i] << " ";
        cout << *(result.end()-1) << endl;
    }
    return 0;
}