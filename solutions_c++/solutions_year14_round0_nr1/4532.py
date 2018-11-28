#include<iostream>
#include<cstdio>
using namespace std;

int a[5][5], b[5][5], T, ans1, ans2, ans, tot;

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (int h=1; h<=T; h++){
		cin >> ans1;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++)
				cin >> a[i][j];
		cin >> ans2; 
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++)
				cin >> b[i][j];
		tot = 0; ans = 0;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++)
				if (a[ans1][i] == b[ans2][j]){
					ans = a[ans1][i]; tot++;
				}
		cout << "Case #" << h << ": ";
		if (tot == 0) cout <<"Volunteer cheated!\n";
		else if (tot == 1) cout << ans << endl;
		else cout << "Bad magician!\n";
	}
}
