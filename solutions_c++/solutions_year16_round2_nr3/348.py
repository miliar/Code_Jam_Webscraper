//
// Created by user on 2016/4/30.
//

#ifndef CODEJAM_CODEJAM3_H
#define CODEJAM_CODEJAM3_H
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;


class Solution{
public:
    int count;
    int map[2000][2000],vis[2000],link[2000];
    void solute(){
        ifstream fin("A-small-attempt0.in");
        ofstream fout("out.txt");
        int T;
        fin>>T;

        vector<pair<string, string> > topic;
        set<string> set1, set2;
        string s1, s2;
        vector<string> v1, v2;
        count=1;
        unordered_map<string, int> map_1, map_2;
        for(int i=0;i<T;i++){
            int num;
            fin>>num;
            for(int j=0;j<num;j++){
                fin>>s1>>s2;
                set1.insert(s1);set2.insert(s2);
                topic.push_back(make_pair(s1,s2));
            }
            for (auto &x1: set1) {
                map_1[x] = count++;
            }
            for (auto &x2: set2) {
                map2_[x] = count++;
            }
            fout<<"Case #"<<i+1<<": "<<get(v1, v2, v)<<endl;
        }

        fin.close();
        fout.close();
    }

    int find(int x)
    {
        int i;
        for(i=1;i<count;i++)
        {
            if(map[x][i]&&!vis[i])
            {
                vis[i]=1;
                if(link[i]==0||find(link[i]))
                {
                    link[i]=x;
                    return 1;
                }
            }
        }
        return 0;
    }

};
#endif //CODEJAM_CODEJAM3_H
