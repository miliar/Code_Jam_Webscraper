#include<iostream>
#include<string>
#include<fstream>

using namespace std;
int mult[5][5] = {{0,0,0,0,0}, 
{0, 1, 2, 3, 4}, 
{0, 2, -1, 4, -3},
{0, 3, -4, -1, 2},
{0, 4, 3, -2, -1}};

inline int multiply(int x, int y){
	int res = 1;
	if(x < 0){
		res *= -1;
		x = -x;
	}
	if(y < 0){
		res *= -1;
		y = -y;
	}
	res *= mult[x][y];
	return res;
}
inline int get(char c){
	if(c == 'i')
		return 2;
	if(c == 'j')
		return 3;
	return 4;
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int L, X;
		cin >> L >> X;
		string s, str = "";
		cin >> s;
		for(int i = 0; i < X; i++)
			str += s;
		int res = 1, k = 0;
		while(k < str.length() && res != 2){

			res = multiply(res, get(str[k]));
			k++;
		}
		res = 1;
		while(k < str.length() && res != 3){

			res = multiply(res, get(str[k]));
			k++;
		}
		res = 1;
		while(k < str.length()){

			res = multiply(res, get(str[k]));
			k++;
		}
		cout << "Case #" << i + 1 << ": ";
		if(res == 4)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}