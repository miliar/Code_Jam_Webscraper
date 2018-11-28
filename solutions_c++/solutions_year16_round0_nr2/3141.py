#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <list>

using namespace std;



int main(){
	//run. ./main < in.txt > out.txt
	int TC;
	cin >> TC;
	cin.ignore();
	for(int tc=1;tc<=TC;tc++){
		printf("Case #%d: ", tc);
		string input;
		getline(cin, input);
		stringstream ss(input);
		vector<int> v;
		char c;
		while(ss >> c){
			//cout << c;
			if(c=='+')
				v.push_back(1);
			else
				v.push_back(-1);
		}
		int t=0;
		while(v.size()!=0){
			while(v.size()>0 && v.back()==1)
				v.pop_back();
			if(v.size()>0){

				if(v.front()==1){
					int j=v.size()-1;
					while(v[j]==-1)
						j--;
					t++;
					std::vector<int> nv;
					for(int k=j;k>=0;k--)
						nv.push_back(-v[k]);
					for(int k=j+1;k<v.size();k++)
						nv.push_back(v[k]);
					v.clear();
					v.assign(nv.begin(),nv.end());
				 }
				if(v.front()==-1){
					t++;
					std::vector<int> nv;
					for(int j=v.size()-1;j>=0;j--){
						//cout << -v[j] << endl;
						nv.push_back(-v[j]);
					}
					v.clear();
					v.assign(nv.begin(),nv.end());
				}
			}
		}
		cout << t << endl;
	}
	return 0;
}