//============================================================================
// Name        : A.cpp
// Author      : Yul Obraz
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

struct party
{
public: int id;
 int c;
};
bool func (party* x, party*y ) {return x->c> y->c;}
string calc(vector<party*>& src){
	int sum =0;
	for(std::vector<party*>::iterator it = src.begin(); it != src.end(); ++it) {
		party *p= it[0];
	    sum +=p->c;
	 }
	cerr<<sum<<endl;
	sort(src.begin(), src.end(), func);
	while(src[0]->c!=0){
		cerr<<(sum-1) <<" "<< 2*(src[1]->c)<<endl;
		if((sum-1) >= 2*(src[1]->c)){
			char v='A'+(char)src[0]->id;
			cout<<v<<" ";
			src[0]->c--;
			sum--;
			sort(src.begin(), src.end(), func);
		}else{
			char v='A'+(char)src[0]->id;
			char v2='A'+(char)src[1]->id;
			cout<<v<<v2<<" ";
			src[0]->c--;
			src[1]->c--;
			sum-=2;
			sort(src.begin(), src.end(), func);
		}
	}
	return "";
}
int main(int argc,char *argv[]) {
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		int NParties;
		cin>>NParties;
		vector<party*> parties;
		for(int j=0; j<NParties; j++){
			party *p = new party();
			p->id=j;
			cin >> p->c;
			parties.push_back(p);
		}

		cout << "Case #"<< (i+1)<<": ";
				calc(parties);
		cout<< endl;
	}
	return 0;
}
