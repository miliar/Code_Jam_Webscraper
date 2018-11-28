/*
	In the Name Of GOD
	TRIPLE NARENGIES:)
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

double v,x;
int n;
int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test=0;
	while(T--)
	{
		test++;
		cin>>n;
		scanf("%lf %lf",&v,&x);
		cout<<"Case #"<<test<<": ";
		if(n==1){
			double ri,ci;
			cin>>ri>>ci;
			if(ci!=x){
				cout<<"IMPOSSIBLE"<<endl;
			}else{
				// cout<<v/ri<<endl;
				printf("%.7lf\n", v/ri);
			}
		}else{
			double r1,c1,r2,c2;
			cin>>r1>>c1>>r2>>c2;
			if(c1<c2){
				swap(c1,c2);
				swap(r1,r2);
			}
			if(x>c1 || x<c2){
				cout<<"IMPOSSIBLE"<<endl;	
			}else{
				if(c1==c2){
					printf("%.7lf\n", v/(r1+r2));
				}else{
				double a= (v*x - v*c2)/(c1-c2);
				double b = v-a;
				//cout<<max(a/r1 , b/r2)<<endl;
				// if(test==25){
				// 	sh(a);
				// 	sh(b);
				// 	sh(r1);
				// 	sh(r2);
				// }
				printf("%.7lf\n", max(a/r1 , b/r2));
			}
			}
		}
	}
}
