#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double rate=2.0,money=0,time=0;
		bool cond=true;
		if(x<=c)
		{
			cond=false;
			time=x/rate;
		}
		while(cond)
		{
			if(money==x){
				break;
			}
			else if(money<c){
				money=c;
				time+=	c/rate;
			}
			else if((x-money)/rate>(x-money+c)/(rate+f))
			{
				money=0;
				rate+=f;
			}
			else{
				time+=(x-money)/rate;
				money=x;
				break;
			}
			//cout<<money<<" "<<time<<" "<<rate<<endl;
		}
		cout<<"Case #"<<i<<": ";
		printf("%F7",time);
		cout<<endl;
	}
}
