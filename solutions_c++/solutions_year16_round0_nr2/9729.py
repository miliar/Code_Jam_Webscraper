
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ofstream fout ("B-large.out");
	ifstream fin ("B-large.in");
	int cases;
	fin >> cases ;
	//fout<<3<<endl;
	string stack[105];
	//fout << a+b << endl;
	string temp;
	for(int i=0; i<cases; i++) {
		temp="";
		fin>>stack[i];
		temp=stack[i];
		int count=1;
	//	fout<<endl<<"temp.size()= "<<temp.size()<<endl;
		for(int k=0; k<temp.size()-1; k++) {
			if(temp[k]!=temp[k+1]) {
				count++;
			}
		}
	//	fout<<endl<<"count1= "<<count<<endl;

		if(temp[temp.size()-1]=='+') {
			count--;
		}
	//	fout<<endl<<"count2= "<<count<<endl;
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

/*		}
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

*/



