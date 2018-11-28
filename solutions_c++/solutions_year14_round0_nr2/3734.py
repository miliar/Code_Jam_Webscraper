#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
	ifstream inp("Cinput.txt");
	ofstream out("Coutput.txt");
	
	int t,cno=0;
	double c,f,x,rate,ttime,tmp1,tmp2;

	inp>>t;

	for(int i=0;i<t;i++){
		rate = 2;
		ttime=0;
		cno++;

		inp>>c;
		inp>>f;
		inp>>x;

		while(1){
			tmp1=c/rate + x/(rate+f);
			tmp2=x/rate;
			if(tmp2<tmp1){
				ttime+=tmp2;
				break;
			}
			else {
				ttime+=c/rate;
				rate+=f;
			}

		}
		out<<"Case #"<<cno<<": "<<fixed << setprecision(7)<<ttime<<"\n";
	}


}