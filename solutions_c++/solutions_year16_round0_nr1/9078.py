#include <string>
#include <cstring>
#include <iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
using namespace std;
typedef long long ll;
int T;

void solve(ll num, int t){
	if (num == 0){
		printf("Case #%d: INSOMNIA\n", t);
	}
	else{
		int res = 0;
		while (res != (1 << 10) - 1){
			for (int i = 1; i < 2000; i++)
			{
				ll cur = num*i;
				while (cur>0){
					int lad = cur % 10;
					res = res | (1 << lad);
					if (res == (1 << 10) - 1){
						printf("Case #%d: ",t);
						cout << num*i << endl;
						return;
					}
					cur /= 10;
				}
			}
		}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		ll num;
		cin >> num;
		solve(num, i);
	}
}