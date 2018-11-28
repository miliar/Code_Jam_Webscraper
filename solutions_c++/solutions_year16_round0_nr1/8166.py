#include <bits/stdc++.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	int ite,cp=1;
	cin>>ite;
	while(ite--){
		cout<<"Case #"<<cp++<<": ";
		int n;
		int tmp, some;
		//what !
		cin>>n;
		int ar[10]={0};
		int c=0,k=0;
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}

		while(c<10){
			k+=1;
			int tmp = k*n;
			while(tmp){
				if(ar[tmp%10]==0){
					ar[tmp%10]+=1;
					c++;
				}
				tmp/=10;
			}
		}

		cout<<k*n<<endl;

	}	
}
