#include<iostream>
using namespace std;
char s[100][100];
int re;
void print(int i, int n, int m, int b){
	//cout<<i<<' '<<n<<' '<<m<<' '<<b<<' '<<re<<endl;
	for (int j = 0; j < n; ++j)
		for (int k = 0; k < m; ++k)
			s[j][k] = '*';
	int j, k;
	int remain = n * m - b;
	for (k = 0; k < m; ++k){
		for (j = 0; j < i; ++j){
			s[j][k] = '.';
			remain --;
			//cout<<k<<' '<<j<<' '<<remain<<endl;
			if (!remain) break;
		}
		if (!remain) break;
	}
	if ((i > 2)&&(k > 0)&&(j == 0)){
		s[i - 1][k - 1] = '*';
		s[1][k] = '.';
	}
	s[0][0] = 'c';
}
bool gao(int i, int n, int m, int b){
	int remain = n * m - b;
	//cout<<i<<' '<<remain<<endl;
	if (remain == 1){
		print(i, n, m, b);
		return true;
	}
	if (i * m < remain) return false;
	if (i >= remain) return false;//不满一列->reverse然后只有一行 
	if ((i == 1)&&(n != 1)) return false; //只有1行 的特殊情况
	int k = remain % i;
	if ((i == 2)&&(k == 1)) return false; //只有2行 的特殊情况 
	if ((k == 1)&&(remain / i <= 2)) return false;
	if (remain / i <= 1) return false;
	print(i, n, m, b); 
	return true;
}
bool gao(int n, int m, int b){
	re = false;
	for (int i = 1; i <= n; ++i)
		if (gao(i, n, m, b)) return true;
	re = true;
	swap(n, m);
	for (int i = 1; i <= n; ++i)
		if (gao(i, n, m, b)) return true;
	return false;
}
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tt;
	int n, m, b;
	for (scanf("%d ", &tt), t = 0; t < tt; ++t){
		cin>>n>>m>>b;
		printf("Case #%d:\n", t + 1);
		if (gao(n, m, b)){
			for (int i = 0; i < n; ++i){
				for (int j = 0; j < m; ++j)
					if(re) cout<<s[j][i];
					else cout<<s[i][j];
				cout<<endl;
			}
		}else {
			cout<<"Impossible"<<endl;
		}
	}	
} 
