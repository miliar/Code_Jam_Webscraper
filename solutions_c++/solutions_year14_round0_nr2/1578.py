#include<iostream>
#include<fstream>
#include <iomanip>
#include<stdlib.h>
#define cin fcin
#define cout fout
using namespace std;
ifstream fcin("date.in.txt");
ofstream fout("date.out.txt");
int main(){
	int T;
	cin>>T;
    //setprecision(7);
    FILE*p=fopen("date.out.txt","w");
	for(int i=1;i<=T;i++){
		double c,f,x,sum,now;
		sum=0;now=0;
		double k=2;
		cin>>c>>f>>x;
		while(true){
			double a=c/k;
			sum+=a;
			now+=c;
			if((x-now)/k>(x-now+c)/(k+f)){
				now-=c;
				k+=f;
			}
			else{sum=sum+(x-now)/k;
			break;
			}
		}
		
		fprintf(p,"Case #%d: %.7lf\n",i,sum);
		
	}
	return 0;
}
			