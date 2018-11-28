#include<iostream>
using namespace std;

double c,f,x;
const int maxBuy = 1000*1000+1; // at most we but factory x times

//double EPS = 1e-10;
bool check(int k){ // rate is 2 at first
	double rate = k*f + 2.0;		
	if(x*f-c*rate-c*f > 0)
		return true;
	else
		return false;
}
// Finds the first false
int bs(int i,int j){
	if(i==j)
		return i;
	bool cur = check((i+j)/2);
	if(cur)
		return bs((i+j)/2+1,j);
	else
		return bs(i,(i+j)/2);
}


int main(){
	int T=0;
	cin >> T;
	for(int t=0;t<T;t++){
		cin >> c >> f >> x;
		double ans = 0;
		int k = bs(0,maxBuy);

	//	cout << k << endl;
		for(int i=0;i<k;i++)
			ans += c/(2.0+i*f);
		ans += x/(2.0+k*f);

		cout.precision(15);
		cout << "Case #" << t+1 << ": ";
		cout << ans << endl;
	}	


	return 0;
}
