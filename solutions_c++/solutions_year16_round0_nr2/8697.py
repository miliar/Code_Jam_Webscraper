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

char ss[105];
int main() {

	freopen ("B-large.in","r",stdin);
	freopen ("out.txt","w",stdout);

	int T, n, change, ans;
	string s;
	char cur;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++){
		n=0;
		scanf("%c", &ss[n]);
		cur = ss[n];
		change = 0;
		while(ss[n]!='\n' && ss[n]!= EOF){
			if(cur != ss[n]){
				change++;
				cur = ss[n];
			}
			scanf("%c", &ss[++n]);
		}

		if(change > 0){
			if(cur == '+'){
				ans = change;
			}else{
				ans = change+1;
			}
		}else{
			if(cur == '+'){
				ans = 0;
			}else{
				ans = 1;
			}
		}
		
		printf("Case #%d: %d\n", t, ans);
	}



	return 0;
}