#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
int main()
{
	int T;
	int counter=0;
	cin>>T;
	while(T--)
	{
		counter++;
		double C,F,X;
		cin>>C>>F>>X;
		int answer;
		double ans1,t_curr,curr_rate=2;
		ans1=(X-C)*F/C;
		int ans=(ans1-2)/F;
		double t_prev=0;
		for(int i=0;i<ans;i++)
		{
			t_prev=t_prev+C/curr_rate;
			curr_rate=curr_rate+F;
		}
		t_curr=C/curr_rate + t_prev;
		t_curr = min(t_prev + X/(curr_rate),t_curr + X/(curr_rate+F));
		cout<<"Case #"<<counter<<": ";
		printf("%.8lf\n", t_curr);
	}	
}