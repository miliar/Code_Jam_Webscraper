#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in = ifstream("in.txt");
	ofstream out = ofstream("out.txt");

	int T;
	in>>T;
	int testn = 1;
	while(T-- > 0){
		int N,M;
		in>>N>>M;

		vector<vector<int>> m(N , vector<int>(M , 0));
		vector<int> rowmax(N , 0);
		vector<int> colmax(M, 0);
		for(int i=0 ; i<N ; i++){
			for(int j=0 ; j<M ; j++){
				int n;
				in>>n;
				m[i][j] = n;

				if(m[i][j] > rowmax[i]) rowmax[i] = m[i][j];
				if(m[i][j] > colmax[j]) colmax[j] = m[i][j];
			}
		}

		bool res = true;
		for(int i=0 ; i<N ; i++){
			for(int j=0 ; j<M ; j++){
				if(!(m[i][j] >=rowmax[i] || m[i][j]>=colmax[j])) { 
					res = false;
					break;
				}
			}
			if(!res) break;
		}

		if(res) out<<"Case #"<<testn++<<": YES"<<endl;
		else out<<"Case #"<<testn++<<": NO"<<endl;
	}
	return 1;
}