#include<bits/stdc++.h>
//Definitions
#define LL long long
#define LLU unsigned long long
#define fora(var,end) for(int var=0;var<end;var++)
#define fore(var,start,end) for(int var=start;var<end;var++)
#define forit(it1,a) for(typeof(a.begin()) it1=a.begin();it1!=a.end();it1++)
#define pub push_back
#define fst first
#define snd second
#define MOD 1000000007
/*
Coded by:Anmol Pandey
Editor:Codeblocks 12.11
*/
using namespace std;
int main()
{
    //freopen("x.txt","r",stdin);
   // freopen("out2.txt","w",stdout);
   // freopen("a.txt",stdin)
int t,x=0;
cin>>t;
char str[100000];
int n;
while(t--)
{
    x++;
    cin>>n;
    cin>>str;

    LL ans=0,sum=0;
    fora(i,n+1)
    {

        if(sum<=i)
        {
            ans+=(i-sum);
            sum=(i);
        }
        sum+=str[i]-'0';

    }
    cout<<"Case #"<<x<<": "<<ans<<endl;
}

    return 0;
}

