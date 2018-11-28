#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>


using namespace std;

int main(){

    freopen("A-large.in" , "r" , stdin);
    freopen("A-large-sol.in" , "w" , stdout);
    int t;
    cin >> t;
    for(int i=0;i<t;++i){
        int s,count=0,no=0;
        string str;
        cin >> s;
        cin >> str;
        //if((int)str[0]-48==0){++count;++no;}
        for(int k=0;k<=s;++k){
            if(str[k]-48>0){
                while(count < k){
                    ++count;++no;
                }
            }
            count = count + str[k]-48;
        }
        cout<< "Case #"<<(i+1)<<": "<<no<<"\n";
    }
    return 0;
}
