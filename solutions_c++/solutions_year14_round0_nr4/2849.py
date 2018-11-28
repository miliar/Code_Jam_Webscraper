#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int tests;
	cin>>tests;
	for(int t=0; t<tests; t++){
		int n;
		cin>>n;
		double  naomi[n];
		double ken[n];

		for (int i = 0; i < n; i++){
			cin>>naomi[i];
		}
		for (int i = 0; i < n; i++){
			cin>>ken[i];
		}

   		sort(naomi, naomi + n);
   		sort(ken, ken + n);

		int count1, count2;
		count1=0;
		count2=0;
		int cap=n;
		int nao=0;
		int ke=0;

		while(nao<n){
			if(ke>cap)
				break;

			if(naomi[nao]>ken[ke]){
				ke++;
				nao++;
				count1++;
			}
			else {
				nao++;
				cap --;
			}
		}
		count1+=n-nao;


		int j = 0;
		for(int i=0; i<n; i++){
			while(j<n){
				if(naomi[i]<ken[j]){
					//cout<<"naomi"<<naomi[i];
					j++;
					count2++;
					break;
				}
				else j++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<count1<<" "<<n-count2<<endl;
	}

}