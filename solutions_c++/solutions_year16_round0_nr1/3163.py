#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define ll long long
#define v vector
#define pr pair<int,int>
#define sd second
#define ft first
#define pb push_back
#define mp make_pair
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    ll i,j,k,t,n,flag,x;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        if(n==0)
            cout<<"CASE #"<<k<<": INSOMNIA"<<endl;
        else
        {
            int a[10]={0};
            flag=1;
            i=1;
            while(flag)
            {
                j=n*i;
                x=j;
                while(j)
                {
                    a[j%10]=1;
                    j/=10;
                }
                for(j=0;j<10;j++)
                {
                    if(a[j]==0)
                        break;
                }
                if(j==10)
                    flag=0;
                    i++;
            }
            cout<<"CASE #"<<k<<": "<<x<<endl;
        }
    }
    return 0;
}
