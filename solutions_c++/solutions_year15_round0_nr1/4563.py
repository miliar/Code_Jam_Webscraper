#include<fstream>


using namespace std;

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	in >> t;
	for(int k = 1; k <= t; k++){
		int sMax;
		in >> sMax;
		int cnt = 0;
		int amici = 0;
		for(int i = 0; i <= sMax; i++){
			int s;
			char c;
			in >> c;
			s = c - '0';
			if(i > cnt){
				amici += (i-cnt);
				cnt = i;
			}
			cnt += s;
		}
		out << "Case #" << k << ": " << amici << endl;
	}
}
		
