
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	int cases;
	fin >> cases ;
	//fout<<3<<endl;
	int tests[1000];
	int flag=0;
	int x;
	//fout << a+b << endl;
	int arr[]= {0,1,2,3,4,5,6,7,8,9};

	for(int i=0; i<cases; i++) {
		for(int t=0;t<10;t++){
			arr[t]=t;
		}
		fin>>tests[i];
		int c=0;
		if(tests[i]!=0) {
			for(int j=1;; j++) {
				c=c+tests[i];
				//fout<<"c="<<c<<endl;
				int k=c;
				while(k!=0) {
					int m=k%10;
					for(int j=0; j<10; j++) {
					//	fout<<"j  arr j and m"<<j<<arr[j]<<m<<endl;
						if(arr[j]==m) {
							arr[j]=-1;
						}
					}
					k=k/10;
				}
				for(x=0; x<10; x++) {
					//fout<<"arr x ="<<arr[x]<<endl;
					if(arr[x]!=-1) {
						break;
					}
				}
				if(x==10) {
					fout<<"Case #"<<i+1<<":"<<" "<<c<<endl;
					break;
				}
			}
		} 
		else
			fout<<"Case #"<<1<<":"<<" INSOMNIA"<<endl;
	}
}





