#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<climits>
#include<cmath>
#include<cstring>
using namespace std;
typedef long long ll;

#define y1 mine
#define mp make_pair

double pi = acos(-1);

string str;
int cnt;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	int t = T;
	while (T--){
		cin >> str;
		cnt = 0;

		int left;
		while (1){
			bool flag = true;

			for (int i = str.size() - 1; i >= 0; i--){
				if (str[i] == '-') {
					flag = false;

					left = i;
					if (str[0] == '+') {
						for (int j = i - 1; j >= 0; j--){
							if (str[j] == '+'){
								left = j;
								break;
							}
						}
					}

					break;
				}
			}
			if (flag) break;

			cnt++;


			for (int r = 0, l = left; r <= l; r++, l--){
				if (str[r] == '-') str[r] = '+';
				else str[r] = '-';

				if (r != l && str[l] == '-') str[l] = '+';
				else if (r != l && str[l] == '+') str[l] = '-';
				swap(str[r], str[l]);
			}
			


		}

		cout << "Case #" << t - T << ": " << cnt << endl;


	}

	
	return 0;
}


