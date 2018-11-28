#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<utility>
#include<fstream>
#include <iomanip>  
using namespace std;

#define inp(a) scanf("%d",&a)
#define out(a) printf("%d\n",a)
#define inpll(a) scanf("%lld",&a)
#define outll(a) printf("%lld\n",a)

#define swap(a,b) {a=a+b;a=a-b;b=a-b;} 
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >

#define ll long long int
#define mod 1000000007
 
#define mp make_pair 
#define X first
#define Y second
#define pb push_back
#define rep(i,a,b) for(i=a;i<b;i++)


/*inline void in(int *n)
{
    *n = 0;
    int ch = getchar_unlocked();
    while(ch < '0' || ch > '9') 
    {
        ch = getchar_unlocked();
    }
    while(ch >= '0' && ch <= '9')
        (*n) = ((*n)<<3) + ((*n)<<1) + ch - '0', ch = getchar_unlocked();
}*/
/*bool compare(const pair<ll,ll>& p,const pair<ll,ll> &q){
	return p.X<q.X;
}*/

int i,j,k,n,t,w;
double c,f,x,a,b,time1;
int main(){
	//ifstream input("o1.txt");
	//ofstream output("o4.txt"); 
	inp(t);
	//input>>t;
	w=1;
	while(w<=t){
		scanf("%lf %lf %lf",&c,&f,&x);
		//input>>c>>f>>x;
		a=2;
		time1=0;
		while(true){
			b=((c/a)+(x/(f+a)));
			if((x/a)<=b){
				time1+=x/a;
				break;
			}
			time1+=(c/a);
			a+=f;
		}
		//output<<"Case #"<<w<<": "<<setprecision (7)<<fixed<<time1<<endl;
		printf("Case #%d: %0.7lf\n",w,time1);
		w++;
	}
	return 0;
}
