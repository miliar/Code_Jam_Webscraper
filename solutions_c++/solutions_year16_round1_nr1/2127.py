#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"

using namespace std ; 
char a[2000];
int n ; 
int main(int argc, char const *argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts , cs ; cin >> ts ; 
	for(cs = 1 ; cs <= ts ; ++ cs){
		string s = "";
		scanf("%s",a + 1);

		int n = strlen(a + 1);
		for(int i = 1 ; i <= n ; ++ i){
			string x = s + a[i] , y = a[i] + s ; 
			if(x > y) s = x ; else s = y ;
		}

		printf("Case #%d: %s\n",cs,s.c_str());
	}
	return 0;
}