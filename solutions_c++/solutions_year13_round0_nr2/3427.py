#include<iostream>
#include<fstream>
using namespace std;
ifstream in("2.in");
ofstream out("2.out");
int a[200][200];

int n, m;

bool judge1(int x, int y){
	for (int k = 1; k <= n; k++)
		if (a[k][y] > a[x][y]) return false;
	return true;
}
bool judge2(int x, int y){
	for (int k = 1; k <= m; k++)
		if (a[x][k] > a[x][y]) return false;
	return true;
}

int main(){
	int iTestSum;
	in >> iTestSum;
	for (int iTest = 1; iTest <= iTestSum; iTest++){
		out << "Case #" << iTest << ": ";

		in >> n >> m;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				in >> a[i][j];
		bool ans = true;
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++){

				if (!(judge1(i,j) || judge2(i,j)))
					{ans = false;cout << 1;}
				else cout << 0;

			}
			cout << endl;
		}
		if (ans) out << "YES";
		else out << "NO";
		out << endl;
	}
}
//#include<iostream>
//#include<fsteam>
//using namespace std;
//ifstream in("2.in");
//ofstream out("2.out");
//int main(){
//	int iTestSum;
//	in >> iTestSum;
//	for (int iTest = 1; iTest <= iTestSum; iTest++){
//		out << "Case #" << iTest << ": ";
//
//		out << endl;
//	}
//}
