#include "iostream"
#include "bitset"
#include "cstdio"
#include "cstring"
#include "string"
#include "vector"
#include "cmath"
#include "algorithm"
using namespace std;

#define FOR(count) for(int i=0;i<(count);i++)
#define FORi(i,count) for(int i=0;i<(count);i++)
#define FOR2(from,to) for(int i=(from);i<=(to);i++)
#define FOR2i(i,from,to) for(int i=(from);i<=(to);i++)
#define long long ll

#define MAX 100

int main(){
	#ifdef codejam
		freopen("out.txt","w",stdout);
	#endif

	int T;
	int a,b,k;
	cin>>T;


	int res=0;


	FORi(t,T){
		cin>>a>>b>>k;
		
		res=0;
		FORi(i,a){
			FORi(j,b){
				if((i&j)<k) res++;
			}
		}

		printf("Case #%d: %d\n",t+1,res);
	}

	return 0;
}