#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream ifile;ofstream ofile;ifile.open("lottery.in");ofile.open("lottery.txt");
	int cases,n1,n2,n3,count,temp;
	ifile>>cases;
	for(int a=0;a<cases;a++){
		count=0;
		ifile>>n1>>n2>>n3;
		for(int i=0;i<n1;i++){
			for(int j=0;j<n2;j++){
				temp=i&j;
				if(temp<n3){
					count=count+1;}
			}
		}
		ofile<<"Case #"<<a+1<<": "<<count<<endl;
	}
	return 0;
}