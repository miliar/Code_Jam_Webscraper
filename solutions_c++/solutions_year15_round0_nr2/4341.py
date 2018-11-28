#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

void special(vector<int>, int, int);

int minimum;
ifstream infile("B-small-attempt2.in");
ofstream outfile("pancakes.out");

bool reversesort( int l, int h ){
	return h <= l;
}

void print(vector<int> v ){
	for( int i=0;i<v.size();++i ){
		cout<<v[i]<<" ";
	}
	cout<<endl;
}

void eat( vector<int> v, int passed ){
	if( passed > minimum ) return;
	bool done = true;
	for( int k = 0 ; k < v.size() ; ++k ){
		if( v[k] > 0 ){
			v[k] = v[k]-1;
		}
		if( v[k] != 0 ) done=false;
	}
	passed++;
	if( done && passed < minimum ) {
		minimum = passed;
		return;
	}
	
	eat(v, passed);
	special(v, passed,-1000);
}

void special( vector<int> v, int passed , int level){
	if( passed > minimum ) return;

	int step = v[0]/2;
	for( int i = 0 ; i < step ; ++i ){
		vector<int> w(v);
		w[0]-=(i+1);
		w.push_back(i+1);
		
		sort(w.begin(), w.end(), reversesort);
		eat(w, passed+1);
		if( level == 1 ){
			//cout<<"level 1"<<endl;
			//print(w);
		}
		special(w, passed+1 ,level+1);
	}
}


int main(){
	int T;
	infile>>T;
	
	for( int t = 1 ; t <= T ; ++t ){
		cout<<"case "<<t<<endl;
		int D;
		infile>>D;
		vector<int> pancakes;
		for( int i=0;i< D;++i ){
			int in;
			infile>>in;
			pancakes.push_back(in);
		}
		sort(pancakes.begin(), pancakes.end(), reversesort);
		//print(pancakes);
		minimum = pancakes[0];
		eat(pancakes,0);
		special(pancakes,0,0);
		outfile<<"Case #"<<t<<": "<<minimum<<endl;
	}
	
	return 0;
}
	