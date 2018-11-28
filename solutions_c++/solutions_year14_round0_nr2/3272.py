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

double C,F,X;

void Scan()
{
	cin>>C>>F>>X;
	return;
}

void Out(int z)
{
	double ret=0,s=2,t1,t2;
	while(1)
	{
		t1=X/s;
		t2=C/s + X/(s+F);
		//printf("%lf %lf\n",t1,t2);
		//getchar();
		if(t1<=t2) 
		{
			ret+=t1;
			break;
		}	
		else 
		{
			ret+=C/s;
			s+=F;
		}	
	}
	printf("Case #%d: %.7lf\n",z,ret);
	return;
}
int main()
{
	int t;ss1(t);
	loope(z,1,t)
	{
		Scan();
		Out(z);
	}
	return 0;
}
