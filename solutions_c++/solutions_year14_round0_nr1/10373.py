#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;

int comp(int *arr1,int* arr2){
	int counter=0;
	int ans;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
		
			if(arr1[i]==arr2[j]){
				
				counter++;
				ans=arr2[j];
			}

		}		
	}
	if(counter==0){
		return -1;
	}
	if(counter>1){
		return -2;
	}
	else 
		return ans;
	
}
int main(){

	fstream fin;
	fstream fout;
	fout.open("out.txt",ios::out);
	fin.open("input.txt");
	
	int test_cases;
	string t;
	getline(fin,t);
	stringstream s(t);
	s>>test_cases;

	int ans1=0,ans2=0;
	int arr1[4],arr2[4];
	string xx;
	for(int i=0;i<test_cases;i++){
			
		getline(fin,t);
		stringstream ss(t);
		ss>>ans1;
		
		for(int x=0;x<4;x++){
			if(x==ans1-1){
				getline(fin,t);
				continue;
			}
			getline(fin,xx);
		}
		stringstream sx(t);
		for(int j=0;j<4;j++){
			
			sx>>arr1[j];
		}
		
		getline(fin,t);
		stringstream sy(t);
		sy>>ans2;
		
		for(int y=0;y<4;y++){
			if(y==ans2-1){
				getline(fin,t);
				continue;
			}
			getline(fin,xx);
		
		}
		stringstream sz(t);
		for(int j=0;j<4;j++){
			
			sz>>arr2[j];
		}
	
		
		int ll=comp(arr1,arr2);
		if(ll==(-1)){
			
			fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!\n";
		}
		else if(ll==(-2)){

			fout<<"Case #"<<i+1<<": "<<"Bad magician!\n";

		}
		else{
			fout<<"Case #"<<i+1<<": "<<ll<<"\n";
			
		}
	}
	
	return 0;
}