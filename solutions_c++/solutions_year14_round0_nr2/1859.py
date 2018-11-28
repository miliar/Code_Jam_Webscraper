#include<iostream.h>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
int main(){
	ifstream in("B-large.in");
	ofstream out("output.txt");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	int noc;
	in>>noc;
	for(int i=0;i<noc;i++){
	double fp,pow,tot=0.000000,inc=2.0,time=0.0,coc=0;
		in>>fp;
		in>>pow;
		in>>tot;
		if(fp>tot){
			out<<"Case #"<<i+1<<": "<<(tot*1.0)/(inc)<<endl;
		}else{
			time+=(fp*1.0)/inc;
			while(1){
				coc=fp;
				double temp=tot-coc;
				double w1,w2;
				w1=temp/inc;
				w2=tot/(inc+pow);
				if(w1<=w2){
					time+=(temp*1.0)/inc;
					out<<"Case #"<<i+1<<": "<<time<<endl;
					break;
				}else{
					inc+=pow;
					coc=0;
					time+=(fp/inc);
				}
			}//while
		}//end of else
	}
}