#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<iomanip>
using namespace std;

int main(){
	int nc, caso;
	double c,f,x;
	
	cin>>nc;
	double t,s;
	for(caso=0; caso<nc; caso++){
		cin>>c>>f>>x;
		t=0;
		s=2;
		while(1){
			double op1 = x/s;
			double op2 = c/s + x/(s+f);
			
			if(op1<op2){
				t += op1;
				break;
			}
			else{
				t += c/s;
				s += f;
			}
		}
		cout<<"Case #"<<caso+1<<": "<< std::fixed <<std::setprecision(7)<<t<<endl;
	}
	return 0;
}
