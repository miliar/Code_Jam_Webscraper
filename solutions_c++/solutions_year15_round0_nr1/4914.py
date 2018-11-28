#include<iostream>
#include<fstream>
using namespace std;
main(){
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int tt;
	fin>>tt;
	int maxShy;
	char c;
	for(int no=1;no<=tt;no++){
		int count=0;
		int upAudience=0;
		int a;
		fin>>maxShy;
		for(int i=0;i<=maxShy;i++){
			fin>>c;
			a=c-'0';
			upAudience+=a;
		//	cout<<"done";
			while(upAudience<=i){
				count++;
			//	cout<<"vikash "<<endl;
				upAudience++;
			}
		}
		fout<<"Case #"<<no<<": "<<count<<endl;
		
	}
}
