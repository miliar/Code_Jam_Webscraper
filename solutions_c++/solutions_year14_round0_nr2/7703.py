#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int t=0,e=0;
double c=0,f=0,x=0,this_step=0,next_step=0,sum=0,rate=2,k=0;
int main(){

ifstream fin;
fin.open("input.in");
ofstream fout;
fout.open("Output");
setprecision(9);
fin>>t;
while(t--){
	fin>>c>>f>>x;
	while(true){
		this_step+=c/rate;
		next_step+=x/rate;
		if((x/rate)<((c/rate)+x/(rate+f))){break;}
		rate+=f;
		next_step=this_step;
	}
	fout<<setprecision(9)<<"Case #"<<++e<<": "<<next_step<<endl;
	sum=this_step=0;
	next_step=0;
	rate=2;
}
}