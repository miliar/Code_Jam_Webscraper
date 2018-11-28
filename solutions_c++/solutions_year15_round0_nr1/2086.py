#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>


using namespace std;

int main(){
	ifstream in("in");
	int casenum=0;
	in>>casenum;
	int sm=0;
	char c;
	
	int nfriend=0;
	for (int i=0;i<casenum;i++){
		nfriend=0;
		int sofar=0;
		in>>sm;
		for(int j=0;j<=sm;j++){
			in>>c;
			int l=(int)c-'0';
			
			if(j>sofar){
				//cout<<j<<" "<<sofar<<endl;
				int extra=(j-sofar);
				sofar+=extra;
				nfriend+=extra;
			}
			sofar+=l;
		}
		cout<<"Case #"<<i+1<<": "<<nfriend<<endl;
			
	}
	
	return 0;
	
}
