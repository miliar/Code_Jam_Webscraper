//Coder- Srikant Badri :)
#include<bits/stdc++.h>
using namespace std; 
typedef pair<int,int> ii; 
typedef long long int ll;
typedef unsigned long long int ull;
typedef long int l;
typedef double d;
typedef vector<ll> vi;
typedef vector<vi> vvi; 
#define sf(a)	scanf("%lld",&a);
#define pf(a)	printf("%lld",a);
#define p(e)	printf("\n");
#define REP(i,a)	for(long long int i=0;i<a;i++)
#define REPP(i,a,b)	for(long long int i=a;i<b;i++)
#define FILL(a,x)	memset(a,x,sizeof(a))
#define debug(ccc)	cout<<#ccc<<"="<<ccc<<endl;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
const double eps=1e-8;
const int mod=1e9+7;
//const ll inf=1e18;
#define EQ(a,b)	(fabs((a)-(b))<eps)
int main() 
{
  	ll t, N;
  	freopen("C://Users//Badri//Desktop//input.txt", "r", stdin);
  	freopen("C://Users//Badri//Desktop//output.txt", "w", stdout);
	cin>>t;
  	for (int i = 1; i <= t; ++i) 
  	{
    	cin >>N;
    	ll j;
    	if(N==0)
    	cout << "Case #" << i << ": "<< "INSOMNIA"<< endl;
    	else
    	{
    		bool flag[10]={false};
    		ll K=N;
    		ll j=1;
			//while(flag[0]==false || flag[1]==false || flag[2]==false ||flag[3]==false ||flag[4]==false ||flag[5]==false ||flag[6]==false ||flag[7]==false ||flag[8]==false ||flag[9]==false )
    		while(1)
			{
    			//cout<<"Hala\n";
    			K=j*N;
    			//cout<<"K="<<K<<"\t";
    			while(K>0)
    			{
    				flag[K%10]=true;
    				K=K/10;
				}
				//i++;
				if(!(flag[0]==false || flag[1]==false || flag[2]==false ||flag[3]==false ||flag[4]==false ||flag[5]==false ||flag[6]==false ||flag[7]==false ||flag[8]==false ||flag[9]==false ))
				{
					//cout<<K<<"\t";
					cout << "Case #" << i << ": "<<j*N<< endl;
					break;
				}
				j++;
			}
			
			//cout<<K<<"\t";
			//cout << "Case #" << i << ": "<<" "<<K<< endl;
		}
 		 	
	}
	return 0;
}
