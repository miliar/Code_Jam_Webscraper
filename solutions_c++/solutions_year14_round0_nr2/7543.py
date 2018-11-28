#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

// Helper function to solve the question
void solve(int Cs)
{
	double C, F, X, Rate = 2.0, T1, T2, ANS = 0;
	scanf("%lf %lf %lf",&C,&F,&X);
	// Time T1 is the time that will be taken if we continue at the current rate of increase
	T1 = X / Rate;
	T2 = (C / Rate) + (X / (Rate + F));
	//cout<<T1<<" "<<T2<<endl;
	if(T2 >= T1)
	{
		// If time taken to increase the rate in the 1st step is more then print answer and return
		ANS = T1;
		printf("Case #%d: %.7lf\n",Cs,ANS);
		return;
	}
	else
	{
		ANS += (C / Rate);

		// Whenever T1 and T2 become equal get out of the loop
		while (T1 > T2)
		{	
			Rate += F;
			T1 = X / Rate;
			T2 = (C / Rate) + (X / (Rate + F));

			// Only change if T1 is greater than T2
			if(T1 > T2)
				ANS += (C / Rate);
			
			//cout<<"T1: "<<T1<<" T2: "<<T2<<" CURRENT TOTAL TIME ELAPSED: "<<ANS<<endl;
		}

		ANS += (X / Rate);

		printf("Case #%d: %.7lf\n",Cs,ANS);
		return;
	}
}

// Main function
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)
		solve(i);
	
	return 0;
}

