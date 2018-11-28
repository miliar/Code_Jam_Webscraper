/*Author : Vineet Kumar */
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
#include<fstream>
#include<string>
using namespace std;
 
#define FOR(i,a,b) 	for(int i= (int )a ; i <= (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define ps(n)		printf("%s",n)
#define psl(n)		printf("%s\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define scan_in(v,n)	vector<int> v;rep(i,n){ int j;in>>j;v.pb(j);}
#define scan_in_s(v,n)	vector<string> v;rep(i,n){ string j;in>>j;v.pb(j);}
#define mod (int)(1e9 + 7)
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
	int T;
	
	ifstream in("Fair.txt");
	ofstream out("Fair_out.txt");
	
	in>>T;
	vector<string> s;
	int r = T;
	
	while(T--)
	{
		LL A,B;
		in>>A>>B;
		LL sum=0;
		
		FOR(i,A,B)
		{
			
			char buffer[10];
			itoa(i,buffer,10);
			
			string input(buffer);
			if (input == string(input.rbegin(), input.rend()))
			{
				double num_sqrt = sqrt((double)i);
				//cout<<num_sqrt<<endl;
				char buffer1[10];
				
				if(num_sqrt==(int)num_sqrt)
				{
					itoa(num_sqrt,buffer1,10);
					string str_sqrt(buffer1);
					
					if(str_sqrt == string(str_sqrt.rbegin(), str_sqrt.rend()))sum++;
				    //cout << input << " is a palindrome"<<endl;
				}
			}
			
		}
		cout<<sum<<endl;
		
		//output init..
		char buffer[50];
		sprintf(buffer,"Case #%d: ",r-T);
		out<<buffer;
		//output
		out<<sum<<endl;
	}
	
	in.close();
	out.close();
	return 0;
}

