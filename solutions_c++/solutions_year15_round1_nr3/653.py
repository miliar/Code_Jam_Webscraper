#include <bits/stdc++.h>
using namespace std;
// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9
 
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())

#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
 
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define mod 1000000007
#define F first
#define S second
#define pb push_back
#define B 27
struct PT
{
    long long int x, y,idx; 
    PT() {}
    PT(long long int x, long long int y) : x(x), y(y) {}
    PT(const PT &p) : x(p.x), y(p.y)    {}
    PT operator + (const PT &p)  const { return PT(x+p.x, y+p.y); }
    PT operator - (const PT &p)  const { return PT(x-p.x, y-p.y); }
    PT operator * (long long int c)     const { return PT(x*c,   y*c  ); }
    PT operator / (long long int c)     const { return PT(x/c,   y/c  ); }
};

double  dot(PT p, PT q)     { return p.x*q.x+p.y*q.y; }
double dist2(PT p, PT q)   { return dot(p-q,p-q); }
double cross(PT p, PT q)   { return p.x*q.y-p.y*q.x; }

PT lower_left;
bool sorter(const PT &p, const PT &q)
{
    long long int cpq = cross(p-lower_left, q-lower_left);
    if(cpq == 0)
        return dist2(p, lower_left) < dist2(q, lower_left);
    return cpq>0;
}
	int n;
vector<PT> f;
//size of A should at least be three
vector<int> hull_size(vector <PT> &A)
{
    vector <PT> hull;
 
    for (int i = 1; i < A.size(); ++i)
    {
        if(A[i].y < A[0].y || (A[i].y <= A[0].y && A[i].x < A[0].x))
        {
           swap(A[0],A[i]);
        }
    }
    lower_left = A[0];
    
   
    sort(A.begin()+1, A.end(),  sorter);
    hull.clear();
    hull.push_back(A[0]);
   
    hull.push_back(A[1]);

    int hull_sz=2;
    for (int i = 2; i < A.size(); ++i)
    {
        while(hull_sz > 1 && cross(hull[hull_sz-1]-hull[hull_sz-2], A[i]-hull[hull_sz-1]) <= 0)
        {
            hull.pop_back();
           // ans.pop_back();
            hull_sz--;
        }
        hull.push_back(A[i]);
       // ans.push_back(A[i].idx);
        hull_sz++;
    }
    vector<int>ans;
    int len=hull.size();
    for(int i=0;i<n;i++)
    {
    	for(int j=0;j<len;j++)
    	{
    		PT A1=hull[j];
    		PT B1=hull[(j+1)%len];
    		PT C1=f[i];
    	
    		double dist=cross(B1-A1,C1-B1)/sqrt(dist2(A1,B1));
    		
    		int dot1=dot(B1-A1,C1-B1);
    		if(dot1 > 0)
    		dist=sqrt(dist2(A1,B1));
    		int dot2=dot(A1-B1,C1-A1);
    		if(dot2 > 0)
    		dist=sqrt(dist2(A1,C1));
    		if(dist < EPS)
    		{
    			ans.pb(i);
    			break;
    		}
    		
    	}
    }
   
    return ans;
}
 

int x[16];
int y[16];
int mini[16];
int bit[16];
map<pair<int,int> ,int> m;
void solve(int t)
{
	m.clear();
	f.clear();
	for(int i=0;i<16;i++)
	mini[i]= INF;

	cin >> n;
	f.resize(n);
	for(int i=0;i<n;i++)
	{
		cin >> x[i] >> y[i];
		m[make_pair(x[i],y[i])]=i;
		f[i].x=x[i];
		f[i].y=y[i];
	}
	printf("Case #%d:\n",t);
	for(int i=1;i<(1<<n);i++)
	{
		fill(bit,0);
		int val=i;
		int cnt=0;
		int one=0;
		while(val > 0)
		{
			bit[cnt++]=val&1;
			if(val&1)
			one++;
			val=val/2;
		}
		if(one <= 2)
		{
			for(int j=0;j<cnt;j++)
			{
				if(bit[j] == 1)
				{
					mini[j] = min(mini[j],n-one);
				}
			}
			continue;
		}
		
		int len=one;

		vector <PT> A(len);
		int p1=0;
		for(int j=0;j<cnt;j++)
		{
			if(bit[j] == 1)
			{
				A[p1].x=x[j];
				A[p1].y= y[j];	
				//A[p1].idx=j;
				p1++;
			}
		}

		vector<int> ans=hull_size(A);
		for(int j=0;j<ans.size();j++)
		{
			int idx=ans[j];
			mini[idx]=min(mini[idx],n-len);
		}
	
	}
	for(int i=0;i<n;i++)
	{
		printf("%d\n",mini[i]);
	}
}
int main()
{
    ios_base::sync_with_stdio(0);
   	int t;
   	cin >> t;
   	for(int i=0;i<t;i++)
   	solve(i+1);
}