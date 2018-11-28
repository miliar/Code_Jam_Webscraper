#include <iostream>
#include <cstdio>
using namespace std;

void test(int t){
	int n; cin >> n;
	bool seen[10];
	if (n == 0) {
		cout << "Case #" << t << ": INSOMNIA\n";
		return;
	}
	for (int i=0;i<10;i++) seen[i] = false;
	int cn = n;
	while (true){
		int tmp = cn;
		while (tmp != 0) {
			seen[tmp%10] = true;
			tmp /=10;
		}
		bool tobreak = true;
		for (int i=0;i<10;i++){
			if (!seen[i]) tobreak = false;
		}
		if (tobreak) break;
		cn += n;
	}
	cout << "Case #" << t << ": " << cn << "\n";;
}

int main(){
//	ifstream cin ("");
//	ofstream cout ("A.txt");
	freopen("A-large.in", "r", stdin);
	freopen("AL.txt", "w", stdout);
	int n; cin >> n;
	for (int i=0;i<n;i++) test(i+1);
}
