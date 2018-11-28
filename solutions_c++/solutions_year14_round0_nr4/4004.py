#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#define FOR(i,j) for(int i=0;i<j;i++)
using namespace std;

int main(){
	int T,N;
	cin>>T;
	bool flag;
	int casenum=0,war,dwar;
	double weight;
	while(casenum<T){
		casenum++;
		war=0;dwar=0;
		cin>>N;
		flag=true;
		vector<double> ken,naomi,backup;
		FOR(i,N){
			cin>>weight;
			naomi.push_back(weight);
		}
		FOR(i,N){
			cin>>weight;
			ken.push_back(weight);
			backup.push_back(weight);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		sort(backup.begin(),backup.end());
		//Optimal War
		FOR(i,N){
			weight=naomi[i];
			flag=true;
			FOR(j,ken.size()){
				if (ken[j]>weight) {
					
					flag=false;
				//	cout<<weight<<" VS "<<ken[j]<<endl;
					ken.erase(ken.begin()+j);
					break;
				}
			}
			if (flag) {
				war++;
				ken.erase(ken.begin());
			}
		}
		//Deceitful War Now

		FOR(i,N){
			weight=backup[i];
			flag=true;
			FOR(j,naomi.size()){
				if (naomi[j]>weight) {
					dwar++;
					naomi.erase(naomi.begin()+j);
					flag=false;
					break;
				}
			}
			if (flag){
				naomi.erase(naomi.begin());
			}
		}
		printf("Case #%d: %d %d\n",casenum,dwar,war);
	
	}

}