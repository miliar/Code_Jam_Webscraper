#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void solve(double C,double F, double X, double& ans){
	//no need to get Farm
	if(2*C+F*C>= X*F){
		ans = X/2;
		return;
	}
	ans = X/2;
	int farms = 0;
	double time =0;
	while(true){
		time+=(C/(2+farms*F));
		++farms;
		double tempAns = time + X/(2+farms*F);
		if(tempAns<ans){
			ans=tempAns;
		}
		else
			break;
	}
}
void showAns(int round, double ans, ofstream& file){
	file<<"Case #"<<round<<": "<<fixed<<setprecision(7)<<ans<<endl;
	return;
}
void main(){
	ifstream file("B-large.in");
	if(!file)
		return;
	int T =0;
	double C,F,X,ans;
	file>>T;
	ofstream outfile("output");
	for(int idx = 1; idx<=T; ++idx){
		file>>C>>F>>X;
		solve(C,F,X,ans);
		showAns(idx,ans,outfile);	
	}
	outfile.close();
	file.close();

}