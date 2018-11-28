#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<fstream>
using namespace std;

double C,F,X, N;
double gain, sum, curr_t;
int cookie = 1;

int main(){
FILE *out;
out = fopen("drugi.txt", "wt");
cin>>N;

while( N--){
	cin>>C>>F>>X;
	
	gain = 2;
	sum = 0;
	curr_t= 0;
	
	while( sum < X) {
		double t1 = ( X-sum ) / gain;
		double t2 = ( C-sum ) / gain;	
		
		sum += gain*min(t1,t2);
		curr_t += min ( t1, t2);
		
		if( sum >= X) break;
		
		double sum2 = sum+ (C/F) * gain;
		if( sum2 < X) {
			sum -= C;
			gain+=F;	
		}
		else {
			curr_t += ( X-sum ) / gain;
			break;	
		}
	
	}
	
	fprintf( out, "Case #%d: %.07f\n", cookie, curr_t);
	cookie++;
}
return 0;
}

