#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef long long LL;


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        string st;
        cin>>st;
        string ans = "";
        int len = st.length();
        for(int i=0;i<len;i++){
            string a = ans+st[i];
            string b = st[i]+ans;
            if(a<=b) ans = b;
            else ans = a;
        }
        printf("Case #%d: %s\n",cas,ans.c_str());

    }
    return 0;
}
