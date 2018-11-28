#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cstring>
#include<numeric>


using namespace std;

#define ll long long int 
#define ss1(a) scanf("%d",&a)
#define ss2(a,b) scanf("%d %d",&a,&b)
#define ss3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loope(i,a,b) for(int i=a;i<=b;i++)
#define loopd(i,a,b) for(int i=a;i>=b;i--)


#define pii pair<int,int>
typedef vector<int> vi; 
typedef vector< vi > vvi;  
#define setzero(a) fill(a,a+sizeof(a),0);
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define DEBUG if(0)

ll powr(int s,int p)
{
	if(p==0)
		return 1;	

	if(p%2==1)
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);
		q=(q*s);	
		return ( q );
	}

	else
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);	
		return (q);
	}
}

/*******************************MAIN CODE STARTS*******************************/

vector<pair<double,int> > v;
int n;
void Scan()
{
	v.clear();
	double x;
	ss1(n);
	loop(i,0,n)
	{
		cin>>x;
		v.pb(mp(x,1));		
	}
	loop(i,0,n)
	{
		cin>>x;
		v.pb(mp(x,2));		
	}
	return;
}

void Out(int z)
{
	sort(all(v));
	/*loop(i,0,sz(v))
		printf("%lf %d, ",v[i].F,v[i].S);*/
	int c=0;
	int ret1=0,ret2=0;
	loop(i,0,sz(v))
	{
		if(v[i].S==1) c++;
		else if(v[i].S==2 && c>=1) 
		{
			c--;
			ret1++;
		}
	}
	
	c=0;
	loop(i,0,sz(v))
	{
		if(v[i].S==2) c++;
		if(v[i].S==1 && c>=1) 
		{
			c--;
			ret2++;
		}
	}
	printf("Case #%d: %d %d\n",z,ret2,n-ret1);
	return;
}
int main()
{
	int t;
	ss1(t);
	loope(z,1,t)
	{
		Scan();
		Out(z);
	}
	return 0;
}
