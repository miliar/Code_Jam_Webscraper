#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;
typedef long long int lint;

int main(){
	int casos;
	lint a, b, res, v[] = {1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,
	102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,
	12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,
	1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL, -1LL};
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		scanf(" %lld %lld", &a, &b);
		res = 0;
		for(int i=0;v[i]>0LL;i++) if(a <= v[i] && v[i] <= b) res++;
		printf("Case #%d: %d\n", inst, res);
	}
	return 0;
}