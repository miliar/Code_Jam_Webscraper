#include<bits/stdc++.h>
using namespace std;
bool track[10]={0};
int t,t0,cnt,i;
long long int n,num,n0;
int main()
{
    freopen("file.out","w",stdout);
    cin>>t;
    t0=1;
    while(t--)
    {
        cin>>n;
        n0=n;
        for(i=0;i<10;i++) track[i]=0;
        cnt=0;
        if(n)
        {
            while(1)
            {
                num=n;
                while(num!=0)
                {
                    if(!track[num%10])
                        track[num%10]=1,cnt++;
                    num=num/10;
                }
                if(cnt==10) break;
                n=n+n0;
            }
            cout<<"Case #"<<t0++<<": "<<n<<endl;
        }
        else
            cout<<"Case #"<<t0++<<": INSOMNIA"<<endl;
    }
}