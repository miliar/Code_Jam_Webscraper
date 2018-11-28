#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define fr(i,beg,end) for(i=beg;i<end;i++)
#define itfr(it,stl) for(it=stl.begin();it!=stl.end();it++)
#define PII pair<int,int>
#define init(x,val) memset(x,val,sizeof(x))
#define fst first
#define snd second
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n;
    cin>>t;
    int i,j,k,cnt=0;
    int test;
    fr(test,1,t+1)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        i=n;
        int check[10];
        fr(j,0,10)
            check[j]=0;
        j=1;
        while(true)
        {
            int num=i*j;
            while(num)
            {
                check[num%10]=1;
                num/=10;
            }
            fr(k,0,10)
                if(!check[k])
                    break;
            if(k==10)
                break;
            j++;
        }
        cout<<"Case #"<<test<<": "<<i*j<<endl;
    }
    return 0;
}
