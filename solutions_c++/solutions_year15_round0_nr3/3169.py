#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
using namespace std;

int multip[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };
char mul(const char &a, const char &b, int &mark){
	int a1, b1;
	switch (a){
	case '1':a1 = 0; break;
	case 'i':a1 = 1; break;
	case 'j':a1 = 2; break;
	case 'k':a1 = 3; break;
	}
	switch (b){
	case '1':b1 = 0; break;
	case 'i':b1 = 1; break;
	case 'j':b1 = 2; break;
	case 'k':b1 = 3; break;
	}
	if (multip[a1][b1] < 0)
		mark = 1;
	else
	    mark = 0;
	int res = abs(multip[a1][b1]);
	char resc;
	switch (res){
	case 1:resc = '1'; break;
	case 2:resc = 'i'; break;
	case 3:resc = 'j'; break;
	case 4:resc = 'k'; break;
	}
	return resc;
}
int main(){
	freopen("output.txt", "w", stdout);
	freopen("C-small-attempt1.in", "r", stdin);
	int n;
	int k = 0;
	cin >> n;
	while (n--){
		k++;
		int l, x;
		cin >> l >> x;
		string s;
		cin >> s;
		if (l*x < 3){
			cout << "Case #" << k << ": " << "NO" << endl;
			continue;
		}
		string res;
		for (int i = 0; i < x; i++){
			res += s;
		}
		int mark = 0;
		int sig = 0;
		char tmp = res[0];
		for (int i = 1; i<res.size(); i++){
			tmp = mul(tmp, res[i], sig);
			mark += sig;
		}
		if (tmp == '1' && mark % 2 == 1){
			int mark = 0;
			int sig = 0;
			int marki = 0;
			int i=0, j=0;
			char tmp = res[0];
			if (tmp == 'i')
				marki = 1;
			else{
				for (i = 1; i < res.size(); i++){
					tmp = mul(tmp, res[i], sig);
					mark += sig;
					if (tmp == 'i'&&mark%2==0){
						marki = 1;
						break;
					}
				}
			}
			if (marki == 0){
				cout << "Case #" << k << ": " << "NO" << endl;
				continue;
			}
			reverse(res.begin(),res.end());

			marki = 0;
			mark = 0;
			tmp = res[0];
			if (tmp == 'k')
				marki = 1;
			else{
				for (j = 1; j < res.size(); j++){
					tmp = mul( res[j],tmp, sig);
					mark += sig;
					if (tmp == 'k'&&mark % 2 == 0){
						marki = 1;
						break;
					}
				}
			}
			if (marki == 1 && i + j < res.size()-2){
				cout << "Case #" << k << ": " << "YES" << endl;
			}
			else{
				cout << "Case #" << k << ": " << "NO" << endl;
			}
		}
		else{
			cout << "Case #" << k << ": " << "NO" << endl;
		}
	}
	return 0;
}
