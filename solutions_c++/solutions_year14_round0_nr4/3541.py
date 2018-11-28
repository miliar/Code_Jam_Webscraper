#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int n;
		cin>>n;
		vector<double> naomi;
		vector<double> naomi_war;
		vector<double> ken;
		vector<double> ken_war;
		for(int j=0;j<n;j++){
			double temp;
			cin>>temp;
			naomi.push_back(temp);
			naomi_war.push_back(temp);
		}
		for(int j=0;j<n;j++){
			double temp;
			cin>>temp;
			ken.push_back(temp);
			ken_war.push_back(temp);
		}
		sort(naomi.begin(),naomi.end());
		sort(naomi_war.begin(),naomi_war.end());
		sort(ken.begin(),ken.end());
		sort(ken_war.begin(),ken_war.end());
		
		int win_naomi_war = n;
		int ptr1_war=0;
		int ptr2_war=0;
		while(true){
			if(ptr1_war==n) break;
			double item = naomi_war[ptr1_war];
			naomi_war[ptr1_war]=-1;
			ptr1_war++;
			for(int l=0;l<n;l++){
				if(ken_war[l]>item) {
					win_naomi_war--;
					ken_war[l]=-1;
					break;
				}
			}
		}
		
		
		int win_naomi = 0;
		int ptr1=n-1;
		int ptr2=n-1;
		
		while(true){
			//if(naomi[ptr1]==-1 && ptr1>0) ptr1--;
			//if(ken[ptr2]==-1 && ptr2>0) ptr2--;
			if(ptr2<0) break;
			if(naomi[ptr1]>ken[ptr2]) {
				naomi[ptr1]=-1;
				ken[ptr2]=-1;
				win_naomi++;
				ptr1--;
				ptr2--;
			}
			else{
				for(int l=0;l<n;l++){
					if(naomi[l]!=-1&&l<ptr1){
						naomi[l]=-1;
						ken[ptr2]=-1;
						ptr2--;
						break;
					}
					else if(l==ptr1){
						ptr2--;
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<win_naomi<<" "<<win_naomi_war<<endl;
	}
}

