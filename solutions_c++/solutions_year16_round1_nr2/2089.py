#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"

using namespace std ; 
int n ; 
int s[3000];
int main(int argc, char const *argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts , cs ; cin >> ts ; 
	for(cs = 1 ; cs <= ts ; ++ cs){
		printf("Case #%d:",cs);
		cin >> n ;
		int x ; 
		memset(s , 0 , sizeof s); 
		for(int i = 1 ; i <= 2 * n - 1 ; ++ i)
			for(int j = 1 ; j <= n ; ++ j){
				scanf("%d",&x) ; 
				s[x] ++ ; 
			}
		for(int i = 0 ; i <= 2500 ; ++ i)
			if(s[i] & 1) printf(" %d",i);
		cout << endl ;
	}
	return 0;
}