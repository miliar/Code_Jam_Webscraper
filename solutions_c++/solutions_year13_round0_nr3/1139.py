#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;
const ll s[39] = {1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};
int T,ans;
ll A,B;
int main () {
	//freopen("c.in","r",stdin); freopen("c.out","w",stdout);
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> A >> B; ans = 0;
		for (int j = 0; j < 39; ++j)
			if (s[j] >= A && s[j] <= B) ++ans;
		cout << "Case #" << i << ": " << ans << endl;
	}
	//fclose(stdin); fclose(stdout);
}
	
