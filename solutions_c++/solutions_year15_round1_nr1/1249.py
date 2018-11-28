#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;


bool Check(int r,vector<int> &v)
{
	int n=v.size();
	for(int i=0;i<n-1;i++)
	{
		if(v[i]-r*10 > v[i+1])
			return 0;
	}
	return 1;
}
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
		freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int tc;
    int ic=1;
    cin>>tc;
    while(tc--)
    {
    	LL a,n;
    	vector<LL> v;

    	cin>>n;
    	for(int i=0;i<n;i++){
    		cin>>a;
    		v.push_back(a);
    	}
    	LL ret1=0;
    	LL maxi=0;
    	for(int i=1;i<n;i++)
    	{
    		if(v[i]<v[i-1])
    		{
    			LL d=v[i-1]-v[i];
    			ret1+=d;
    			maxi=max(maxi,d);
    		}
    	}
    	double r=(double)maxi/10.0;
    	/*double s=0;
    	double e=10000;
    	while(s<=e)
    	{
    		double mid=(s+e)/2.0;
    		if(Check(mid,v))
    		{
    			r=mid;
    			e=mid-1;
    		}
    		else
    			s=mid+1;
    	}*/
    	LL ret2=0;
#define EPS 1e-9
    	for(int i=0;i<n-1;i++)
    	{
    		double k=r*10.0;
    		ret2+=min(maxi,v[i]);
    		//cout<<" "<<min(k,v[i]);
    	}
    	cout<<"Case #"<<ic++<<": "<<ret1<<" "<<ret2<<endl;
    }
    return 0;
    
}
