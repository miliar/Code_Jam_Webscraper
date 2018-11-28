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

#define OUTPUT freopen("output.txt", "wt", stdout);
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
set<int>::iterator its;
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
double C,X,F,ans;
#define INPUT freopen("A-small-attempt1.in", "rt", stdin);
//#define INPUT freopen("input.txt", "rt", stdin);
int rec(int a , int b)
{
	int cnt=0;


   	 if((a==0&&b==1))
		return 10000000;
		 b/=2;
		 if(b==0) return 0;
   	 if((a==1 && b==1))
		return 1;
   	 cnt++;
   	 int p=a/b;

   	 return 1+min(rec(p,1), rec(a-b*p,b));

}


int main ()
{
#ifndef ONLINE_JUDGE
INPUT;OUTPUT;
#endif
set<int>s1,s2;
string str;
int t,i,j,k,n,m,val,row,col,a,b,arr[100000];
    int T;
    scanf("%d", &T);
for(int t=1; t<=T; t++)
{
	char ch;
	//s1.clear();
printf("Case #%d: ", t);
  scanf("%d%c%d",&a,&ch,&b);
 // scanf("%d%d",&a,&b);
if( (b!=1) && (b&(b-1))!=0) cout<<"impossible\n";
else
{

//cout<<a<<b<<endl;
cout<<rec(a,b)<<endl;

}
/*  for(i=0;i<4;i++)
	for(j=0;j<4;j++)
  scanf("%d",&mat[i][j]);
*/


  //printf("Volunteer cheated!\n");


}
 return 0;
}
