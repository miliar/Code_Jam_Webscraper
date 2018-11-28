#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int i=0;i<T;++i){
		int r1;
		cin>>r1;
		vector<int> cards; int c;
		for(int j=0;j<16;++j){
			cin>>c; if(j/4==r1-1) cards.push_back(c);
		}
		int r2;
		cin>>r2;
		int h=0,ch;
		for(int j=0;j<16;++j){cin>>c;
		if(j/4==r2-1){
			for(int k=0;k<4;++k){if(c==cards[k]) {++h; ch=c;}}
		}
	}
		if(h==0) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;

		else if(h==1) cout<<"Case #"<<i+1<<": "<<ch<<endl;
		else  cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
}

