#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
		freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t,ic=1;
    cin>>t;
    int n;
    string s;
    while(t--)
    {
    	LL ret=0;
    	cin>>n;
    	cin>>s;
    	LL tot=0;
    	for(int i=0;i<=n;i++)
    	{
    		if(tot<i)
    		{
    			LL r=i-tot;
    			tot+=r;
    			ret+=r;
    		}
    		tot+=s[i]-'0';
    	}
    	cout<<"Case #"<<ic++<<": "<<ret<<endl;
    }
    return 0;
    
}
