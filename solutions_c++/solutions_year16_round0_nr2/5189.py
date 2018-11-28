#include<bits/stdc++.h>
#define FRU freopen("out.txt","w",stdout)
#define FRO freopen("B-large.in","r",stdin)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mem(ara,n) memset(ara,n,sizeof ara)
#define loop(i,j,n) for(i=j;i<n;i++)
#define rloop(i,j,n) for(i=n;i>=j;i--)
#define INF 2147483647
#define ll long long
#define pii pair<int,int>
#define eps 1e-9
#define mii map<int,int>
#define vi vector<int>
#define all(n) n.begin(),n.end()
#define inf INF

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int lcm(int a,int b){return ((a*b)/gcd(a,b));}

/*bool bitcheck(int n,int pos)
{
    return (bool)(n & (1<<pos));
}

int biton(int n,int pos)
{
    return n=n or (1<<pos);
}
int bitoff(int n,int pos)
{
    return n=n & ~(1<<pos);
}*/

using namespace std;

int main()
{
FRO;
FRU;
//std::ios_base::sync_with_stdio(false);
    int a,b,c,i,j,k,tc,t;
	int n,m,cnt=0;
	string s,s1;
	cin>>tc;
	for(t=1;t<=tc;t++)
	{
	    cin>>s;
	    n=s.length();
	    s.pb('.');
	    s1.clear();
	    char ch;
	    for(i=0;i<n;i++)
	    {
	        ch=s[i];
	        while(s[i]==s[i+1])i++;
	        s1.pb(ch);
	    }
	    n=s1.length();
	    cnt=0;
	    printf("Case #%d: ",t);
	    if(s1[n-1]=='+')cout<<n-1<<endl;
	    else cout<<n<<endl;
	}
return 0;
}
