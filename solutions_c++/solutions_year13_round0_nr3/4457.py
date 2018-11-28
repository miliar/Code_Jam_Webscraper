#include <iostream>
#include <fstream>
#include <cmath>	
using namespace std;

ifstream fin;
ofstream fout;
int t,k;
int num[4]={0};
int a,b;

bool pa(int a){
	int i=0;
	while(a!=0){
		num[i++]=a%10;
		a=a/10;
	}
	if(i==4) return (num[3]==num[0]&&num[2]==num[1]);
	if(i==3) return (num[2]==num[0]);
	if(i==2) return (num[1]==num[0]);
	if(i==1) return true;

};
int main(){
	fin.open("C-small-attempt0.in");
	fout.open("C-small-attempt0.out");

	fin>>t;
	for(k=0;k<t;k++){
		fin>>a>>b;
		int count=0;
		int root;
		for(int i=a;i<=b;i++){
			root=(int)sqrt(i);
			if(pa(i)&&pa(root)&&i==root*root) count++;
		}
		fout<<"Case #"<<k+1<<": "<<count<<endl;
	}	


	fin.close();
	fout.close();
	return 0;
}