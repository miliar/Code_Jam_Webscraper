#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,k=1;
	ofstream fout;
	fout.open("baba.txt");
	ifstream fin;
	fin.open("A-small-attempt4.in");
	fin>>t;
	while(k<=t){
		int n;
		fin>>n;
		char a[n+1];
		fin>>a;
		int need=0,stand=0;
		for(int i=0;i<=n;i++){
			if((a[i]-48)==0){
				continue;
			}
			if(stand>=i){
				
				stand+=(a[i]-48);
			}
			else{
				need+=(i-stand);
				stand=stand+(a[i]-48)+need;
			}
		}
		fout<<"Case #"<<k<<": "<<need<<endl;
		k++;
	}
	fin.close();
	fout.close();
}
