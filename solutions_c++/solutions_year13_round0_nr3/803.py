#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
using namespace std;
const double PI = 3.14159265358979323846;
typedef long long ll;

ll d[40];


int main(){
d[0] = 1;
d[1] = 4;
d[2] = 9;
d[3] = 121;
d[4] = 484;
d[5] = 10201;
d[6] = 12321;
d[7] = 14641;
d[8] = 40804;
d[9] = 44944;
d[10] = 1002001;
d[11] = 1234321;
d[12] = 4008004;
d[13] = 100020001;
d[14] = 102030201;
d[15] = 104060401;
d[16] = 121242121;
d[17] = 123454321;
d[18] = 125686521;
d[19] = 400080004;
d[20] = 404090404;
d[21] = 10000200001LL;
d[22] = 10221412201LL;
d[23] = 12102420121LL;
d[24] = 12345654321LL;
d[25] = 40000800004LL;
d[26] = 1000002000001LL;
d[27] = 1002003002001LL;
d[28] = 1004006004001LL;
d[29] = 1020304030201LL;
d[30] = 1022325232201LL;
d[31] = 1024348434201LL;
d[32] = 1210024200121LL;
d[33] = 1212225222121LL;
d[34] = 1214428244121LL;
d[35] = 1232346432321LL;
d[36] = 1234567654321LL;
d[37] = 4000008000004LL;
d[38] = 4004009004004LL;
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		ll A,B;
		cin>>A>>B;
		int a = 0,b = 38;
		while(d[a]<A)a++;
		while(d[b]>B)b--;
		printf("Case #%d: %d\n",Case,b-a+1);
	}
	return 0;
}
