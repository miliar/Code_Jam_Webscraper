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
string s;


int cnt = 0;
int main(){
	cin >> t;
	int tt = 0;
	while (t--){
		tt++;
		cin >> s;
		char pr = '?';
		cnt = 0;
		for (int i = 0; i < s.size(); i++){
			if (pr == s[i]){

			}
			else{
				cnt++;
				pr = s[i];
			}
		}
		if (s.back() == '+'){
			cnt--;
		}
		printf("Case #%d: ", tt);
		printf("%d\n", cnt);
	}
	return 0;
}