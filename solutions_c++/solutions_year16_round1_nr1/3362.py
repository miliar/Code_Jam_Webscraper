#include<iostream> 
#include<algorithm>
#include<queue>
#include<cstring>
#include<string>
#include<stdio.h>
#include<map>
using namespace std;
typedef long long LL;
int sum,r,n,t,txt,N, cases;
#define S 1005
string s, a, b;
int main() {
    int i,j,k;
    freopen("a_large.in", "r", stdin);
    freopen("a_large.out", "w", stdout);
    scanf("%d", &n);
    for(int i = 0; i < n; ++i){
       cin >> s; 
        a = "";
        a.push_back(s[0]);
        for(int i = 1; i < s.size(); ++i){
            char c = s[i];
            string ss;
            ss.push_back(c);
            string sa = a + ss;
            string sb = ss + a;
            if(sa >= sb)a = sa;
            else a = sb;
        }
        printf("Case #%d: %s\n", ++cases, a.c_str());
    }
    return 0;
}








