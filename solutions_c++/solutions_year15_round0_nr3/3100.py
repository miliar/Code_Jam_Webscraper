#include<cstdlib>
#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<queue>
#include<functional>
#include<map>
using namespace std;

int q[4][4] = { 
	{ 1, 2, 3, 4 }, 
	{ 2, -1, 4, -3 }, 
	{ 3, -4, -1, 2 }, 
	{ 4, 3, -2, -1 } };
int mult(int x, int y)
{
	int temp = q[abs(x)-1][abs(y)-1];
	if (x*y > 0){
		return temp;
	}
	else{
		return -1 * temp;
	}
}
int divid(int x, int y){ // finds v such that x*v = y
	return mult(-1 * x, y);
}
int find(int loc, int length, int data[], int total) {
	int mod = loc % length;
	int cycle = (loc - mod) / length % 4;
	int temp = data[mod];
	for (int i = 0; i < cycle; i++){
		temp = mult(total, temp);
	}
	return temp;
}
//bool dij(int L, int X, string input){
//
//	int* data = new int[L];
//	int temp = 1; 
//	for (int i = 0; i < L; i++)
//	{
//		int go;
//		if (input[i] == '1'){ go = 1; }
//		if (input[i] == 'i'){ go = 2; }
//		if (input[i] == 'j'){ go = 3; }
//		if (input[i] == 'k'){ go = 4; }
//		temp = mult(temp, go);
//		data[i] = temp;
//		
//	}
//	int total = data[L - 1];
//	int loc;
//	bool flag = false;
//	for (int i = 0; i < 4*L; i++){
//		int a = find(i, L, data, total);
//		if (a == 2) { loc = i; flag = true; break; }
//	}
//	if (flag == false){
//		return false;
//	}
//	//-------------------------------------
//	bool f = false; 
//	for (int i = 0; i < 4 * L; i++){
//		int a = divid(find(loc + i, L, data, total), find(loc + i + 1, L, data, total));
//		if (a == 3){ f = true; break; }
//	}
//	if (f == false) {
//		return false;
//	}
//	int t = find(X, L, data, total);
//	return ((divid(4,t ) == 4));
//
//
//
//}
bool dij(int L, int X, string input){
	int temp = 1; 
	int loc1;
	bool flag = false;
	for (int i = 0; i < L*X; i++)
	{
		int go;
			if (input[i % L] == '1'){ go = 1; }
			if (input[i % L] == 'i'){ go = 2; }
			if (input[i % L] == 'j'){ go = 3; }
			if (input[i % L] == 'k'){ go = 4; }
			temp = mult(temp, go);
			if (temp == 2){
				loc1 = i; flag = true;  break;
			}
	}
	if (flag == false) {
		return false;
	}
	flag = false;
	temp = 1;
	int loc2;
	for (int j = loc1 + 1; j < L*X; j++){

		int go;
		if (input[j % L] == '1'){ go = 1; }
		if (input[j % L] == 'i'){ go = 2; }
		if (input[j % L] == 'j'){ go = 3; }
		if (input[j % L] == 'k'){ go = 4; }
		temp = mult(temp, go);
		if (temp == 3){
			loc2 = j; flag = true; break;
		}
	}
	if (flag == false) {
		return false;
	}
	flag = false; 
	temp = 1;
	for (int k = loc2 + 1; k < L*X; k++){
		int go;
		if (input[k % L] == '1'){ go = 1; }
		if (input[k % L] == 'i'){ go = 2; }
		if (input[k % L] == 'j'){ go = 3; }
		if (input[k % L] == 'k'){ go = 4; }
		temp = mult(temp, go);
		
	}
	if (temp == 4){
		return true;
	}
	return false; 
}
void main() {

	ifstream q;
	q.open("C:\\Users\\songr_000\\Desktop\\C-small-attempt1.in");
	int T;
	q >> T;
	ofstream ofs("C:\\Users\\songr_000\\Desktop\\outputC.txt");
	for (int i = 1; i <= T; i++){
		int L;
		int X;
		q >> L;
		q >> X;
		string input;
		q >> input;
		if (dij(L, X, input)){
			ofs << "Case #" << i << ": " <<"YES" << endl;
		}
		else{
			ofs << "Case #" << i << ": " << "NO" << endl;
		}
		
		
	}
	ofs.close();

	

}
