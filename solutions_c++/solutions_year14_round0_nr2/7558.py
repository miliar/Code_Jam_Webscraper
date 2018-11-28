#include <iostream>
using namespace std;

int main() {
	// your code goes here
	 freopen("B-large.in", "r", stdin);
   freopen("jam2_1.txt", "w", stdout);
	int test;
	cin>>test;
	for(int k=1;k<=test;k++)
	{
	cout<<"Case #"<<k<<":"<<" ";
	long double c,f,k,p;
	cin>>c>>f>>k;
	p=(double)(2);
	double time1=0,time2=0,t=0;
	time1= c/p;
	time2 = k/p;
	 //t=time1;
	 //cout<<"time1 - "<<time1<<"  time 2 = "<<time2<<endl;
	 
	while((time1+k/(p+f))<time2)
	{
	//cout<<p<<endl;
	t+=time1;
	 p+=f; 
	 time1 = c/p;
	 
	 //cout<<t<<endl;
	 time2 = k/p;
	}
	t+= (k/p);
	printf("%.7lf\n",t);
	}
	return 0;
}