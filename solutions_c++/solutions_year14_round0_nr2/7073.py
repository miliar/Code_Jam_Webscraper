#include <iostream>
#include <cmath>
using namespace std;


double getMin(double c,double f,double x,double rate){
	if(x<c) return x/rate;
	double ans1 = x/rate;
	double ans=0;
	while(x/rate > c/rate + x/(rate+f)){
		ans += c/rate;
		rate+=f;
	}
	ans += x/rate;
	//if(x/rate < c/rate+x/(rate+f)) return x/rate;
	//double ans2 = c/rate  + getMin(c,f,x,rate+f);
	
	//return min(ans1, ans2);
	return ans;
}

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	double c,f,x;
	cin >> t;
	for(int cn=1;cn<=t;cn++){
		cin >> c >> f >> x;
		cout << "Case #" << cn << ": ";
		double ans = getMin(c,f,x,2.0);
		printf("%.7f\n",ans);
	}
}