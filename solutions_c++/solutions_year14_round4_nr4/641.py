#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

static int debug = true;

class Solver{
public:
	ifstream &in;
	ofstream &out;
	int N; // number of servers
	int M; // number of strings
	vector<string> s;

	Solver(ifstream &input, ofstream &output):in(input), out(output){
		in>>M;
		in>>N;
		s = vector<string>();
		s.resize(M);
		for(int i=0;i<M;++i)
			in>>s[i];
	}

	void solve(){
		//first, we precalculate the substrings of each string.
		vector<vector<string>> ties = vector<vector<string>>();
//		cout<<"ties:\n";
		ties.resize(M);
		for(int i=0;i<M;++i){
				ties[i].resize(s[i].length()+1);
			for(int j=0;j<=s[i].length(); ++j){
				ties[i][j]=s[i].substr(0,j);
//				cout<<'"'<<ties[i][j]<<'"'<<" ";
			}
//			cout<<"\n";
		}
//		cout<<"\n";

		int m=-1;
		int c=0;
		//we loop over all possible distributions of the strings.
		int server[M];	// we store the selected server for every string.
		for(int i=0;i<M;++i)
			server[i]=0;
		int limit =1;
		for(int i=0;i<M;++i)
			limit*=N;
		for(int i=0;i<limit;++i){
			set<string> servers[N];
			for(int j=0;j<M;++j){
				//add all substrings to the servers
				for(int k=0;k<ties[j].size();++k)
					servers[server[j]].insert(ties[j][k]);
			}

			int cc = 0;
			for(int j=0;j<N;++j)
				cc+=servers[j].size();
			if(cc>m){
				m=cc;
				c=1;
			} else if(cc==m){
				++c;
			}
			/*
				cout<<"max: "<<m<<"\n";
				for(int j=0;j<M;++j)
					cout<<server[j];
				cout<<"\n";
			*/
			//increase the servers distribution
			for(int j=0;j<M;++j){
				if(server[j]==N-1)
					server[j]=0;
				else {
					++server[j];
					break;
				}
			}
		}
		out <<m<<" "<<c<<"\n";
		cout <<m<<" "<<c<<"\n";
	}
};


int main(){
	ifstream in;
	ofstream out;
	string fileName = "D-small-attempt0";
//	string fileName = "D-large";
	in.open(fileName+".in");
	out.open(fileName+".out");

	int T;
	in>>T;
	for(int i=1;i<=T;++i){
		cout<< "Case #"<<i<<": ";
		out <<"Case #"<<i<<": ";
		Solver solver(in, out);
		solver.solve();
	}

	return 0;
}

