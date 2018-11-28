#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


class Solver{
public:
	ifstream &in;
	int N;
	vector<int> sizes;
	vector<bool> done;
	int diskSize;

	Solver(ifstream &input):in(input){
		in>>N;
		in>>diskSize;
		sizes = vector<int>();
		done = vector<bool>();
		sizes.resize(N);
		done.resize(N);
		for(int i=0;i<N;++i){
			in>>sizes[i];
			done[i]=false;
		}
		sort(sizes.begin(), sizes.end());
		reverse(sizes.begin(), sizes.end());
	}

	int solve(){
		int result=0;
		for(int i=0;i<N;++i){
			if(done[i])
				continue;
			++result;
//			cout << sizes[i]<<"\n";
			int remaining = diskSize - sizes[i];
			for(int j=i+1;j<N;++j){
				if(done[j])
					continue;
				if(sizes[j]>remaining)
					continue;
				done[j]=true;
//				cout << sizes[j]<<"\n";
				break;
			}
		}
		return result;
	}
};


int main(){
	ifstream in;
	ofstream out;
//	string fileName = "A-small-attempt0";
//	string fileName = "A-small";
	string fileName = "A-large";
	in.open(fileName+".in");
	out.open(fileName+".out");

	int T;
	in>>T;
	for(int i=1;i<=T;++i){
		cout<< "Case #"<<i<<": ";
		Solver solver(in);
		int result=solver.solve();
		cout<<result<<"\n";
		out << "Case #"<<i<<": "<<result<<"\n";
	}

	return 0;
}

