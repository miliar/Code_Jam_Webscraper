#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
using namespace std;
int T;
void solve(string& s, int& ans){
    if (s[0] == '-') ans = 1;
    int i=1;
    while(i < s.size()){
        if (s[i] != s[i-1] && s[i] == '-') ans += 2;
        i++;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    int t = 0;
    string s;
    while(t < T)
    {
        t++;
        cin >> s;
        int ans = 0;
        solve(s, ans);
        printf("Case #%d: %d\n", t, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
