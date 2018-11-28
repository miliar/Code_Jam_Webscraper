// Q2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

double clicker(double c, double f, double x){
	int flag=0;
	double ans=0, tmp=0, speed=2, passed=c/speed, cur;
	cur = x/speed;
	speed += f;
	while(flag==0){
		tmp = passed + x/speed;
		if(cur<=tmp) {
			ans=cur;
			flag=1;
		}
		else{
			passed += c/speed;
			speed +=f;
			cur = tmp;
		}
	}
	return ans;
}

int main()
{
    freopen("D://Practice//B-large.in", "r", stdin);
    freopen("D://Practice//B-large.out", "w", stdout);

	int numCase;
	cin >> numCase;
	cout<<setiosflags(ios::fixed);
	cout<<setprecision(7);
	for(int i=0; i<numCase; i++) {
		double c, f, x;
		cin>>c>>f>>x;
		cout << "Case #" << (i+1) << ": " << clicker(c, f, x) << endl;
	}
	return 0;
}