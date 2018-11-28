#include <fstream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T = 0;
	in >> T;	
	for (int i = 0; i < T; ++i)
	{
		unordered_set<int> check;
		for (int j = 0; j < 10; ++j)
		{
			check.insert(j);
		}
		int N = 0;
		in >> N;
		out << "Case #"<< i+1 <<": ";
		if(N == 0) out<<"INSOMNIA"<<endl;
		else {
			int tmp = N;
			int count = 1;
			while(!check.empty()) {	
				int j = 0;	
				while(tmp) {
					j = tmp%10;
					if(check.find(j) != check.end()) {
						check.erase(j);
					}
					tmp/=10;
				}
				count++;
				tmp = N*count;
			}
			out<<N*(count-1)<<endl;
		}
		


	}

}