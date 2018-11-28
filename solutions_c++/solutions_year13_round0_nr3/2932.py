#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <sstream> 
#include <string>
using namespace std;
long long fairandsquare[10000000];
int fs = 0;
bool palindromes(long long n){
	static char buff[255];
	int s = 0;
	while (n){
		buff[s++]=n%10;
		n/=10;
	}
	for (int i = 0 ; i < s ; i++) 
		if (buff[i]!=buff[s-i-1]) return false;
	return true;
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	for (int i = 1;i <= 10000001 ; i++)
	{
		//if (i%10000==0) printf("%d %lld\n",i,(long long)i*i);
		if (palindromes(i) && palindromes((long long)i*i)){
			fairandsquare[fs++] = i*i;
		}
	}
//	for (int i = 0 ; i < fs; i ++)
//		printf("%d%c",fairandsquare[i],(i%10==0)?'\n':' ');
	int T = 0;
	scanf("%d",&T);
	for (int i = 1; i <= T ; i ++ ){
		long long a,b;
		scanf("%lld%lld",&a,&b);
		int posb = upper_bound(fairandsquare,fairandsquare+fs,b)-fairandsquare;
		int posa = lower_bound(fairandsquare,fairandsquare+fs,a)-fairandsquare;
		printf("Case #%d: %d\n",i,posb-posa);
		//int numb = upper_bound(fairandsquare,fairandsquare+fs,b)-fairandsquare-1;
	//	int numa = lower_bound(fairandsquare,fairandsquare+fs,a)-fairandsquare;
//		while (numa&&fairandsquare[numa]>=a)numa--;
//		printf("%d\n",numb-numa+1);
	}
};