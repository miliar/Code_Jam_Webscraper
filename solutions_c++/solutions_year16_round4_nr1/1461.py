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
#include<unordered_map>
using namespace std;

int t;

int n;
int r;
int p;
int s;

int T;

vector<int> ans;
vector<int> TMP;
deque<int> tmp;

int win[] = { 1, 2, 0 };

int main(){
	cin >> t;
	while (t--){
		T++;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: ", T);
		int len = (1 << n);
		int way = 1;
		for (int i = 0; i < len; i++){
			way *= 3;
		}
		ans.clear();
		for (int i = 0; i < way; i++){
			tmp.clear();
			TMP.clear();
			int j = i;
			int P = 0;
			int R = 0;
			int S = 0;
			int cc = 0;
			while (cc<len){
				cc++;
				if ((j % 3) == 0){
					tmp.push_back(0);
					TMP.push_back(0);
					P++;
				}
				if ((j % 3) == 1){
					tmp.push_back(1);
					TMP.push_back(1);
					R++;
				}
				if ((j % 3) == 2){
					tmp.push_back(2);
					TMP.push_back(2);
					S++;
				}
				j /= 3;
			}
			if (p == P&&r == R&&s == S){
				bool er = false;
				while (tmp.size() > 1){
					int a = tmp[0];
					int b = tmp[1];
					tmp.pop_front();
					tmp.pop_front();
					if (a == b){
						er = true;
						break;
					}
					if (win[a] == b)tmp.push_back(a);
					else tmp.push_back(b);
				}
				if (er == false){
					if (ans.size() == 0){
						ans = TMP;
					}
					else{
						ans = min(ans, TMP);
					}
				}
			}
		}
		if (ans.size() == 0){
			puts("IMPOSSIBLE");
		}
		else{
			for (int i = 0; i < ans.size(); i++){
				if (ans[i] == 0){
					printf("P");
				}
				if (ans[i] == 1){
					printf("R");
				}
				if (ans[i] == 2){
					printf("S");
				}
			}
			puts("");
		}
	}
	return 0;
}