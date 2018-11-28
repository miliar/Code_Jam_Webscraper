#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>
#include <math.h>

using namespace std;

int main(){
	ifstream in("in");
	int casenum=0;
	int p[1000];
	in>>casenum;
	for(int c=0;c<casenum;c++){
		int d;
		in>>d;
		for(int i=0;i<d;i++){
			in>>p[i];
		}
		int mintime=1000;
		int bestm=1000;
		for(int m=1;m<=1000;m++){
			int cutnum=0;
			
			for(int i=0;i<d;i++){
				int l=ceil((double)p[i]/m)-1;
				if(l>0)
					cutnum+=l;
			}
			if(mintime>cutnum+m){
				mintime=cutnum+m;
				bestm=m;
			}
		}
		cout<<"Case #"<<c+1<<": "<<mintime<<endl;
		
	}
	
	return 0;
	
}
