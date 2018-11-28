#include <vector>
#include <algorithm>
#include <fstream>
#include <math.h>
#include <algorithm>
using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

void start()
{
	printf("%d\n", TestCase);
  double result;
	// read test case
   int N;
   double V,X;
   ein >> N >> V >> X;
   vector<pair<double,double>> CR;

   for (int n=0;n<N;n++)
   {	   
	   pair<double,double> kcr;
	   ein >> kcr.second >> kcr.first;
	   for (int m=0;m<CR.size();m++)
	   {
		   if (CR[m].first == kcr.first)
		   {
			   CR[m].second += kcr.second;
			   kcr.first = 0;
			   break;
		   }
	   }
	   if (kcr.first>0)
	   {
		   CR.push_back(kcr);
	   }

   }
   sort(CR.begin(),CR.end());
   if ((X < CR[0].first) || (X > CR[CR.size()-1].first))
   {
	   fprintf(aus, "Case #%d: IMPOSSIBLE\n", TestCase);     // %llu , %ll
       return;
   }
   double dmax = 0;
   for (int n=0;n<CR.size();n++)
   {
	   if (V/CR[n].second > dmax)
		   dmax = V/CR[n].second;
   }

   double d;
   double dmin = 0;
   while (dmax - dmin > 0.000000004)
   {
	   d = (dmax + dmin) / 2;
	   // test d

	   double VV, Smax, Smin,Vi;
	   
	   VV = V;	   
	   Smax = 0;
	   for (int i=CR.size()-1;i>=0;i--)
	   {
		   Vi = min(VV,d*CR[i].second);
		   VV -= Vi;
		   Smax += Vi*CR[i].first;
	   }
	   VV = V;	   
	   Smin = 0;
	   for (int i=0;i<CR.size();i++)
	   {
		   Vi = min(VV,d*CR[i].second);
		   VV -= Vi;
		   Smin += Vi*CR[i].first;
	   }
	   //  Smin <= V*X <= Smax ?
	   if ((Smin <= V*X) && (V*X <= Smax))
	   {
		   // d ok
		   dmax = d;
	   }
	   else
	   {
		   dmin = d;
	   }
   }
   result = dmax;
	// output result
    fprintf(aus, "Case #%d: %.9f\n", TestCase, result);     // %llu , %ll
	/*if (N==2)
	{
		if (CR[0].first != CR[1].first)
		{
			double lambda = (X-CR[1].first)/(CR[0].first-CR[1].first);
			fprintf(aus, "Case #%d: %.9f\n", TestCase, max((lambda*V)/CR[0].second,(1-lambda)*V/CR[1].second));     // %llu , %ll
		}
	}*/
}

void main()
{
	int NumTestCases;	
	ein.open("B-large.in");
	aus = fopen("ausgabe.txt","w");
	
	ein >> NumTestCases;
	for (TestCase = 1; TestCase <= NumTestCases; TestCase++)
		start();

	fclose(aus);
	ein.close();
}
