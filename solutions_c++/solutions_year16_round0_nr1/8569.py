#include<iostream>
using namespace std;
int cnt[10];
#pragma warning(disable:4996)
bool issleep() {
	for (int i = 0;i < 10;i++) {
		if (cnt[i] == 0)return false;
	}
	return true;
}
void mark(int n) {
	while (n != 0) {
		cnt[n % 10] = 1;
		n /= 10;
	}
}
int main() {
	ios::sync_with_stdio(0);
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
	int t=1;
	cin >> t;
	for (int m = 1 ;m <=t;m++)
	{
		memset(&cnt, 0, sizeof(cnt));
		int n;
		cin >> n;
		int i = 1;
		if (n == 0) {
			cout << "Case #" << m << ": INSOMNIA\n";
			continue;
		}
		while(!issleep()){
			mark(i*n);
			i++;
		} 
		i--;
		cout<<"Case #"<<m<<": "<<i*n<<'\n';
	}
//	system("pause");
	return 0;
}