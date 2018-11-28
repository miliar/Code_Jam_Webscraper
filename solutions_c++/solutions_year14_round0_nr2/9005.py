#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
double c , f , x;
bool fun(double mid){
	double acc = 0.0 ,rate =2.0;
	double sec = mid;
	while(sec>=0){
		double temp1 = (x-acc)/rate; // with out farm
		if(temp1>sec){
			double  temp2;
			if(acc<c)
			{
				temp2 = (c-acc)/rate;
				acc=0;
			}else
			{
				temp2 = (c)/rate;
				acc-=c;
			}
			
			if(temp2<sec){
				rate+=f;
				sec-=(temp2);
				acc = 0;
			}else return false;
		}else{
			return true;
		}
	}
	return false;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t , k= 1;
	cin >> t;
	while(t--){
		cin >> c >> f >> x;
		double low = 0.0 , high = x / 2.0;
		double mid ;
		while(fabs(low-high)>=0.00000001){
			mid = (low+(high-low)/2);
			if(fun(mid)){
				high = mid;
			}else{
				low = mid; 
			}
		}
		printf("Case #%d: %0.7lf\n",k,mid);
		k++;
	}
	return 0;
}
