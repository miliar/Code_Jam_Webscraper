/* 
 * File:   main.cpp
 * Author: ckun
 *
 * Created on 2013年5月12日, 下午5:01
 */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define min(x,y) ((x)<(y)?(x):(y))
#define max(x,y) ((x)>(y)?(x):(y))

int cas;
string s;
int n;
bool al[26] = {1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0};

bool check(int x){
    //if (x>s.size()-n)
        //return false;
    for (int i=0; i<n; i++){
        if (al[s[x+i]-'a']){
            return false;
        }else{
            if (i == n-1)
                return true;
        }
    }
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    cin>>cas;
    for (int l=1; l<=cas; l++){
        cin>>s>>n;
        int count = 0;
        bool yes;
        for (int i=0; i<=s.size()-n; i++){
            for (int j=i+n-1; j<s.size(); j++){
                yes = false;
                for (int k=i; k<=j-n+1; k++){
                    if (check(k)){
                        yes = true;
                        break;
                    }
                }
                if (yes) count++;
            }
        }
        printf("Case #%d: ", l);
        cout<<count<<endl;
    }
    return 0;
}