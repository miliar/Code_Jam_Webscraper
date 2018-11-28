#include<climits>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void Cookie(double C, double F,double X)
{
	double totalTime = 0;
	
	

	if (X < C)
	{
		printf("%.7f\n", X / 2 );
		return;
	}

	double cookies = 0;
	double moreToGo = X;
	double speed = 2;
	
	while (moreToGo != 0)
	{
		double directTime, farmTime;
		moreToGo = X - cookies;
		directTime = moreToGo / speed;
		farmTime = (C / speed);
		farmTime += (moreToGo / (speed + F));
		if (directTime < farmTime)
		{
			totalTime += directTime;
			moreToGo = 0;
		}
		else
		{
			moreToGo = X;
			totalTime += (C / speed);
			speed += F;
		}

	}

	printf("%.7f\n", totalTime);


}

int main()
{
	int T = 0;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << i + 1 << ": ";
		Cookie(C, F, X);
	}
}