#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <queue>

using namespace std;

int foo(priority_queue<int>& pq) {
	int maxi = pq.top();
	pq.pop();
	if (maxi <= 2)
		return maxi;
	pq.push(maxi/2 + maxi%2);
	pq.push(maxi/2);
	return min(maxi, 1 + foo(pq));
}

int main() {
	int num, noempty, maxi, tmp, res;
	string line;
  	ifstream myfile ("B-large.in");
  	int count = 1;
  	string temp;
  	ofstream ofile;
  	ofile.open("output_large.txt");
  	if (myfile.is_open()) {
		getline(myfile, line);
		num = atoi(line.c_str());
		while (getline(myfile,line)) {
			noempty = atoi(line.c_str());
			getline(myfile, line);
			istringstream ss(line);
			maxi = INT_MIN;
			vector<int> plate(noempty, 0);
			for (int i = 0; i < noempty; i++) {
				ss>>temp;
				tmp = atoi(temp.c_str());
				plate[i] = tmp;
				maxi = max(tmp, maxi);
			}
			res = INT_MAX;
			//cout<<maxi<<endl;
			for (int N = maxi; N > 0; N--) {
				tmp = 0;
				for (int i = 0; i < noempty; i++) {
					tmp += plate[i]/N;
					if (plate[i]%N == 0)
						tmp -= 1;
				}
				res = min(res, N+tmp);
			}
			plate.erase(plate.begin(), plate.begin()+noempty);
			ofile<<"Case #"<<count<<": "<<res<<endl;
			count++;
		}
	}
}