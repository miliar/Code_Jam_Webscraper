#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#define P printf
#define PN printf("\n");
#define PR(a) printf("%d",a);
#define PRN(a) printf("%d\n",a);

using namespace std;

#define ll long long
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define Set(a,c) memset(a, c, sizeof(a))
#define INF 1000000000
#define MAXN 100005
#define S(a) scanf("%d",&a);
#define SL(a) scanf("%lld",&a);
#define SORT(a) sort(a.begin(),a.end());
#define RSORT(a) sort(a.rbegin(),a.rend());
#define print_array(a,i,n) for(i=0;i<n;i++)cout<<a[i]<<" "; cout<<"\n";
#define print_matrix(a,i,j,row,col)FOR(i,0,row-1){FOR(j,0,col-1)cout<<a[i][j];cout<<"\n";}
#define sz(a) a.size()
#define mem(a,val) memset(a,val,sizeof(a));typedef pair<int, int> PII;
#define MOD 1000000007

#define OUTPUT freopen("output1.txt", "wt", stdout);
#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define db(debug) cout<<#debug <<" "<<debug<<"\n";
typedef vector<int> VI;
typedef vector < VI > VII;
typedef pair<int,int> pi;
typedef pair< pi ,int> pii;
VII g;
VI gr[10];
VI ::iterator up,low;
set<int>sety;
map<int , int>mapp;
map<int , int>::iterator it;
set<double>s1,s2,s3,s4;
set<double>::iterator its,its2,it1,it2;
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
double C,X,F,ans;
//#define INPUT freopen("inp.txt", "rt", stdin);
//#define INPUT freopen("B-small-attempt5.in", "rt", stdin);
#define INPUT freopen("D-large.in", "rt", stdin);

double fun(set<double>& s , double tar)
{
	double max=1000000;
   for(it1=s.begin();it1!=s.end();it1++)
   {
   	 if(*it1>=tar && *it1<max)
		max=*it1;
   }
   return max;
}
double fun2(set<double>& s , double tar)
{
	double max=-1;
   for(it2=s.begin();it2!=s.end();it2++)
   {
   	 if(*it2>=tar && *it2>max)
		max=*it2;
   }
   return max;
}

int main ()
{
#ifndef ONLINE_JUDGE
INPUT;OUTPUT;
#endif

string str;
int t,i,j,k,n,m,val,row,col;
double a[10001],b[10001];
    int T;
    scanf("%d", &T);

for(int t=1; t<=T; t++)
{
	s1.clear();
	s2.clear();
	s3.clear();
	s4.clear();
printf("Case #%d: ", t);
    scanf("%d", &n);
for(i=1;i<=n;i++)
{scanf("%lf", &a[i]);s1.insert(a[i]);s3.insert(a[i]);}
for(i=1;i<=n;i++)
{scanf("%lf", &b[i]);s2.insert(b[i]);s4.insert(b[i]);}
sort(a+1,a+n+1);
sort(b+1,b+n+1);

int ans1=0;
int ans2=0;
// normal
for(its=s1.begin();its!=s1.end();its++)
{
	double ele=fun(s2,*its);
//cout<<"looking for "<<*its<<endl;
//cout<<"ele is "<<ele<<endl;
	if(ele!=1000000)
	{
		if(ele==*its)// ==
		{
			//cout<<" *its ="<<*its<<" ele ="<<ele<<endl;
			//cout<<"SFDGHJKJGGDFGHJKLK";

		}
		else
			{ans2++;
			//cout<<"!!!!!!!!!!!!!!!!!!!!!!!!!1";
			}

		its2=s2.find(ele);
		//cout<<" *its ="<<*its<<" ele ="<<ele<<endl;
		s2.erase(*its2);
		//cout<<" ele ="<<ele<<"deleting "<<*its2<<endl;
	}
	else{
     		its2=s2.begin();
			s2.erase(*its2);
			//cout<<"ok  deleting "<<*its2<<endl;
	}
}

for(its=s3.begin();its!=s3.end();its++)
{
	if(*its<=*(s4.begin()))
	{
		double ele=fun2(s4,*its);
		its2=s4.find(ele);
		//cout<<" *its ="<<*its<<" ele ="<<ele<<endl;
		s4.erase(*its2);
		//cout<<" ele ="<<ele<<"deleting "<<*its2<<endl;
	}
	else
	{
		//double ele=fun2(s4,*its);
		its2=s4.begin();
		//cout<<" *its ="<<*its<<" ele ="<<ele<<endl;
		s4.erase(*its2);
		//cout<<" ele ="<<ele<<"deleting "<<*its2<<endl;
		ans1++;
	}
}

  printf("%d %d\n",ans1,n-ans2);
}
 return 0;
}
