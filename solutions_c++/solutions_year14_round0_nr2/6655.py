#include <fstream>
#include <iomanip>

using namespace std;

bool shouldBuy(double producing, double cost,double adv,double win,double cookie){
	if((win-cookie)/(producing)>(cost/producing)+win/(producing+adv))
		return true;
	else return false;
}


int main(){
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("output.txt");
	int times;
	fin>>times;
	for(int caseNo=1;caseNo<=times;caseNo++){
		double cookies=0;
		double sec=0;
		double producingAt=2;
		double farmCost,farmProduces,toWin;
		fin>>farmCost>>farmProduces>>toWin;
		while(cookies<toWin){
			if(shouldBuy(producingAt,farmCost,farmProduces,toWin,cookies)){
				sec+=(farmCost/producingAt);
				producingAt+=farmProduces;
			}
			else {
				sec+=((toWin-cookies)/producingAt);
				cookies+=(toWin-cookies);
			}
		}
		fout << setprecision(16);
		fout<<"Case #"<<caseNo<<": "<<sec<<'\n';
	}
	return 0;
}