#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("D-small-attempt4.in");
	ofstream fout("out.out");
	int t;
	fin >> t;
	int x,r,c;
	bool flag;
	int count = 1;
	while(t--){
		fin >> x >> r >> c;
if(x == 1)flag = true; // Gabriel
		else if(x == 2){
			if(r%2 == 0 || c%2 == 0 ){
				flag = true;
			}
			else flag = false;
		}
		else if(x == 3){
		
		if( r== 3 && c == 2){
		flag = true;
		}
		else if( r== 3 && c == 3){
		flag = true;
		}
		else if( r== 3 && c == 4){
		flag = true;
		}
		else if( r== 2 && c == 3){
		flag = true;
		}
		else if( r== 4 && c == 3){
		flag = true;
		}
		else flag = false;
		}
		else if(x == 4){
		if( r== 4 && c == 3){
		flag = true;
		}
		else if( r== 4 && c == 4){
		flag = true;
		}
		else if( r== 3 && c == 4){
		flag = true;
		}
		
		else flag = false;
		}
		if(flag)fout<<"Case #"<<count++<<": "<<"GABRIEL\n";
		else fout<<"Case #"<<count++<<": "<<"RICHARD"<<'\n';
		
	}
	fin.close();
	fout.close();
	return 0;
}
