#include <stdio.h>
//#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(){
	ifstream in ("B-large.in");
	ofstream out ("output.txt");
	int caso,coso;
	in>>caso;
	for(coso=0;coso<caso;coso++){
		double c,f,x,bs,tt=999999999999999999,temp;
		int i=0,j;
		bool culo = true;
		in>>c>>f>>x;
		while (culo==true){
			temp = 0;
			bs=2.0000000;
			for(j=0;j<i;j++){
				temp= temp + c/bs;
				bs = bs+f;
				}
			temp = temp + x/bs;
			if(temp<tt) tt=temp;
			else culo=false;
			i++;
			}
			out<<"case #"<<setprecision(7)<<coso+1<<": "<<tt<<endl;
		}
}
