//
//  main.cpp
//  CodeJam2015_2_CPP
//
//  Created by Nataphol Baramichai on 4/11/2558 BE.
//  Copyright (c) 2558 krabrr. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

int getMax(vector<int> arr) {
    int result = arr[0];
    int len = (int)arr.size();
    
    for (int i = 0; i < len ; i++) {
        if (arr[i] > result)
            result = arr[i];
    }
    return result;
}

int main() {
    string line;
    //ifstream input ("test_input.txt");
    //ifstream input ("C-large.in.txt");
    ifstream input ("B-small-attempt10.in.txt");
    
    ofstream output ("output.txt");
    
    if (input.is_open()) {
        
        getline(input, line);
        int num_case = stoi(line);
        int caseIdx = 1;
        
        while (getline(input, line)) {
            int n = stoi(line);
            getline(input, line);
            //cout << line << "\n";
            
            vector<string> s_arr;
            istringstream iss(line);
            copy(istream_iterator<string>(iss),
                 istream_iterator<string>(),
                 back_inserter(s_arr));
            
            vector<int> p_arr;
            for (int i = 0; i < s_arr.size(); i++) {
                p_arr.push_back(stoi(s_arr[i]));
                cout << stoi(s_arr[i]) << " ";
            }
//            for (int i = 0; i < p_arr.size(); i++)
//                cout << p_arr[i] << " ";
            
            int count = 0;
            vector<int> p_arr_clone = p_arr;
            int t_max = getMax(p_arr);
            int k_max = t_max;
            int ans = t_max;
            vector<int>::iterator it;
            
            bool contain_m3 = false;
            for (int i = 0; i < p_arr.size(); i++) {
                if (p_arr[i] > 6 && p_arr[i]%3 == 0) {
                    contain_m3 = true;
                    break;
                }
            }
            if (contain_m3) {
                while (count < k_max) {
                    it = find(p_arr.begin(), p_arr.end(), t_max);
                    int np;
                    if (t_max> 6 && t_max%3 == 0)
                        np = int(t_max/3);
                    else
                        np = int(t_max/2);
                    *it = t_max - np;
                    
                    p_arr.push_back(np);
                    count++;
                    
                    t_max = getMax(p_arr);
                    
                    if (t_max + count < ans)
                        ans = t_max + count;
                }
                
                //cout << "M3 ANS: " << ans << "\n";
                
                //reset
                count = 0;
                p_arr = p_arr_clone;
                t_max = getMax(p_arr);
            }
            
            while (count < k_max) {
                it = find(p_arr.begin(), p_arr.end(), t_max);
                int np = int(t_max/2);
                *it = t_max - np;
                
                p_arr.push_back(np);
                count++;
                
                t_max = getMax(p_arr);
                
                if (t_max + count < ans)
                    ans = t_max + count;
            }
            
            string result = to_string(ans);
            
            cout << "-> " << ans << "\n";

            result = "Case #" + to_string(caseIdx) + ": " + result;
            if (caseIdx != num_case)
                result += "\n";
            if (output.is_open())
                output << result;
            
            caseIdx++;
        }
        input.close();
        output.close();
    }
    else {
        cout << "Unable to open file";
    }
    return 0;
}
