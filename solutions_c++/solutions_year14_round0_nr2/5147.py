#include<iostream>
#include <math.h>
using namespace std;
 
int main(){
int t;
freopen("inp.txt","r",stdin);
freopen("outp.txt","w",stdout);
cin >> t;
int idx = 1;
double c,f,x;
while(t--){
	cin >> c >> f >> x;
	double time=0.0,rate=2.0;
	while(x/rate > (c/rate)+(x/(rate+f))){
	time+=(c/rate);
	rate+=f;
	}
time+=(x/rate);
printf("Case #%d: %.7f\n",idx,time);
//cout << "Case #"<<i+1<<":"<< time_taken << endl;
idx++;
}
return 0;
} 
