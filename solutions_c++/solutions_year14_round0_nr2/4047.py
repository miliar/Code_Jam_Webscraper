#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
	 double C,F,X;
	 cin>>C>>F>>X;
	 double delay,rate;
	 double olddelay,oldrate;
	 double temp;
	 double timetaken;// random max value
	 olddelay=0;
	 oldrate = 2.0000000;
	 timetaken = olddelay + X / oldrate;
	 for(int k=1;k<200000;k++) {
	  delay = olddelay + C / oldrate;
	  rate = oldrate + F;
	  temp = delay + X / rate;
	  if(temp < timetaken) {
	   timetaken = temp;
	   olddelay = delay;
	   oldrate = rate;
	  } else {
	   break;
	  }
	 }
	 cout<<"Case #"<<i<<": ";
	 printf("%.7lf\n",timetaken);
	}
	
	return 0;
}