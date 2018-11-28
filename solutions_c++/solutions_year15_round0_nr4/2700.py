#include<fstream>
#include<string>

using namespace std;

bool doIt(int x, int r, int c){
	if (x == 1){
		return true;
	}
	if (r > c){
		return doIt(x, c, r);
	}
	if (r == 1 && c == 1){
		return false;
	}
	if (r == 1 && c == 2){
		return x == 2;
	}
	if (r == 1 && c == 3){
		return false;
	}
	if (r == 1 && c == 4){
		return x == 2;
	}
	if (r == 2 && c == 2){
		return x == 2;
	}
	if (r == 2 && c == 3){
		return x == 2 || x == 3;
	}
	if (r == 2 && c == 4){
		return x == 2;
	}
	if (r == 3 && c == 3){
		return x == 3;
	}
	if (r == 3 && c == 4){
		return x == 3||x==2||x==4;
	}
	if (r == 4 && c == 4){
		return x == 2 || x == 4;
	}
}

int main(){
	ifstream in("D-small-attempt1.in");
	ofstream out("ans.txt");
	int T;
	in >> T;
	for (int t = 1; t <= T; t++){
		int x, r, c;
		in >> x >> r >> c;
		if (doIt(x, r, c)){
			out << "Case #" << t << ": GABRIEL"<<endl;
		}
		else{
			out << "Case #" << t << ": RICHARD" << endl;
		}
	}
	in.close();
	out.close();
}