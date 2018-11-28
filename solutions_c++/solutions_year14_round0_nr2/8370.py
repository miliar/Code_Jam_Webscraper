#include<iostream.h>
#include<conio.h>
#include<iomanip.h>
#include<stdio.h>
void main()
{
int t;
double c,f,x,min,t1,t2,t3;
double rate;
int p;

p=1;
min=0.0;
rate=2.0;
cin>>t;
while(t>0)
{
	rate=2.0;
	min=0.0;
	cin>>c>>f>>x;
	while(1)
	{

	  t1=c/rate;
	  t3=x/(rate+f);
	  t2=x/rate;
	  if(t1+t3<t2)
	       {
		min=min+t1;
		rate=rate+f;

	       }
	  else
	  {
	  min=min+t2;
	  break;
	  }

       }
	printf("Case #%d: %.7f\n",p,min);
	/*cout<<"Case #"<<p<<": ";
	cout.precision(7);

	cout<<min;
	if(min==a)
		cout<<".0000000";
	cout<<endl;  */

	p++;
	t--;

}
getch();
}