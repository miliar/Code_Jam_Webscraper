#include<vector>
#include<fstream>

using namespace std;

int main(){
	ifstream in("A-large (1).in");
	ofstream out("ans.txt");
	int T;
	in >> T;
	for (int t = 1; t <=T; t++){
		int N;
		in >> N;
		vector<int> vt(N, 0);
		for (int n = 0; n < N; n++){
			in >> vt[n];
		}
		int y = 0, z = 0, d=0;
		for (int i = 1; i < N; i++){
			if (vt[i]<vt[i - 1]){
				y += vt[i-1] - vt[i];
				if (vt[i-1] - vt[i] > d){
					d = vt[i-1] - vt[i];
				}
			}
		}
		for (int i = 0; i < N - 1; i++){
			if (vt[i] <= d){
				z += vt[i];
			}
			else{
				z += d;
			}
		}
		out << "Case #" << t << ": " << y <<" "<< z << endl;
	}
	in.close();
	out.close();
}