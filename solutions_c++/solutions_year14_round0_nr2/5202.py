#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<algorithm>
#include<math.h>
#include <iomanip>
using namespace std;
int main(){
int t1,l=1;
cin>>t1;
while(t1--){
	double c,f,x,ans=0,p,q,r,s=2;
	cin>>c>>f>>x;
	int t=0;
	
	while(true){
	p=(x)/((f*t)+s);
	q=(c)/((f*t)+s);
	r=(x)/((f*(t+1))+s);
	r=r+q;

	if(r>=p){
		ans=ans+p;
		break;
	}
	else{
		ans=ans+q;
	}
	t++;
	}

//printf("Case #%d: %1.7f\n",l,ans);

cout<<"Case #"<<l<<": "<<fixed<<setprecision(7)<<ans<<"\n";
l++;
}

system("pause");
  return 0;
}
