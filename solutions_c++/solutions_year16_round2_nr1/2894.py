//
//  main.cpp
//  a
//
//  Created by ram on 30/04/16.
//  Copyright © 2016 ram. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    string s;
    vector<char> vec;
    vec.reserve(2000);
    vector<int> ans;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        cin>>s;
        cout<<"Case #"<<i<<": ";
        for (int a = 0; a<s.length(); a++) {
            vec.push_back(s[a]);
        }
        while (vec.size() !=0) {
            while(find(vec.begin(), vec.end(), 'Z') != vec.end()) {
                vec.erase(find(vec.begin(), vec.end(), 'Z'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                vec.erase(find(vec.begin(), vec.end(), 'R'));
                vec.erase(find(vec.begin(), vec.end(), 'O'));
                ans.push_back(0);
            }
            while(find(vec.begin(), vec.end(), 'W') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'W'));
                vec.erase(find(vec.begin(), vec.end(), 'T'));
                vec.erase(find(vec.begin(), vec.end(), 'O'));
                ans.push_back(2);
            }
            while(find(vec.begin(), vec.end(), 'U') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'U'));
                vec.erase(find(vec.begin(), vec.end(), 'F'));
                vec.erase(find(vec.begin(), vec.end(), 'O'));
                vec.erase(find(vec.begin(), vec.end(), 'R'));
                ans.push_back(4);
            }
            while(find(vec.begin(), vec.end(), 'V') != vec.end()){
                if (find(vec.begin(), vec.end(), 'F') != vec.end()) {
                    vec.erase(find(vec.begin(), vec.end(), 'F'));
                    vec.erase(find(vec.begin(), vec.end(), 'I'));
                    vec.erase(find(vec.begin(), vec.end(), 'V'));
                    vec.erase(find(vec.begin(), vec.end(), 'E'));
                    ans.push_back(5);
                }
                else{
                    vec.erase(find(vec.begin(), vec.end(), 'S'));
                    vec.erase(find(vec.begin(), vec.end(), 'E'));
                    vec.erase(find(vec.begin(), vec.end(), 'V'));
                    vec.erase(find(vec.begin(), vec.end(), 'E'));
                    vec.erase(find(vec.begin(), vec.end(), 'N'));
                    ans.push_back(7);
                }
            }
            while(find(vec.begin(), vec.end(), 'X') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'X'));
                vec.erase(find(vec.begin(), vec.end(), 'S'));
                vec.erase(find(vec.begin(), vec.end(), 'I'));
                ans.push_back(6);
            }
            while(find(vec.begin(), vec.end(), 'G') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'G'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                vec.erase(find(vec.begin(), vec.end(), 'I'));
                vec.erase(find(vec.begin(), vec.end(), 'H'));
                vec.erase(find(vec.begin(), vec.end(), 'T'));
                ans.push_back(8);
            }
            if (find(vec.begin(), vec.end(), 'O') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'O'));
                vec.erase(find(vec.begin(), vec.end(), 'N'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                ans.push_back(1);
            }
            else if (find(vec.begin(), vec.end(), 'T') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'T'));
                vec.erase(find(vec.begin(), vec.end(), 'H'));
                vec.erase(find(vec.begin(), vec.end(), 'R'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                ans.push_back(3);
            }
            else if (find(vec.begin(), vec.end(), 'N') != vec.end()){
                vec.erase(find(vec.begin(), vec.end(), 'N'));
                vec.erase(find(vec.begin(), vec.end(), 'I'));
                vec.erase(find(vec.begin(), vec.end(), 'N'));
                vec.erase(find(vec.begin(), vec.end(), 'E'));
                ans.push_back(9);
            }
        }
        sort(ans.begin(),ans.end());
        for (int j = 0; j<ans.size(); j++) {
            cout<<ans[j];
        }
        cout<<endl;
        ans.clear();
        s.clear();
        vec.clear();
    }
    return 0;
}
