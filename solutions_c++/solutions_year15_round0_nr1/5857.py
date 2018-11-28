#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("tryop.txt","w",stdout);
    int t,smax,cnt=0,peoplereq=0;
    char s[1010];
    int s1[1010];
    cin>>t;
    int m=1;
    while(m<=t)
    {
        cin>>smax;
        cin>>s;
        int i;
        cnt=0;peoplereq=0;
        for(i=0;i<=smax;i++)
            s1[i]=(int)(s[i]-48);
        for(i=0;i<=smax;i++)
        {
            //cout<<i<<"  cnt== "<<cnt<<" people==  ";

            if(cnt<i)
            {
                peoplereq+=(i-cnt);
                cnt+=(i-cnt);
            }
            cnt+=s1[i];
            //cout<<peoplereq<<endl;
        }
        cout<<"Case #"<<m<<": "<<peoplereq<<endl;
        m++;
    }
}
