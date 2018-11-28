//
//  main.cpp
//  TR
//
//  Created by jiusi on 4/13/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int cc;

vector<int> find(int keys[400], bool tc[cc] , vector<int> path, int nk[cc], vector<int> pk[25]) {
    if(path.size() == cc) {
        return path;
    }
    
    for(int i=0; i< cc; i++) {
        if(tc[i]) {
            if(keys[nk[i]] > 0){
                int newkeys[400];
                for(int k = 0; k<400; k++) {
                    newkeys[k] = keys[k];
                }
//                cout << "path:";
                vector<int> newpath;
                for(int k = 0; k<path.size(); k++){
                    newpath.push_back(path[k]);
//                    cout << path[k] << " ";
                }
//                cout << endl;
                bool newtc[cc];
                for(int k = 0; k<cc; k++) {
                    newtc[k] = tc[k];
//                    cout << "tc, i:" << k << " " << newtc[k] << endl;
                }
                
                newpath.push_back(i+1);
                newkeys[nk[i]]--;
                for(int k = 0; k < pk[i].size(); k++) {
                    newkeys[pk[i][k]]++;
                }
                newtc[i] = false;
                
                if(newkeys[nk[i]] == 0) {
                    bool produce = false;
                    bool consume = false;
                    for(int j = 0; j<cc; j++) if(newtc[j]){
                        if(nk[j] == nk[i]) {
                            consume = true;
                        } else if( find(pk[j].begin(), pk[j].end(), nk[i]) != pk[j].end()) {
                            produce = true;
                        }

                    }
                 
                    if(consume && !produce) {
                        continue;
                    }
                    
                }
                
                vector<int> res = find(newkeys, newtc, newpath, nk, pk);
                if(res.size() == cc) {
                    return res;
                }
            }
        }
    }
    
    return path;
}


       
int main(int argc, const char * argv[])
{
    
    ifstream cin("/Users/jiusi/Downloads/D-small-attempt1.in");
//    ifstream cin("/Users/jiusi/test.in");
    ofstream cout("/Users/jiusi/workspace-cv/TR/TR/res.out");
    int n;
    cin >> n;
    
    

    int count = 0;
    for(int c=0; c< n; c++) {
        int kc;
        
        cin >> kc >> cc;
        
//        cout << kc << " " << cc << " " << endl;;
        
        int keys[400];
        for(int i=0; i<400; i++) {
            keys[i] = 0;
        }

        for(int i = 0; i < kc; i++) {
            int key;
            cin >> key;
            keys[key-1] ++;
        }
        
        int nk[cc];
        vector<int> pk[25];
        for(int i=0; i<cc; i++) {
            int key;
            cin >> key;
            nk[i] = key-1;
            
            int kn;
            cin >> kn;
            for(int j = 0; j<kn; j++) {
                cin >> key;
                pk[i].push_back(key-1);
            }
            
        }
        
//      precheck
        bool imp = false;
        pair<int, int> com[400];
//      first: produced, sec: needed
        for(int i = 0; i < 400; i++) {
            com[i] = make_pair(0, 0);
        }
        for(int i = 0; i < cc; i++) {
            for(int j = 0; j < pk[i].size(); j++) {
//                cout << "pk ij:" << i << " " << j << " " << pk[i][j] << endl;
                com[pk[i][j]].first++;
            }
            com[nk[i]].second++;
        }
        for(int i = 0; i < 400; i++){
            if(keys[i] != 0) {
                com[i].first += keys[i];
            }
        }
        
        for(int i = 0; i < 400; i++){
//            cout << "i:" << i << " first:" << com[i].first << " sec:" << com[i].second << endl;
            
            if(com[i].first < com[i].second) {
                imp = true;
                break;
            }
        }
        
        
        if(!imp) {
            bool tc[cc];
            for(int t=0; t<cc; t++) {
                tc[t] = true;
            }
            
            vector<int> v;
            
            vector<int> path = find(keys, tc, v, nk, pk);

            cout << "Case #" << ++count << ": ";
            if(path.size() == cc) {
                for(int p = 0; p < path.size(); p++) {
                    cout << path[p] << " ";
                }
                cout << endl;
            } else {
                cout << "IMPOSSIBLE" << endl;
            }
        } else {
            cout << "Case #" << ++count << ": IMPOSSIBLE"<< endl;
        }
        
        
    }
    
    
    
}

