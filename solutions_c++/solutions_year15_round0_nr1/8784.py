#include <fstream>
#include <vector>


using namespace std;

int main(){
	ifstream fin("in.in");
	ofstream fout("out.out");
	int n;
	fin >> n;
	vector<int> v;
	for(int i = 0; i < n ;i++){
		int m;
		fin >> m;
		int q;
		int n = 0;
		int e = 0;
		for(int j = 0; j<=m;j++){
			char q;
			fin >> q;
			if(n+e < j){
				e += j - n - e;}
			n += q - '0';	
		}
		fout << "Case #" << i+1 << ": " << e <<endl;
	}
	return 0;
}
