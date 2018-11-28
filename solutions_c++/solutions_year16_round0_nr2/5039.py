//Tirth Maniar
#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1 && arg1){
	cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1 && arg1, Args &&... args){
	const char* comma = strchr(names+1,','); cerr.write(names,comma-names) << " : " << arg1 << " | "; __f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define all(c) c.begin(),c.end()
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end()) 
				// For Set and Map
#define cpresent(container, element) (find(all(container),element) != container.end())
				// For Vector
				// Use v.clear() to remove all elements
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
				// Better to use v.empty() instead of comparing with 0 to check if empty
#define F first
#define S second		
			// For pair
#define mod 1000000007
#define scand(x) scanf("%d",&x)
#define printd(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)

typedef long long ll;
typedef vector<int> vi;		
typedef vector< vi > vvi;    	// 2-d array
typedef pair<int,int> pii;
typedef vector<pii> vpii;

inline int mult(int x,int y){return ((ll)x*y)%mod;}
int power(int x,int y){int ret=1; while(y){ if(y&1) ret = mult(ret,x); x = mult(x,x); y = y/2;} return ret;}
int gcd(int a,int b){ if(b) return gcd(b,a%b); return a;}
vi prime;
void generateprime(int n){ int i,j; vi num(n+5); num[1]=1; for(i=4;i<n;i=i+2) num[i]=1;
	for(i=3;i<n;i++){ if(num[i]==0) { for(j=3*i;j<n;j=j+2*i) num[j] = 1;}} num[0] = 0;
	for(i=2; i<n; i++){ if(num[i]==0) prime.pb(i); num.clear();} 
}

int main()
{
	int z,t,count1,len,j=0;
	char str[200];
	scand(t);
	while(t--)
	{
		j++;
		z = 0;
		count1 = 0;
		scanf("%s",str);
		len = strlen(str);
		if(str[0] == '-')
		{
			count1 = 1;
		}
		while(str[z] == '-')
		{
			str[z] = '+';
			z++;
		}
		while(z != len)
		{
			while(str[z] == '+')
			{
				z++;
			}
			if(z != len)
			{
				count1 = count1 + 2;
				while(str[z] == '-')
				{
					str[z] = '+';
					z++;
					if(z == len)
					{
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",j,count1);
	}			
return 0;
}
