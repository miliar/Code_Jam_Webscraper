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

string totwo(int x){
    string s;
    while(x>0){
        s+='0'+x%2;
        x/=2;
    }
    reverse(s.begin(),s.end());
    return s;
}

long long change(string s,int k){
    long long x=0;
    for(int i=0;i<s.length();i++){
        x=x*k+(s[i]-'0');
    }
    return x;
}

int main(){
    int t;
    cin >> t;
    int hhh=1;
    while(t--){
        cout << "Case #" << hhh++ << ":\n";
        int n;
        int j;
        cin >> n >> j;
        int p=(1<<(n-1))+1;
        int cnt=0;
        for(;cnt<j;p++){
            int x=p;
            string s=totwo(x);
            if(s[s.length()-1]!='1')
                continue;
            int fail=0;
            vector<long long> vec(9,1);
            for(int i=2;i<=10;i++){
                long long y=change(s,i);
               // cout << "y=" << y << endl;
                int check=0;
                for(long long k=2;k<=sqrt(y);k++){
                    if(y%k==0){
                        vec[i-2]=k;
                        check=1;
                        break;
                    }
                }
                if(check==0){
                    fail=1;
                    break;
                }
            }
            if(fail==1)
                continue;
            else{
                
                cout << s;
                for(int i=0;i<=8;i++)
                    cout << " " << vec[i];
                cout << endl;
                cnt++;
            }
                
            
        }
    }
}