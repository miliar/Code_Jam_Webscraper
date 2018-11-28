#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
const int maxn = 2e3 + 10;
const string num[] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
void get_vec(const string &s,int cur,int data,vector<int> &v)
{
    int n = s.size();
    if(cur == n) {
        v.push_back(data);
        return;
    }else {
        if(s[cur] != '?') get_vec(s, cur+1, data*10+s[cur]-'0',v);
        else {
            for(int i = 0; i < 10; ++i) get_vec(s, cur+1,data*10+i,v);
        }
    }
}
void show(int x, int n)
{
     char s[20];
     sprintf(s,"%d",x);
     x = strlen(s);
     for(;x < n; ++x) putchar('0');
     printf(s);
}
char s[maxn];
int main()
{
    vector<int> v1,v2;
    int T; cin >> T;
    int cas = 0;
    while(T--) {
        ++cas;
         string c,j;
         cin >> c >> j;
         v1.clear();
         v2.clear();
         get_vec(c,0,0,v1);
         get_vec(j,0,0,v2);
         int ans = 1e9;
         sort(v1.begin(),v1.end());
         sort(v2.begin(),v2.end());
         for(auto e1: v1) {
             for(auto e2: v2) {
                 int d = e1 - e2;
                 if(d < 0) d = -d;
                 ans = min(ans,d);
             }
         }
         bool f = false;
         for(auto e1: v1){
             if(f) break;
             for (auto e2:v2) {
                 int d = e1 - e2;
                 if (d < 0) d = -d;
                 if(d == ans) {
                    f = true;
                      printf("Case #%d: ", cas);
                      show(e1,c.size());
                      putchar(' ');
                      show(e2,c.size());
                      putchar('\n');
                      break;
                 }
             }
         }
    }
    return 0;
}
