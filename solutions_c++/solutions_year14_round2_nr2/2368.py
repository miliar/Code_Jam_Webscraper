#include<bits/stdc++.h>
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define p(n) printf("%d\n",n)
#define mod 1000000007
#define ll long long
using namespace std;
int main()
{

    int t,k,n,i,f,j,len,p;
    int ans;
    int a,b;
    ifstream f1("input.txt");
    ofstream f2("output3.txt");
    cin>>t;
    for(k=1;k<=t;++k)
    {

        cout<<"Case #"<<k<<": ";
        ans=0;
        cin>>a>>b>>p;
        for(i=0;i<a;++i)
        {
        	for(j=0;j<b;++j)
        	{
        		int tmp;
        		tmp=i&j;
        		if(tmp<p)
        		ans++;
        	}
        }
       cout<<ans<<endl;
    }
    return 0;
}
