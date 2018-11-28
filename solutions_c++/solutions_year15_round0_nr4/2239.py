#include<fstream>

using namespace std;

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	int t;
	in >> t;
	for(int k = 1; k <= t; k++){
		int x,r,c;
		in >> x >> r >> c;
		if(x > r && x > c){
			out << "Case #" << k << ": RICHARD" << endl;
			continue;
		}
		if(x == 1){
			out << "Case #" << k << ": GABRIEL" << endl;
			continue;	
		}
		if(x == 2){
			if(r % 2 == 0 || c % 2 == 0){
				out << "Case #" << k << ": GABRIEL" << endl;
				continue;
			}else{
				out << "Case #" << k << ": RICHARD" << endl;
				continue;
			}
		}
		if(x == 3){
			if(r==1 || c == 1){
				out << "Case #" << k << ": RICHARD" << endl;
				continue;
			}
			if(r % 3 != 0 && c % 3 != 0){
				out << "Case #" << k << ": RICHARD" << endl;
				continue;
			}
			out << "Case #" << k << ": GABRIEL" << endl;
			continue;
		}
		
		if(x == 4){
			if(r == 1 || c == 1){
				out << "Case #" << k << ": RICHARD" << endl;
			}else if(r == 2 || c == 2) out << "Case #" << k << ": RICHARD" << endl;
			else out << "Case #" << k << ": GABRIEL" << endl;
			continue;
		}
	}
}		
