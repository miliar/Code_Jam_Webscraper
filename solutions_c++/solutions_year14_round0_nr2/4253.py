#include <iostream>
#include <iomanip>
using namespace std;
double c,f,x;
int test;
float cal(double c, double f, double x){
	double speed,tempSum,tempTime,tempTime2;
	speed = 2;
	tempSum = 0;
	tempTime = 0;
	while (true) {
		if (tempSum < c){
			if (x <= c ) return tempTime + (x-tempSum)/speed;
			else {
				tempTime += (c-tempSum)/speed;
				tempSum = c;
			}
			//cout << tempTime << endl;
		} else {
			tempTime2 = (x+c-tempSum)/(speed+f);
			//cout <<"tempTime2 : "<< tempTime2 << endl;
			if ((x - tempSum)/speed > tempTime2){
				speed +=f;
				tempSum-=c;
			} else return tempTime + (x-tempSum)/speed;
			//cout << "tempTime : "<<tempTime << endl;
		}
	}
}
int main(){
    cin >> test;
    for (int t=1; t<= test; t++){
        cin >> c >> f >> x;
        cout << "Case #" << t << ": " ;
		cout <<fixed << setprecision(7) << cal(c,f,x);
		cout << endl;
    }
}
