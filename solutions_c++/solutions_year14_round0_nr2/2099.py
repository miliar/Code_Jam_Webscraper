#include<iostream>
#define rep(i,n) for (int i=0;i<n;i++)
#define For(i,a,b) for (int i=a;i<=b;i++)
using namespace std;
double C,F,X;
int caseNum;
void mainProcess()
{
	//int farm=((int)X/2)+1;
	double ans=X/2.0;
	double totalTime=0;
	//rep(i,farm){
	for(int i=0;;i++)
	{
		totalTime+=C/(2.0+i*F);
		if (totalTime+X/(2.0+F*(i+1))<ans)
			ans=totalTime+X/(2.0+F*(i+1));
		else
			break;
	}
	++caseNum;
	printf("Case #%d: %.7lf\n",caseNum,ans);
}
int main(){
	int testnum;
	scanf("%d",&testnum);
	rep(test,testnum)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		mainProcess();
	}
	return 0;
}
