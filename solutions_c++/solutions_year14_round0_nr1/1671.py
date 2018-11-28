#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-small-attempt0.in","r", stdin);
	freopen("output.out","w",stdout);
	int t;
	int x, y;
	int a[10][10];
	int b[10][10];
	int c[10];
	cin >> t;
	for (int k = 1; k <= t; k++){
		cin >> x;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++)
				cin >> a[i][j];
		}
		cin >> y;
		
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++)
				cin >> b[i][j];
		}
		int dem = 0;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (a[x][i] == b[y][j])
					c[++dem] = a[x][i];
		cout << "Case #" << k << ": ";
		if (dem == 1) cout << c[1];
		else if(dem == 0) cout << "Volunteer cheated!";
		else cout << "Bad magician!";
		cout << endl; 
		
 	}
}
