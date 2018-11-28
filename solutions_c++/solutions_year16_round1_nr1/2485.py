#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define N 100010
char s[N];
bool cmp(string a,string b)
{
    return a+b>b+a;
}
int main()
{
    int T,len,i,i1=1;
    string tmp,ans;
//    freopen("A-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        cin>>tmp;
        len=tmp.size();
        ans=tmp[0];
        for(i=1;i<len;i++)
        {
            if(cmp(ans+tmp[i],tmp[i]+ans))
                ans=ans+tmp[i];
            else
                ans=tmp[i]+ans;
        }
        printf("Case #%d: ",i1++);
        cout<<ans<<endl;
    }
    return 0;
}
