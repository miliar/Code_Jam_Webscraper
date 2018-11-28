#include<iostream>
#include<string>
#include<vector>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

string solve(vector<string> mat){
	
	for(int i=0;i<4;i++)
	if((mat[i][0]=='X'||mat[i][0]=='T') && (mat[i][1]=='X'||mat[i][1]=='T') &&( mat[i][2]=='X'||mat[i][2]=='T') && (mat[i][3]=='X'||mat[i][3]=='T'))
	return "X won";
	for(int i=0;i<4;i++)
	if((mat[0][i]=='X'||mat[0][i]=='T') && (mat[1][i]=='X'||mat[1][i]=='T') &&( mat[2][i]=='X'||mat[2][i]=='T') && (mat[3][i]=='X'||mat[3][i]=='T'))
	return "X won";
	if((mat[0][0]=='X'||mat[0][0]=='T') && (mat[1][1]=='X'||mat[1][1]=='T') &&( mat[2][2]=='X'||mat[2][2]=='T') && (mat[3][3]=='X'||mat[3][3]=='T'))
	return "X won";
	if((mat[0][3]=='X'||mat[0][3]=='T') && (mat[1][2]=='X'||mat[1][2]=='T') &&( mat[2][1]=='X'||mat[2][1]=='T') && (mat[3][0]=='X'||mat[3][0]=='T'))
	return "X won";
for(int i=0;i<4;i++)
	if((mat[i][0]=='O'||mat[i][0]=='T') && (mat[i][1]=='O'||mat[i][1]=='T') &&( mat[i][2]=='O'||mat[i][2]=='T') && (mat[i][3]=='O'||mat[i][3]=='T'))
	return "O won";
	for(int i=0;i<4;i++)
	if((mat[0][i]=='O'||mat[0][i]=='T') && (mat[1][i]=='O'||mat[1][i]=='T') &&( mat[2][i]=='O'||mat[2][i]=='T') && (mat[3][i]=='O'||mat[3][i]=='T'))
	return "O won";
	if((mat[0][0]=='O'||mat[0][0]=='T') && (mat[1][1]=='O'||mat[1][1]=='T') &&( mat[2][2]=='O'||mat[2][2]=='T') && (mat[3][3]=='O'||mat[3][3]=='T'))
	return "O won";
	if((mat[0][3]=='O'||mat[0][3]=='T') && (mat[1][2]=='O'||mat[1][2]=='T') &&( mat[2][1]=='O'||mat[2][1]=='T') && (mat[3][0]=='O'||mat[3][0]=='T'))
	return "O won";
	for(int i=0;i<4;i++)
	if(mat[i].find('.')!=-1)return "Game has not completed";
	return "Draw";
}
int main(){
	READ("A-large.in");
	WRITE("C-large-1.out");
	int tries;
	string tem;
	vector<string> v;
	cin>>tries;
	for(int i=1;i<=tries;i++){
		v.clear();
		cin	>>tem;
		v.push_back(tem);
		cin	>>tem;
		v.push_back(tem);
		cin	>>tem;
		v.push_back(tem);
		cin	>>tem;
		v.push_back(tem);
		cout<<"Case #"<<i<<": "<<solve(v)<<endl;
	}
	return 0;
}
