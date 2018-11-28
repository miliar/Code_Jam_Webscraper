#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip> 
using namespace std;

int main() {
	int N=0; cin>>N;
	cout<<setprecision(7)<<fixed;
	for(int o=1;o<=N;++o){
		double C=0,F=0,X=0;
		cin>>C>>F>>X;
		double min=X/2.0; 
		for(int i=1;;++i){
			double p=2,m=0;
			int k=0;
			while(k!=i){
				m+=C/p,p+=F,++k;
				if(m>=min){ m=-1; break;}
			}
			if(m==-1)break;
			m+=X/p;
			if(m<min)min=m;
		}
		cout<<"Case #"<<o<<": "<<min<<endl;
	}
	return 0;
}