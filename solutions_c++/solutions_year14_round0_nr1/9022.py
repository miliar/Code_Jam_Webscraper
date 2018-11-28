#include<iostream>
#include<fstream>
using namespace std;

int a[4][4], b[4][4];
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, s1, s2;
	cin >> t;
	for(int i = 0; i < t; i++){
		
		cin >> s1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> s2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> b[i][j];
		s1 --;
		s2--;
		int mark[20] = {0}, res = -1, k = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(a[s1][i] == b[s2][j]){
					mark[a[s1][i]]++;
					k++;
					res = a[s1][i];
				}

		cout << "Case #" << i + 1 << ": ";
		if(k == 0)
			cout << "Volunteer cheated!" << endl;
		else if(k > 1)
			cout << "Bad magician!" << endl;
		else
			cout << res << endl;
	}
	return 0;
}