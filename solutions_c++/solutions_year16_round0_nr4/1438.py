#include<fstream>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main() {
	int n, j, x;
	long long int mult, t, vec[11], div[11];
	bool flag;
	ifstream is;
	is.open("inC.txt");
	ofstream os;
	os.open("outC.txt");
	is>>x;
	for(int i=0; i<x; i++) {
		os<<"Case #"<<i+1<<": "<<endl;
		is>>n>>j;
		t=1;
		for(int k=0;k<n;k++) t*=2;
		t++;
		for(int k=0; k<j; t+=2, k++){
			flag = true;
			for (int a=0; a<11 ;a++){
				vec[a] = 0;
				div[a] = -1;
			}
			for(int u = t, aux = 0; u>0; u/=2, aux++){
				for(int a = 2; a<11; a++){
					int cnt;
					for(mult=1, cnt=0;cnt<=aux; cnt++) mult*=a;
						vec[a] += u%2*mult;
				}
			}
			
			for(int a = 2; a<11; a++) cout<<vec[a]<<endl;
			cout<<endl;
			
			for (int a=2; a<11 && flag; a++) {
				for(int s=2; s*s < vec[a] && div[a] == -1; s++ ) {
					if(vec[a]%s ==0) div[a] = s;
				}
				if(div[a] == -1) flag = false;
			}
			if(flag){
				for(int u = k; u>0; u/=2){
					os<<u%2;
				}
				os<<" ";
				for(int a = 2; a< 10; a++) os<<div[a];
				os<<div[10]<<endl;	
			}
		}
	}
}



