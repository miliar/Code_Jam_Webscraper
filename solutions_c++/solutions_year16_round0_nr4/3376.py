#include <fstream>
using namespace std;


int main(){
	int t,k,c,s;
	ifstream in("D-small-attempt0.in");
	ofstream out("lg.out");
	in >> t;
	for (int tt = 0; tt < t; tt++){
		in >> k >> c >> s;
		out << "Case #" << tt+1 << ": ";
		for (int i = 1; i <= k;i++ )
			out << i  << ' ';
		out << endl; 
	}
	in.close();
	out.close();
}
