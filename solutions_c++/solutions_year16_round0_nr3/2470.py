#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll n=16;

ll con(ll num,ll b)
{
    ll t=1,i,ans=0;
    for(i=0;i<n;i++)
        {if(num&(1<<i))
    {
        ans+=t;
    }
    t=t*b;
        }
        return ans;
}

ll divisor(ll num)
{
    ll s=(ll)sqrt(num)+1,i;
    for(i=2;i<=s;i++)
        if(num%i==0) return i;
    return 0;
}

int main()
{
    int k=50,f,a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    ll suru=32769,i,ar[10],j,num;

  freopen("out.txt","w",stdout);

    for(i=suru;k!=0;i+=2)
    {
        f=1;
        ar[0]=divisor(i);

        if(ar[0]==0)f=0;
        for(j=1;j<9;j++)
        {
            num=con(i,j+2);
            ar[j]=divisor(num);
             if(ar[j]==0)f=0;
        }
if(f){
            cout<<num<<" ";
           for(j=0;j<9;j++)
                cout<<ar[j]<<" ";
           cout<<endl;
           k--;
}
    }
}
