#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main(){

	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);

	int test;
	cin>>test;
	double C,F,X,min_total_time,needTimetoByeFactory,currentCookie;
	int NumberOfLoop;
	for(int I=0;I<test;I++){
		min_total_time = 0.0;
		needTimetoByeFactory = 0.0;
		currentCookie = 2.0;

		cin>>C>>F>>X;

		min_total_time = X / currentCookie;
		needTimetoByeFactory = C / currentCookie;

		NumberOfLoop = (ceil)( X/C ) - 1;
		while(NumberOfLoop>0)
		{
			currentCookie += F;
			//cout<<currentCookie<<" ";
			min_total_time = min(min_total_time, (needTimetoByeFactory + (X / currentCookie)));
			//cout<<min_total_time<<" ";
			needTimetoByeFactory += (C / currentCookie);
			//cout<<needTimetoByeFactory<<endl;
		NumberOfLoop--;
		}

		printf("Case #%d: %.7lf\n",I+1,min_total_time);
		//cout<<"out: "<<min_total_time<<endl;


	}



return 0;
}
