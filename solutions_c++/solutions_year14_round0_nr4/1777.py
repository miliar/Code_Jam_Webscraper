#include <bits/stdc++.h>
using namespace std;

vector<double> naomi;
vector<double> ken;
vector<double> naomi2;
vector<double> ken2;

int main(){
	int tc;
	cin >> tc;
	for(int d=1;d<=tc;d++){
		int n;
		cin >> n;
		for(int i=0;i<n;i++){
			double temp;
			cin >> temp;
			naomi.push_back(temp);
			naomi2.push_back(temp);
		}
		for(int i=0;i<n;i++){
			double temp;
			cin >> temp;
			ken.push_back(temp);
			ken2.push_back(temp);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		sort(naomi2.begin(),naomi2.end());
		sort(ken2.begin(),ken2.end());
		
		int counter=0;
		for(int i=0;i<n;i++){
			int lastIndex = naomi.size()-1;
			if(naomi[lastIndex]>ken[lastIndex]){
				counter++;
				naomi.erase(naomi.begin()+lastIndex);
				ken.erase(ken.begin()+lastIndex);
			}
			else{
				naomi.erase(naomi.begin());
				ken.erase(ken.begin()+lastIndex);
			}
		}
		
		int counter2=0;
		for(int i=0;i<n;i++){
			int lastIndex = naomi2.size()-1;
			if(naomi2[lastIndex]<ken2[lastIndex]){
				naomi2.erase(naomi2.begin()+lastIndex);
				ken2.erase(ken2.begin()+lastIndex);
			}
			else{
				naomi2.erase(naomi2.begin()+lastIndex);
				ken2.erase(ken2.begin());
				counter2++;
			}
		}
		
		printf("Case #%d: %d %d\n",d,counter,counter2);
		
	}
	
	return 0;
}
