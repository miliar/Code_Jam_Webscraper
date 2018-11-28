#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int t;
	cin>>t;
	string output[t];
	for(int k=1; k<=t; k++){
		int n;
		cin>>n;
		double temp;
		vector<double> arr1, arr2;
		for(int i=0; i<n; i++){	
			cin>>temp;
			arr1.push_back(temp);
		}
		for(int j=0; j<n; j++){
			cin>>temp;
			arr2.push_back(temp);
		}
		std::sort (arr1.begin(), arr1.end());
		std::sort (arr2.begin(), arr2.end());
		// for(int j=0; j<n; j++){
		// 	cout<<arr1[j]<<" ";
		// }
		// cout<<endl;
		// for(int j=0; j<n; j++){
		// 	cout<<arr2[j]<<" ";
		// }
		// cout<<endl;
		int i=0, j=0;
		int w=0, dw=0;
		while(j<n){
			if(arr1[i] < arr2[j]){
				i++;
				j++;
			}
			else{
				j++;
				w++;
			}
		}
		i = 0;
		j = 0;
		while(i<n){
			if(arr1[i] < arr2[j]){
				i++;
			}
			else{
				i++;
				j++;
				dw++;
			}
		}
		output[k-1] = "Case #" + std::to_string(k) + ": " + std::to_string(dw) + " " + std::to_string(w);
	}
	for(int i=0; i<t; i++){
		cout<<output[i]<<endl;
	}
	return 0;
}