#include<iostream>
#include<iomanip> 
using namespace std;
double c,f,x;
double calc(int n){
	double cps=2,time=0;
	for (int i=0;i<n;i++){
		time+=c/cps;
		cps+=f;
	}
	time+=x/cps;
	return time;
}
int main(){
	int t;
	cin >> t;
	for (int ti=0;ti<t;ti++){
		cin >> c >> f >> x;
		cout << "Case #" << ti+1 << ": "; 
		double now,prev=calc(0);
		for (int i=1;;i++){
			now=calc(i); 
			if (now>prev){ 
				cout << fixed << setprecision(7) << prev << endl;
				break;
			}
			prev=now;
		}
	}
	return 0;
}
