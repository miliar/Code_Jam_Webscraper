#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ifstream fin("A-large.in");
	ofstream fout("gcj1.out");
	int testcases;
	fin>>testcases;
	int num;
	string arr[testcases];
	
	//arr = new int[testcases];
	for(int i=0;i<testcases;i++){
		fin>>arr[i];
	}
	for(int i=0;i<testcases;i++){
		num=0;
		
		while(1){
			int j=0;
			while(arr[i][j]!='\0' && arr[i][j]=='+')j++;
			if(arr[i][j]=='\0')break;
			j=0;
			int k=0;
			if(arr[i][0]=='+'){
				while(arr[i][j]!='-' && arr[i][j]!='\0')j++;
				//if(i==2)cout<<j;
				//cout<<j;
			}else{
				while(arr[i][j]!='+' && arr[i][j]!='\0')j++;
			}
			if(arr[i][0]=='-'&&arr[i][j]=='\0'){num++;break;}
			
			if(arr[i][0]=='+'){
				for(int m=0;m<j;m++)arr[i][m]='-';
				num++;
				
			}
			else if(arr[i][0]=='-'){
				for(int m=0;m<j;m++)arr[i][m]='+';
				num++;
				//cout<<" a ";
			}
			
			}
			fout<<"Case #"<<i+1<<": "<<num<<"\n";
		}
	}
	

