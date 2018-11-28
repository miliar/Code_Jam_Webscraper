#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <iomanip>
#define  fi(i,a,b)  for(int i=a;i<b;i++)
#define  fd(i,a,b)  for(int i=a;i>b;i--)
#define  si(n)      scanf("%d",&n);
#define  sc(n)      scanf("%c",&n);
#define  sll(n)     scanf("%lld",&n);
#define  TC         int T; si(T);

using namespace std;
int main(){
    TC
    int t = T;
    while(T--){
        string s;
        cin >> s;
        int n = s.size();
        int bottom = n-1;
        int ans = 0;
        int top = 0;
        while(true){
           top = 0;
           //cout << s << endl;
           while(bottom >= 0 && s[bottom] == '+')
              bottom--;
           int flag = 0;
           while(top < n && s[top] == '+'){
               s[top] = '-';
               flag = 1;
               top++;
           }
           while(top < n && s[top] == '-'){
               top++;
           }
           if((top - bottom) <= 1){
              if(flag)
                 ans += 2;
              else
                 ans++;
              int j = bottom;
              string t = s;
              fi(i,0,bottom+1){
                 if(s[i] == '-')
                    t[j] = '+';
                 else
                    t[j] = '-';
                 j--;
              }
              s = t;
           }
           else
             break;
        }
        cout << "Case #" << t - T << ": " << ans  << endl;
    }
    return 0;
}
