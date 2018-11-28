#include<vector>
#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;

vector<double> times;
const double er = 0.000000001;
double F, C, X;

//up is as given in eq,
//array times is one index
//lower than in eq
double sumTimes(int up){
	double v = 0;
	for(int k = 0; k < up; ++k){
		v+=times[k];  	
	}
	return v;
}

void printtimes(){
	for(int i = 0; i < 5; ++i){
		cout << times[i] << "   ";
	}
	cout << endl;
}

void setTimes(int i){
	double v = F* sumTimes(i-1);
	v = (v+i*C)/(2.+(i-1)*F);
	times[i-1] = v;
}

double solve(int i){
	double v = F*sumTimes(i);
	v = (v+X+C*i)/(2.+i*F);
	return v;
}

int main(){
	int T; cin >> T;
	double ans, next;
	for(int t = 1; t <= T; ++t){
 		cin >> C >> F >> X;
		next = 10000;
		times = vector<double>(50000);
		for(int i = 0; i+1 < times.size(); ++i){
			ans = solve(i);
			if(ans > next) break;
			next = ans;
      setTimes(i+1);
		}
		printf("Case #%i: %.7f\n", t, next);
//		cout << "Case #" << t << ": ";
//		cout << next << endl;
	}


	return 0;
}


