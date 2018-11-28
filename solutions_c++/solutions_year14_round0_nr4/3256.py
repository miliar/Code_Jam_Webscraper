#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
int deceifulWar(vector<double> naomi, vector<double> ken){
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	int res=0;
	for(int i=0; i<naomi.size(); i++){
		if(naomi[i]<ken[0]){
			ken.pop_back();
		}
		else{
			ken.erase(ken.begin());
			res++;
		}
	}
	return res;
}
int war(vector<double> naomi, vector<double> ken){
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	int res=0;
	for(int i=0; i<naomi.size(); i++){
		int j=0;
		while(j<ken.size()&&ken[j]<naomi[i]){
			j++;
		}
		if(j==ken.size()){
			ken.erase(ken.begin());
			res++;
		}
		else if(ken[j]>=naomi[i]){
			ken.erase(ken.begin()+j);
		}
	}
	return res;
}
int main(){
	ifstream ifs("test.txt");
	ofstream ofs("d-large.out");
	int t;
	ifs>>t;
	for(int i=1; i<=t; i++){
		int n;
		ifs>>n;
		vector<double> naomi;
		for(int j=0; j<n; j++){
			double tmp;
			ifs>>tmp;
			naomi.push_back(tmp);
		}
		vector<double> ken;
		for(int j=0; j<n; j++){
			double tmp;
			ifs>>tmp;
			ken.push_back(tmp);
		}
		stringstream ss;
		ss<<"Case #"<<i<<": "<<to_string(deceifulWar(naomi, ken))<<" "<<to_string(war(naomi, ken))<<endl;
		cout<<ss.str();
		ofs<<ss.str();
	}
	return 0;
}