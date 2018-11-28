#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>
#include<queue>
#include<iostream>
typedef long long ll;
using namespace std;
char s[105], t[105];
int main(){
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--){
        scanf("%s", s);
        memset(t, 0, sizeof(t));
        int len = strlen(s), ret = 0;
        printf("Case #%d: ", ca++);
        for( ; ; ){
            bool tag = true;
            for(int i = 0; i < len; i++)
                if(s[i] == '-') tag = false;
            if(tag) break;

            if(s[0] == '+'){//前面变成-
                ret++;
                for(int i = 0; s[i] == '+'&&i < len; i++)
                    s[i] = '-';
            }
            ret++;
            int r = len-1;
            while(s[r] == '+') r--;
            //0 - r
            for(int i = 0; i <= r; i++)
                t[i] = s[r-i] == '+'? '-' : '+';
            for(int i = r+1; i < len; i++)
                t[i] = s[i];
            for(int i = 0; i < len; i++)
                s[i] = t[i];
        }
        cout<<ret<<endl;
    }
    return 0;
}
