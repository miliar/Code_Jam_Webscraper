#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("A-large.in");
	ofstream fout("gcj1.out");
	int testcases;
	fin>>testcases;
	int num;
	int *arr;
	arr = new int[testcases];
	for(int i=0;i<testcases;i++){
		fin>>arr[i];
	}
	int check[10];
	
	for(int i=0;i<testcases;i++){
		int nooftimes=1;
		int val = arr[i];
		long int dupe=0;
		int count=0;
		for(int i=0;i<10;i++){
		check[i]=-1;
		}
		int result[testcases];
			
		//cout<<val<<"  ";
		while(count<10){
			//cout<<nooftimes<<"  "<<val<<"  "<<dupe<<"  ";
			dupe = nooftimes*val;
			long int duplicate = dupe;
			//cout<<duplicate<<"  ";
			while(duplicate>0){
				int d = duplicate%10;
				if(check[d]==-1){
					check[d]=1;
					count++;
					//cout<<d<<" "<<duplicate<<" ";
				}
				duplicate=duplicate/10;
			}
			nooftimes++;
			if(nooftimes>1000 || dupe>429496721){
				result[i]=-1;
				break;
			}
		}
		if(count==10){
			result[i]=dupe;
		}
		fout<<"Case #"<<i+1<<": ";
		if(result[i]==-1)fout<<"INSOMNIA";
		else
		fout<<dupe;
		fout<<"\n";	
	}
	
	
	
}
