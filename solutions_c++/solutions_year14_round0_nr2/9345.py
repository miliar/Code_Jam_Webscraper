#include <iostream>
#include <vector>
using namespace std;
double cost(double valC,double valF,double valX)
{
	bool sign=true;
	double temTime=0,accTime=10000000000;
	int count=0;
	while(sign)
	{
		count++;
		if(count>1)
		{
			int temCount=count;
			temTime=0;
			while(temCount!=1)
			{
				temTime+=valC/(2+valF*(count-temCount));
				temCount--;
			}
			temTime+=valX/(2+valF*(count-1));
		}
		else if(count==1) temTime=valX/2.0;
		
		if(temTime<accTime) accTime=temTime;
		else sign=false;
	}
	return accTime;
}
int main()
{
	vector<double> time;
	int T=0;
	double C=0,F=0,X=0;
	cin>>T;
	int temT=T;
	while(temT)
	{
		cin>>C>>F>>X;
		time.push_back(cost(C,F,X));
		temT--;
	}
	int cou=0;
	for(vector<double> ::iterator p=time.begin();p!=time.end();p++)
	{
		cou++;
		double val=(*p);
		printf("Case #%d: %.7f\n",cou,val);
		//cout<<"Case #"<<cou<<": "<<(*p)<<endl;
	}
	return 0;
}