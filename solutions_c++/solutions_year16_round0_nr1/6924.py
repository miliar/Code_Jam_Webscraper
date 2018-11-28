#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
#include<cstdio>
#include<math.h>
#include<cstdlib>
#include<map>
#include<utility>
#include<stack>
#include<fstream>

using namespace std;
#define ll long long int
vector <ll> v;
vector <ll> v1;
vector <ll> v2;
const int inf=100000005;

#define cincout ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define me1(a,i) memset(a,i,sizeof(a))
#define me2(a,i,n,m) memset(a,i,n*m*sizeof(a[0][0]))
#define mp make_pair
#define pb push_back
#define sortv(v) sort(v.begin(),v.end())
#define printv(n,v) for(int i=0;i<n;i++)  {cout<<v[i]<<" ";}
bool hs[10];
bool done()
	{
	for(int i=0;i<=9;i++)
		if(hs[i]==0)
			return 0;
	return 1;
	}
int main()
	{
	cincout;
	ifstream inp;
	inp.open("test.txt");
	ofstream outf;
	outf.open("output");
	int t;
	inp>>t;
	int j=0;
	while(j!=t)
		{
		ll n,mul=1,temp;
		inp>>n;
		if(n==0)
			{
			outf<<"Case #"<<j+1<<": INSOMNIA"<<endl;
			j++;
			continue;
			}
		me1(hs,0);
		while(!done())
			{	
			temp=n*mul;
				while(temp!=0)
					{
					hs[temp%10]=1;
					temp/=10;
					}
			mul++;
			}
		outf<<"Case #"<<j+1<<": "<<(mul-1)*n<<endl;
		j++;
		}
  	return 0;
  	}