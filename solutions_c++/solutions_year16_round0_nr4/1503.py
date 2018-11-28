#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
using namespace std;

int t;

int k;
int c;
int s;

int main(){
	cin >> t;
	int tt = 0;
	while (t--){
		cin >> k >> c >> s;
		tt++;
		printf("Case #%d: ", tt);
		for (int i = 1; i <= k; i++){
			if (i > 1){
				printf(" ");
			}
			printf("%d", i);
		}
		puts("");
	}
	return 0;
}