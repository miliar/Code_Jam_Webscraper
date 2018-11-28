#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int T; cin>>T;
    for(int x=1;x<=T;++x) {
        int n; string s;
        cin>>n>>s;
        int res=0, t=s[0]-'0';
        for(int i=1;i<s.size();++i) {
            int d=s[i]-'0';
            if(t<i and d>0) {
                int a=i-t;
                res+=a;
                t+=a;
            }
            t+=s[i]-'0';
        }
        printf("Case #%d: %d\n", x, res);
    }
}
