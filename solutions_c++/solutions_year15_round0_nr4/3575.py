#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("D-small-attempt0.in");
	fout.open("baba.txt");
	int t,k=1;
	fin>>t;
	while(k<=t){
		int r,x,c;
		fin>>x>>r>>c;
		int flag=0;
		if((r*c)%x!=0){
			flag=0;
		}
		else{
			if(x==4){
			if((r==4||r==3)&&(c==4||c==3)){
				flag=1;
			}
		}
		else if(x==3){
			if((r==4||r==3||r==2)&&(c==4||c==3||c==2)){
				flag=1;
			}
		}
		else{
			flag=1;
		}
	}
		if(flag==0){
			fout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
		}
		else{
			fout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
		}
		k++;
	}
	fout.close();
	fin.close();
}
