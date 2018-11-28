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
	int T; cin>>T;
for (int i=0;i<T;++i){

	int N;
	cin>>N;

	vector<double> Naomi,Ken; double d;
	for(int j=0;j<N;++j){cin>>d; Naomi.push_back(d);}
	for(int j=0;j<N;++j){cin>>d; Ken.push_back(d);}
	sort(Naomi.begin(),Naomi.end());
	sort(Ken.begin(),Ken.end());
	//Deceitful
	int cnt=0;
	vector<double>::iterator iN=Naomi.begin(),iK=Ken.begin();
	while(iN!=Naomi.end()){
		if(*iN>*iK){++cnt; ++iN; ++iK;}
		else{ ++iN;}
	}
	//War
	int cntW=0;
	 iN=Naomi.begin(),iK=Ken.begin();
	while(iK!=Ken.end()){
		if(*iN<*iK){++iN;++iK;}
		else{++iK;++cntW; }

	}
	cout<<"Case #"<<i+1<<": "<<cnt<<" "<<cntW<<endl;
}
}

