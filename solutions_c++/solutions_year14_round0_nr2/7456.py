#include <iomanip>
#include <fstream>
using namespace std;
ifstream cin("in.txt");
ofstream cout("out.txt");
void main(){
	int T,t0=0;
	double C,F,X,Y,speed;
	cin >> T;
	while(t0++<T){
		Y=0;
		speed=2;
		cin >> C >> F >> X;
		while(true){
			if(((X-C)/speed)<(X/(speed+F)))
				break;
			Y+=C/speed;
			speed+=F;
		}
		Y+=X/speed;
		cout << "Case #" << t0 << ": " << fixed << setprecision(7) << Y << endl;
	}
}
