#include <iostream>
#include <fstream>
using namespace std;
int a[4],b[4],t=0;
int tmp,k=0,count=0,num=0;
int r,e=0;
int main(){
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("Output");
	fin>>t;
	while(t--){
	fin>>r;
	for(int i=0;i<16;i++){
		fin>>tmp;
		if((i>(r*4)-5)&&i<r*4){
			a[k++]=tmp;
		}
	}
	k=0;
	fin>>r;
	for(int i=0;i<16;i++){
		fin>>tmp;
		if((i>(r*4)-5)&&i<r*4){
			b[k++]=tmp;
		}
	}
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(a[i]==b[j]){
				count++;
				if(count==1){
					num=a[i];
				}
			}
		}
	}
	fout<<"Case #"<<++e<<": ";
	if(count==1)
		fout<<num<<endl;
	else if (count>1)
		fout<<"Bad magician!\n";
	else 
		fout<<"Volunteer cheated!\n";
	count=0;
	k=0;
	}
}