//Standing ovation google code jam

#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("file2.out");
	int t;
	fin>>t;
	for(int x=0;x<t;x++){
		int Smax;
		fin>>Smax;
		int arr[Smax+1];
		string str;
		fin>>str;
		for(int i=0;i<=Smax;i++)
			arr[i]=str[i]-'0';
		
		int count=arr[0];
		int res=0;
		for(int i=1;i<=Smax;i++){
			if(count<i){
				res+=i-count;
				count+=i-count;
			}
			count+=arr[i];
		}
		fout<<"Case #"<<x+1<<": "<<res<<endl;
	}
	return 0;
}
