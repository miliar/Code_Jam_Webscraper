#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main(){
	int t,k,i,count;
	string str;
	ifstream fin;
	fin.open("A-large-attempt0.in");
	ofstream fout;
	fout.open("A-large.out");
	cin>>t;
	count=1;
	while(t--){
	cin>>str;
	k=0;
	vector<int> arr;
	vector<int> flag(str.length(),0);
	for(i=1;i<str.length();i++){
	if(str[i]>=str[k]){
	arr.push_back(i);
	k=i;	
	flag[i]=1;
	}	
	}	
		cout<<"Case #"<<count<<": ";
	for(i=arr.size()-1;i>=0;i--){
	cout<<str[arr[i]];	
	
	}
	
	for(i=0;i<str.length();i++){
	if(flag[i]==0){
	cout<<str[i];	
	}	
	
	}
	cout<<endl;
	
	count=count+1;
	}
	
	
	
	
	return 0;
}
