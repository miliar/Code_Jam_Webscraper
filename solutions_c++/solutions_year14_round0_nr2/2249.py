#include <iostream>
#include <cstdio>
using namespace std;

double C,F,X,Start,Answ;

inline void ReadTest()
{
	Answ=0.0;
	Start=2.0;

	//scanf("%f","%f","%f",&C,&F,&X);
	cin>>C>>F>>X;
}

inline bool Count(double c,double &start,double &f, double x, double &answ)
{
	double Time1=c/start;
	double Time2=X/(start+f);
	double Time3=X/start;
	if(Time1+Time2<Time3)
	{
		answ+=Time1;
		start+=f;
		return true;
	}
	else
	{
		Answ+=Time3;
		return false;
	}
}

int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;++i)
	{
		ReadTest();
		while(Count(C,Start,F,X,Answ));
		printf("Case #%d: %.7lf\n",(i+1),Answ);
	}

	return 0;
}