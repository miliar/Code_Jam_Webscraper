#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>

using namespace std;

int calcDWScore(set<float> naomi, set<float> ken){

	set<float>::iterator itKen, itNaomi;
	int n=0;

	itKen=ken.end();
	itKen--;
	itNaomi=naomi.begin();
	while(*itKen>*itNaomi){

		if(*itNaomi>*ken.begin()){
			ken.erase(ken.begin());
			naomi.erase(itNaomi);
			n++;
		}
		else{
			ken.erase(itKen);
			naomi.erase(itNaomi);
		}

		if(ken.size()<=0)
			break;

		itKen=ken.end();
		itKen--;
		itNaomi=naomi.begin();

	}
	

	return naomi.size()+n;

}

int calcWScore(set<float> naomi, set<float> ken){
	set<float>::iterator itKen, itNaomi, itKen1, itNaomi1;

	itKen=ken.begin();
	itNaomi=naomi.begin();
	
	while(itKen!=ken.end() && itNaomi!=naomi.end()){
		while(*itKen<*itNaomi){
			itKen++;
			if(itKen==ken.end())
				break;
		}

		if(itKen==ken.end())
				break;
		itKen++;
		itNaomi++;

		itKen1=itKen;
		itNaomi1=itNaomi;

		itKen1--;
		itNaomi1--;

		ken.erase(itKen1);
		naomi.erase(itNaomi1);

	}

	return ken.size();

}

int main(){
	ifstream inp("dwinput.txt");
	ofstream out("dwoutput.txt");
	
	int t,n,cno=0;
	float tmp;

	inp>>t;

	for(int i=0;i<t;i++){
		cno++;
		set<float> naomi,ken;
		inp>>n;

		for(int j=0;j<n;j++){
			inp>>tmp;
			naomi.insert(tmp);
		}

		for(int j=0;j<n;j++){
			inp>>tmp;
			ken.insert(tmp);
		}

		// for(auto i:ken)
		// 	cout<<fixed << setprecision(6)<<i<<" ";
		// cout<<"\n";
		// for(auto i:naomi)
		// 	cout<<fixed << setprecision(6)<<i<<" ";
		// cout<<"\n\n";

		out<<"Case #"<<cno<<": "<<calcDWScore(naomi,ken)<<" "<<calcWScore(naomi,ken)<<"\n";
	}


}