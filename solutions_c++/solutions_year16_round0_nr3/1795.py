#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
FILE *fi = freopen("my.txt", "r", stdin);
FILE *fo = freopen("here.txt", "w", stdout);
#define ll long long
int test, n, JJ;
ll primeck(ll num)
{
	//prime으로 판명나면 0
	//아니면 divisor 반환
	if (num % 2 == 0)return 2;
	for (ll i = 3; i*i <= num; i += 2){
		if (num%i == 0)return i;
	}
	return 0;
}
vector<int> hol, zac;
struct info{
	vector<int> list;
	info(vector<int> l){ list = l; }
};
vector<info> v;
int main(){
	scanf("%d", &test);
	int lev = 0;
	while (test--){
		hol.clear(); zac.clear();
		++lev;
		scanf("%d%d", &n, &JJ);
		//0은 반드시 포함이라
		for (int i = 2; i < n; i += 2)zac.push_back(i);
		//mod7일 때 반드시 포함되는 앞뒤의 모듈러 값은 1, 6이고
		//각 묶음에서 1이 2개 6이 2개 더 선택되므로 이 합은 21이 되어 다시 mod7로 해도 0이된다.
		for (int i = 1; i <n - 1; i += 2)hol.push_back(i);

		for (int i = 0; i < zac.size(); i++){
			for (int ii = i + 1; ii < zac.size(); ii++){
				for (int j = 0; j < hol.size(); j++){
					for (int jj = j + 1; jj < hol.size(); jj++){
						vector<int> tmp;
						tmp.push_back(0); tmp.push_back(31);
						tmp.push_back(zac[i]); tmp.push_back(zac[ii]);
						tmp.push_back(hol[j]); tmp.push_back(hol[jj]);
						v.push_back(tmp);
					}
				}
			}
		}



		printf("Case #%d:\n", lev);
		int cnt = 0;
		for (int i = 0; i < v.size(); i++){
			string bit(32, '0');
			for (int j = 0; j < v[i].list.size(); j++)
				bit[v[i].list[j]] = '1';
			reverse(bit.begin(), bit.end());
			cout << bit;
			for (int base = 2; base <= 10; base++){
				if (base & 1)printf(" %d", 2);
				else if (base == 2 || base == 4 || base == 8 || base == 10)printf(" %d", 3);
				else if (base == 6) printf(" %d", 7);
			}
			puts("");
			++cnt;
			if (cnt == JJ)break;
		}

	}
}