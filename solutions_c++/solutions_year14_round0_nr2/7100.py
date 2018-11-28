#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	cout << fixed << setprecision(9);
	int n;
	cin >> n; 
	for(int y=0;y<n;++y) {
		double c,f,x,time=0,step=2,timex=0,timex1=0,alltime=0;
		cin >> c;
		cin >> f;
		cin >> x;
		for(int i=0;;++i) {
			timex=x/step;
			time=c/step;
			timex1=x/(step+f);
			if(timex < time + timex1) {
				alltime += timex;
				break;
			}
			else {
				alltime += time;
				step += f;
			}
		}
		if (y!=n-1)
			cout << "Case #"<<y+1<<": "<<alltime<<endl;
		else 
			cout << "Case #"<<y+1<<": "<<alltime;
	}
}