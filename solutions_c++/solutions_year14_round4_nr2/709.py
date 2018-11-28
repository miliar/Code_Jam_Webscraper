#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int debug = false;

class Solver{
public:
	ifstream &in;
	int N;
	vector<long> v;
	vector<bool> done;

	Solver(ifstream &input):in(input){
		in>>N;
		v = vector<long>();

		v.resize(N);
		done.resize(N);
		for(int i=0;i<N;++i){
			in>>v[i];
			done[i]=false;
			if(debug)
				cout<<v[i]<<" ";
		}
		if(debug)
			cout<<"\n";
	}

	int min(int a, int b){
		return a<b?a:b;
	}

	int solve(){
		int result=0;
		for(int i=0;i<N;++i){
			int pos = min_element(v.begin(), v.end())-v.begin();
			if(debug)
				cout<<"minimum at "<<pos<<"\n";
			int c = 0;
			for(int j=0;j<pos;++j)
				if(!done[j])
					++c;
			v[pos] = 1000000001;
			done[pos] = true;
			if(debug)
				cout<<"distance to end: "<<min(c, N-i-c-1)<<"\n";
			result += min(c,N-i-c-1);
		}
		return result;
	}
};


int main(){
	ifstream in;
	ofstream out;
//	string fileName = "B-test-large";
//	string fileName = "B-small-attempt0";
	string fileName = "B-large";

//if(true){
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
//}
//else {
	/*out.open(fileName+".in");

	int limit=1000;
	out<<1<<"\n";
	out<<limit<<"\n";
	vector<int> d;
	d.resize(limit);
	for(int i=0;i<limit;++i)
		d[i] = i;
	random_shuffle(d.begin(), d.end());
	for(int i=0;i<limit;++i){
		out<<d[i]<<" ";
		cout<<d[i]<< " ";
	}
}*/
	return 0;
}

