// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>

#define FOR(i,n) for(int i=0;i<n;i++)

using namespace std;

int P[1001];

// Main Program Starts
int main() {

	
	int T=0;

	cin >> T;

	int fun(int);

	FOR(t,T){
		int D;
		
		cin >> D;
		
		FOR(i,1001) P[i]=0;

		int a=0;

		//cout << endl << D;
		FOR(i,D) {
			cin >> a;
			P[a]++;
			//cout << " " << a;
		}
		
		int val=0,time=0;
	
		int max=0;

		FOR(i,1001)
			if(P[i]!=0) max=i;

		//cout << "Max:" << max << endl;
		
		cout << "Case #" << t+1 <<": " << fun(max) << endl;
	}
		
	return 0;
}



	int fun(int i) {

		if(i<=3 && P[i]!=0)
			return i;

		if(P[i]==0)
			return (fun(i-1));

		if(i/2-P[i]<=0)
			return i;

		int cost2=0,cost3=0;

		//if(i/3-P[i]>1 && (i==9 || i==81 || i==243 || i==729)){
		P[i/3]+=P[i];
		P[i-i/3]+=P[i];
		cost3=fun(i-1);
		//cout << "Cost for " << i-1 << ":" << cost << endl;
		P[i/3]-=P[i];
		P[i-i/3]-=P[i];

		P[(i+1)/2]+=P[i];
		P[i-(i+1)/2]+=P[i];
		cost2=fun(i-1);
		P[(i+1)/2]-=P[i];
		P[i-(i+1)/2]-=P[i];
		
		if(cost2<cost3)
			if(cost2+P[i]<i)
				return cost2+P[i];
			else
				return i;
			
		else
			if(cost3+P[i]<i)
				return cost3+P[i];
	
			else
				return i;

	}
