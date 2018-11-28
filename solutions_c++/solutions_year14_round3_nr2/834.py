#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool check(vector<string> &v){
	vector<bool> visited(26,false);
	char lastv = '.';
	for(int i=0; i<v.size(); i++){
//		for(int j=0; v[i].at(j)!='.'; j++){
		for(int j=0; j<v[i].length(); j++){
			char c = v[i].at(j);
			if(c!=lastv){
				if(visited[c-'a'])
					return false;
				else{
					visited[c-'a']=true;
					lastv = c;
				}
			}
		}
	}
	return true;
}

int main(){

	int NSteps;
	cin >> NSteps;

	for(int s=1; s<=NSteps; s++){
		int nSol=0;
		cout << "Case #" << s << ": ";
		int nTrains;
		cin >> nTrains;
		vector<string> t(nTrains);
		for(int i=0; i<t.size(); i++){
			cin >> t[i];
		//	t[i] += ".";
		//	t[i] += to_string(static_cast<unsigned long>(i));
		}
		sort(t.begin(), t.end());
		if(check(t)) 
			nSol++;

		long long int factId=1;
		long long int part = 1;
		int nfol = 1;
		//count identical neighbors
		for(int i=1; i<t.size(); i++){
			if(t[i] == t[i-1]){
				nfol++;
				part*=nfol;
			}
			else{
				factId*=part;
				part=1;
				nfol=1;
			}
		}

		while(std::next_permutation(t.begin(),t.end())){
			if(check(t))
				nSol++;
		}
		cout << (nSol*factId)%1000000007 << endl;
	}
}
