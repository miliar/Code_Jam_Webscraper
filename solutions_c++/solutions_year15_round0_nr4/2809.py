#include<iostream>
#include<fstream>
#include<string>
#define re(i,j,k) for(int i=j;i<k;i++)
using namespace std;
int main(){
	ofstream fout("out.txt");
	ifstream fin("D-small-attempt1.in");
	int t, x, r, c;
	string ans;
	fin >> t;
	int z = 0;
	while (++z!=t+1){
		fin >> x >> r >> c;
		ans = "RICHARD";
		if (x == 1 || 
			(x == 2 && ((r*c) % 2 == 0)) || 
			(x == 3 && (r*c == 6 || r*c == 12 || r*c == 9)) ||
			(x == 4 && (r*c == 16 || r*c == 12))
			)
			ans = "GABRIEL";
		fout << "Case #" << z <<": "<<ans<<endl;
	}
}