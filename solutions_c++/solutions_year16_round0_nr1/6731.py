#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <fstream>
using namespace std;

int t,a[100],ans,cnt;
long long base,n,temp,k;

FILE* fp;

int main()
{
    ofstream fp("A.out");
    scanf("%d",&t);
    cnt=0;
    //fp=fopen("A.out","r");
    while(t--)
    {
        cin>>base;
        n=0;
        memset(a,0,sizeof(a));
        ans=0;
        while(ans!=10)
        {
            if (n+base==n) break;
            n+=base;
            temp=n;

            while(temp)
            {
                k=temp%10;
                temp/=10;
                if (!a[k]) {++ans;++a[k];}
            }
            //cout<<n<<"    "<<ans<<endl;
        }
        if (ans==10) fp<<"Case #"<<++cnt<<": "<<n<<endl;
            else fp<<"Case #"<<++cnt<<": INSOMNIA"<<endl;
    }
    return 0;
}
