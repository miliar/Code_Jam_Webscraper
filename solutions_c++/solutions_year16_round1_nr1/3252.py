#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("A-large.in");
	ofstream fout("gcj1.out");
	int testcases;
	fin>>testcases;
	char a[2000];
	char b[2000];
	for(int i=0;i<testcases;i++){
		fin>>a;
		int j=0;
		int k=0;
		b[k]=a[j];
		j++;k++;
		while(a[j]!='\0'){
			if(a[j]>=b[0]){
				char temp[2000];
				for(int y=0;y<k;y++){
					temp[y]=b[y];
				}
				b[0]=a[j];
				for(int y=0;y<k;y++){
					b[y+1]=temp[y];
				}
			}else{
				b[k]=a[j];
			}
			j++;k++;
		}
		b[k]='\0';
		fout<<"Case #"<<i+1<<": "<<b<<endl;
	}
}
