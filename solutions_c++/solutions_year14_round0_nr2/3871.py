#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
  freopen("test2.in", "r", stdin);
   freopen("output2.txt", "w", stdout);
  int testCases;
  scanf("%d", &testCases);
  for (int aa=0; aa<testCases; aa++)
  {
	  double totalCookies, totalFarms,farmCost,farmProduction;
	  cin >> farmCost >> farmProduction>>totalCookies;
	  double maxFarms=totalCookies/farmCost;
	  int maxIteration=floor(maxFarms);
	  double minTime=-1;
	  double totalFarmTime=0;
	//  cout << "MAX ITERATIONS: " <<  maxIteration << endl;
	//  cout << "INDEX" << endl;
	  for (int a=0; a<=maxIteration; a++)
	  {
		  double timeRequired=(totalCookies)/((double)(2)+((double)(a)*farmProduction));
		  if (minTime<0||totalFarmTime+timeRequired<minTime) 
		  {
		//	  cout << "INDEX: " << a << endl;
			  minTime=totalFarmTime+timeRequired;
		  }

		  // perform calc
		  double timeToBuildNext=(farmCost)/((double)(2)+(double)(a*farmProduction));
		  totalFarmTime+=timeToBuildNext;

	  }
//	  cout << "ANSWER"<< endl;
	  printf("Case #%d: %.7f\n",aa+1,minTime); 

  }


}