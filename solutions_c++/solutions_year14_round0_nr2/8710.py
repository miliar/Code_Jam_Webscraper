#include<iostream>
#include<algorithm>
#include<iomanip>

using namespace std;

#define INF 10000000
#define EPS 1e-8

int main(){
	int i,j,k;
	int T;
	double C,F,X,R;
	
	cin >> T;
	for(k = 0; k < T; k++){
		cout<< "Case #" << k+1<<": ";
		cin >> C >> F >> X;
		R = 2.0;
		
		double curtime = INF, newtime = X/R;
		//cout<< ">" <<newtime <<"\n";
		double prevtime = 0;
		while( curtime  > newtime){
			//cout<< ">" <<curtime <<"\n";
			curtime =newtime;
			double a = C / R;
			prevtime += a;
			R += F;	
			newtime = prevtime + X / R;
		}
		
		/*for(i=0;i<10;i++){
			cout<< ">" <<curtime <<"\n";
			curtime =newtime;
			double a = C / R;
			prevtime += a;
			R += F;	
			newtime = prevtime + X / R;
		}*/
		cout << fixed << setprecision(7) << curtime << "\n";
	}
	return 0;
}