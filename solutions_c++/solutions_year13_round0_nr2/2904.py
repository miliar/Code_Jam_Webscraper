#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){
        ifstream in("B-large.in");
        ofstream out("foo1");

        int T;
        in >> T;

	for (int p = 0; p < T; p++){
		string answer = "YES";
		int m, n;
		in >> n >> m;
		int matrix[n][m];
		for (int i = 0; i < n; i ++){
			for (int j = 0; j < m; j++){
				in >> matrix[i][j];
			}
		}

		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				int flag = 0;
				int flag1 = 0;
				for (int a = i+1; a < n; a++){
					if (matrix[a][j] > matrix[i][j]){
						flag ++ ;
						a = n;
					}
				}
				for (int a = i-1; a >= 0; a--){
					if (matrix[a][j] > matrix[i][j]){
						flag ++;
						a = -1;
					}
				}
				for (int a = j + 1; a < m; a++){
					if (matrix[i][a] > matrix[i][j]){
						flag1 ++;	
						a =m;
					}
				}
				for (int a = j - 1; a >= 0; a--){
					if (matrix[i][a] > matrix[i][j]){
						flag1 ++;
						a = -1;
					}
				}

				if ((i ==0 && j==0) || (i == n-1 && j == 0) || (i == 0 && j == m-1) || (i == n-1 && j == m-1)){
					if (flag == 1 && flag1 == 1) answer = "NO";
				}
				else if (i == 0 || i == n-1 || j == 0 || j == m-1){
					if (flag >= 1 && flag1 >= 1) answer = "NO";
				} 
				else if (flag >= 1 && flag1 >= 1)
					answer = "NO";
			}
		}
		out << "Case #" << p+1 << ": " << answer << endl;
	}
	
	return 0;
}
