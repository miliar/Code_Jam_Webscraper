#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int tc;
	double C,F,X,time;
	cin>>tc;
	double cookierate = 2.0;
	int flag = 0;
	double t1,t2;
	for(int i=0;i<tc;i++)
	{
		cin>>C>>F>>X;
		time = 0.0;
		flag = 0;
		cookierate = 2.0;
		while(flag != 1)
		{
			t1 = X/cookierate;
			t2 = C/cookierate + X/(cookierate+F);
			//cout<<cookierate<<" "<<C<<" "<<X<<endl;
			if(t1<t2)
			{
				flag = 1;
			} else {
				time = time + C/cookierate;
				cookierate = cookierate+F;
				
			}
		}
		time = time + X/cookierate;
		if(i!=0)
			cout<<endl;
		cout<<"Case #"<<(i+1)<<": ";
		printf("%0.7f",time);
	}
	return 0;
}


