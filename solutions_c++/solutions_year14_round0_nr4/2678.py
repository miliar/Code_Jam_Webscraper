#include<iostream>
#include <algorithm>
#include <vector>
#include<fstream>
using namespace std;

vector<double> vect;
vector<double> vect1;

int func(int n){
	int i=0,j=0,count=0;
	while(i<n){
		if(vect[i]>vect1[j]){
			i++;
			j++;
			count++;
		}
		else{
			i++;
		}
	}
	return count;
}

int func1(int n){
	int i=0,j=0,count1=0;
	while(j<n){
		if(vect[i]<vect1[j]){
			i++;
			j++;
			count1++;
		}
		else{
			j++;
		}
	}
	return count1;
}

int main(){
	int i,j,t,n,k,count,count1;
	int number=1;
	ofstream myfile;
	myfile.open ("out.txt");
	double p;
	cin>>t;
	while(t--){
		cin>>n;
		for(i=0;i<n;i++){
			cin>>p;
			vect.push_back(p);
		}
		for(i=0;i<n;i++){
			cin>>p;
			vect1.push_back(p);
		}
		sort(vect.begin(), vect.end());
		sort(vect1.begin(), vect1.end());
		count=func(n);
	//	cout<<"here"<<endl;
		count1=func1(n);	
		vect.clear();
		vect1.clear();
		count1=n-count1;
		myfile<<"Case #"<<number<<": "<<count<<" "<<count1<<endl;
		number++;
	}
	return 0;
}
