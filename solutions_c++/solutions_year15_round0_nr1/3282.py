#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long long int lli;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<long> si;
typedef multiset<long> msi;
typedef map<string,long> maps;                               

#define Clear(a) memset(a,0,sizeof a);
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())







int main()
{
	//freopen("in.in","r",stdin);
	int t;
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		int ans=0;
		
		int n;
		string s;
		cin>>n>>s;
		int counter=s[0]-48;
		for(int i=1;i<=n;i++)
		{
			
			if(counter>=i) counter=counter+s[i]-48;
			else
			{
				ans=ans+(i-counter);
				//cout<<ans<<endl;
				counter=s[i]+i-48;
			}
		}
		printf("Case #%d: %d\n",l,ans);
	}
	return 0;
}


