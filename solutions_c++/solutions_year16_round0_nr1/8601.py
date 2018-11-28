#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;
#define exp 1e-9
#define si 40
#define inf 0x3f3f3f3f
#define INF 0x00ffffff 
#define time(n) for(int i=0;i<n;i++)
#define period(s,e) for(int i=s;i<=e;i++)


template<class out_type, class in_value>
out_type convert(const in_value &t) {
	stringstream stream;
	stream << t;
	out_type result;
	stream >> result;
	return result;
}

int sign(double x) {
	return x < -exp ? -1 : x > exp;
}

bool digit[128];
char buffer[999999999];

int main() {

	freopen ("A-large.in","r",stdin);
	freopen ("out.txt","w",stdout);

	int T, len, done;
	long long base, ans;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++){
		memset(digit,false, sizeof(digit));
		done=0;
		scanf("%lld", &base);
		ans = 0;
		while(done<10){
			ans += base;
			if(ans<=0){
				break;
			}
			itoa(ans, buffer, 10);
			len = strlen(buffer);
			for(int l=0;l<len;l++){
				if(!digit[buffer[l]-'0']){
					done++;
					digit[buffer[l]-'0'] = true;
				}
			}
			
		}
		if(done>=10){
			printf("Case #%d: %d\n", t, ans);
		}else{
			printf("Case #%d: INSOMNIA\n", t);
		}
	}



	return 0;
}