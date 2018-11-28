#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <numeric> 
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
using namespace std;
int main(){
	int t,k;
	double c,f,x,time,total,rate;
	freopen("B-large.in", "rt", stdin);
  	freopen("outputB-large-attempt0.txt", "wt", stdout);
	cin>>t;
	//cout.precision(8);
	for(k=0;k<t;k++){
		cin>>c>>f>>x;
		rate=2,total=0;
		while(1){
			//time 2 reach c
			if((x/rate)>(c/rate)+(x/(rate+f)))
			{
			
			total=c/rate+total;
			rate=rate+f;
			}
			else
			{
				total=total+(x/(rate));
				break;
			}
			
		}
	
	
	//cout<<"Case #"<<(k+1)<<": "<<total<<endl;
	printf("Case #%i: %0.7f\n",(k+1),total);
	
	}
	return 0;
}
	
