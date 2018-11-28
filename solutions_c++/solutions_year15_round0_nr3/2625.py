#include <iostream>
#include <cstdio>
#include <string>
#include <memory.h>

using namespace std;

int f[10005], length;
int map[5][5] = {0, 0, 0, 0, 0,
				 0, 1, 2, 3, 4,
				 0, 2, -1, 4, -3,
				 0, 3, -4, -1, 2,
				 0, 4, 3, -2, -1,
};
// 1 = 1, i = 2, j = 3, k = 4

int mul(int a, int b){
	int neg_count = 0;
	if (a < 0){
		neg_count++;
		a = -a;
	}
	if (b < 0){
		neg_count++;
		b = -b;
	}

	int	ans = map[a][b];
	if (neg_count == 1)
			return -ans;
	return ans;

}

void pre(string temp){
	f[0] = temp[0];
	for (int i = 1; i < length; ++i){
		f[i] = mul(f[i - 1], temp[i]);
	}
}

string doline(){
	for (int i = 0; i < length; ++i){
		if (f[i] == 2){
			for (int j = i + 1; j < length; ++j)
				if ((mul(f[i], -f[j]) == 3) 
					and (mul(f[j], -f[length - 1]) == 4))
					return "YES";
		}
	}
	return "NO";
}

// def doline(fuck, line):
// 	for i in range(0, len(fuck)):
// 		if fuck[i] == 'i':
// 			for j in range(i + 1, len(fuck)):
// 				if mul(fuck[i], '-' + fuck[j]) == 'j'\
// 				 and mul(fuck[j], '-' + fuck[len(fuck) - 1]) == 'k':
// 					return "YES"
// 	return "NO"




int main(){

	freopen("q3.in","r",stdin);
	freopen("q3.out","w",stdout);


	int n;
	cin >> n;
	for (int i = 0; i < n; ++i){
		int x, m;
		cin >> x >> m;
		length = x * m;
		string s;
		cin >> s;
		for (int j = 0; j < x; ++j){
			s[j] -= 'g';
		}
		string temp = "";
		for (int j = 0; j < m; ++j){
			temp += s;
		}
		for (int j = 0; j < length; ++j)
			f[j] = 0;
		pre(temp);
		cout << "Case #" << (i + 1) << ": ";
		cout << doline() << endl;
	}
}