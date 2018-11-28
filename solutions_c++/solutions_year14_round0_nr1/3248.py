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

int m1[4][4],r1;
int m2[4][4],r2;
vector<int> v;
void Scan()
{
	v.clear();
	ss1(r1);
	r1--;
	loop(i,0,4)
		loop(j,0,4)
			ss1(m1[i][j]);
	ss1(r2);
	r2--;
	loop(i,0,4)
		loop(j,0,4)
			ss1(m2[i][j]);	
				
	return;
}

void Out(int z)
{
	loop(i,0,4)
	{
		loop(j,0,4)
		{
			if(m1[r1][i]==m2[r2][j]) v.pb(m1[r1][i]);
		}
	}	
	if(sz(v)>1) printf("Case #%d: Bad magician!\n",z);
	else if(sz(v)==0) printf("Case #%d: Volunteer cheated!\n",z);
	else printf("Case #%d: %d\n",z,v[0]);
	
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
