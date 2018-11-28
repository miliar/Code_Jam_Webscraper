#include <stdio.h>

class cookie
{
private:
	double C;
	double F;
	double X;
	double Current;
	double K;
	double timeEscaped;
public:
	double IsNeedFarm()
	{
		if (C/K+(X-Current)/(K+F)<(X-Current)/K)
		{
			return true;
		}
		return false;
	}
	void BuyFarm()
	{
		K+=F;
		Current-=C;
	}
	void WaitToBuyFarm()
	{
		timeEscaped+=C/K;
		Current+=C;
	}
	void WaitTillX()
	{
		timeEscaped+=(X-Current)/K;
	}
	double GetEscapedTime()
	{
		return timeEscaped;
	}
	cookie(double C,double F,double X)
		:C(C),F(F),X(X),K(2),Current(0),timeEscaped(0)
	{
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("res.txt","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	int T;
	scanf("%d",&T);
	int count = 0;
	for (;T;--T)
	{
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		cookie ans(C,F,X);
		for (;;)
		{
			if (ans.IsNeedFarm())
			{
				ans.WaitToBuyFarm();
				ans.BuyFarm();
			}
			else
			{
				ans.WaitTillX();
				printf("Case #%d: %.7f\n",++count,ans.GetEscapedTime());
				break;
			}
		}
	}
	return 0;
}

