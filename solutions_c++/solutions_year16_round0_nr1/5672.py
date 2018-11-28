#include<bits/stdc++.h>

using namespace std;
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define M_PIl 3.141592653589793238462643383279502884L

bool num[10];

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t; cin>>t; unsigned long long n,cnt,k,mx=(unsigned long long)1e18; bool ch;
    for(int tc=1;tc<=t;tc++)
    {
        for(int i=0;i<10;i++){num[i]=0;}
        cin>>n; ch=0;
        if(n==0)
        {
            cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        cnt=0;
        for(int i=1;i<=1000000;i++)
        {
            if((n*i)>(mx/i))
            {
                cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
                break;
            }
            k=i*n;
            stringstream ss; ss<<k;
            string s = ss.str();
            for(int j=0;j<s.size();j++)
            {
                if(!num[s[j]-'0']){cnt++;}
                num[s[j]-'0']=1;
            }
            if(cnt==10)
            {
                cout<<"Case #"<<tc<<": "<<k<<endl;
                break;
            }
        }
    }
    return 0;
}
