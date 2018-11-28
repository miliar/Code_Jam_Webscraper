
#include <assert.h>
#include <fstream>

using namespace std;


int main()
{
	  std::ifstream infile("D:/input.txt");
	  int testCases=0;
	//  ofstream outfile;
		
		FILE * pFile;
		int n;
		pFile = fopen ("D:/output.txt","w");
	  
	  infile >>testCases;
	  int i=0;
      while(i<testCases)
	  {
		  double C=0;
		  double F=0;
		  double X=0;
		  infile >> C >>F >>X;
		  int cookies=0;
		  double production=2;
		  double timeSpent=0;
		  int flag=0;
		  double normTime=0;
		  double newTime=0;
		  while (flag !=1)
		  {
			  timeSpent+=C/production;
			  normTime=(X-C)/production;
			  newTime=(X)/(production+F);
			  if(normTime<newTime)
				  flag=1;
			  else
				  production+=F;
		  }
		  timeSpent+=normTime;
	//	  outfile << "Case #" <<i+1<<": %12.0f" <<timeSpent<<"\n";
		  fprintf (pFile, "Case #%d: %0.6f\n",i+1,timeSpent);
		  i++;
      }
    
		  
		  //outfile.close();
		  fclose (pFile);
	return 0;
}