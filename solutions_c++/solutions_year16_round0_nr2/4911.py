//
//  main.cpp
//  math
//
//  Created by Haoyang Gu on 2/2/16.
//  Copyright (c) 2016 Haoyang Gu. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>


using namespace std;

#define all(x) x.begin(),x.end()
 // sort(all(vec))
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define tr(container, it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
// tr(set,it)
    // total+=it->second;

int main(){
    int t;
    cin >> t;
    int k=1;
    while(t--){
        
        string s;
        cin >> s;
        cout << "Case #" << k++ << ": ";
        char cur=s[0];
        int cnt=0;
        for(int i=1;i<s.length();i++){
            if(s[i]!=cur){
                for(int j=i-1;j>=0;j--)
                    s[j]=s[i];
                cur=s[i];
                cnt++;
            }
        }
        if(s[0]=='-')
            cnt++;
        cout << cnt << endl;
    }
}