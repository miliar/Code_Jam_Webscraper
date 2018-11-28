#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <set>
///!AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
typedef __int128_t Int;
using namespace std;
void solve()
{
    char buf[1010],b[2];
    cin>>buf;
    b[0]=buf[0];
    b[1]='\0';
    string ans=string(b);
    for(int i=1;i<strlen(buf);i++)
    {

        b[0]=buf[i];
        if(ans[0]<=buf[i])
            ans=string(b)+ans;
        else
            ans=ans+string(b);
    }
    cout<<ans;
}
int main()
{
    freopen("A-large(1).in","r",stdin);
    freopen("out.txt","w+",stdout);

    int T;
    cin>>T;

    for(int iT=0;iT<T;iT++)
    {
        cout<<"Case #"<<iT+1<<": ";
        solve();
        cout<<"\n";
    }
    return 0;
}
