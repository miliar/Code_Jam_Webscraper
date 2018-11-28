/*************************************************************************
	> File Name: b.cpp
	> Author: 
	> Mail: 
	> Created Time: Fri 08 Apr 2016 09:09:45 PM PDT
 ************************************************************************/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    string str;
    cin>>T;
    for(int icase = 1; icase <= T; icase++){
        cin>>str;
        int time = 0;
        int s = str.size();
        while(s > 0 && str[s - 1] == '+') s--;
        char flag = '-';
        while(1){
            int t = s;
            while(t > 0 && str[t - 1] == flag) t--;
            if(t < s) time++;
            else break;
            s = t;
            flag = (flag == '-')?'+':'-';
        }
        printf("Case #%d: %d\n", icase, time);
    }
    return 0;
}
