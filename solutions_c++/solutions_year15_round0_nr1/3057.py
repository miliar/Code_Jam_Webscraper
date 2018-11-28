#include<iostream>
#include<string>
#include<cstdio>
using namespace std;


int main()
{
    freopen("a_in.in","r",stdin);
    freopen("a_out.txt","w",stdout);
    int t,cs=1,n;
    string ss;
    cin>>t;
    while(t--)
    {
        cin>>n>>ss;
        int cnt=ss[0]-'0';
        int out=0;
        for(int i=1;i<ss.size();i++)
        {
            out+=max(0,i-cnt);
            cnt+=max(0,i-cnt)+ss[i]-'0';
        }
        printf("Case #%d: %d\n",cs++,out);
    }
    return 0;
}
