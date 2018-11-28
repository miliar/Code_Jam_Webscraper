#include <bits/stdc++.h>

using namespace std;

#define forless(i, s, e) for(int i = s; i < e; ++i)
#define forto(i, s, e) for(int i = s; i <= e; ++i)

int table[][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};
short multi[10010][10010];
string str;

int calc(int i, int j){
	int neg = 1;
	if(i * j < 0)	neg = -1;
	i = abs(i);
	j = abs(j);
	int res = neg * table[i][j];
	return res;
}


int main(){
	int T;
	cin >> T;
	forless(t, 0, T){
		memset(multi, 0, sizeof(multi));
		int L, X;
		cin >> L >> X;
		stringstream ss;
		string stmp;
		cin >> stmp;
		forless(i, 0, X)
			ss << stmp;
		str = ss.str();
		forless(i, 0, str.length()){
			multi[i][i] = str[i] - 'i' + 2;
			forless(j, i + 1, str.length()){
				int m1 = multi[i][j - 1], m2 = str[j] - 'i' + 2;
				multi[i][j] = calc(m1, m2);
			}
		}
		bool flag = false;
		forless(i, 0, str.length()){
			forless(j, i + 1, str.length()){
				if(multi[0][i] == 2 && multi[i + 1][j] == 3 && multi[j + 1][str.length() - 1] == 4){
					flag = true;
					break;
				}
			}
			if(flag)	break;
		}
		printf("Case #%d: %s\n", t + 1, (flag?"YES":"NO"));

	}
	return 0;
}