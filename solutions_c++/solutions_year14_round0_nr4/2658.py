#include<iostream>
#include <algorithm>
#include <vector>
#include<fstream>
using namespace std;


int main(){
	int i,j,t,n,k,count,count1;
	int number=1;
	ofstream myfile;
	myfile.open ("output.txt");
	double p;
	vector<double> a;
	vector<double> b;
	cin>>t;
	while(t--){
		cin>>n;
		for(i=0;i<n;i++){
			cin>>p;
			a.push_back(p);
		}
		for(i=0;i<n;i++){
			cin>>p;
			b.push_back(p);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		j=0;
		i=0;
		count=0;
		k=n-1;
		while(i<n){
			if(a[i]>b[j]){
				i++;
				j++;
				count++;
			}
			else{
				i++;
			}
		}
		i=0;
		j=0;
		count1=0;
		while(j<n){
			if(a[i]<b[j]){
				i++;
				j++;
				count1++;
			}
			else{
				j++;
			}
		}
		a.clear();
		b.clear();
		count1=n-count1;
		myfile<<"Case #"<<number<<": "<<count<<" "<<count1<<endl;
		number++;
	}
	return 0;
}
