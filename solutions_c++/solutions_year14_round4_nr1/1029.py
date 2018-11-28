#include <vector>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

void start()
{
	printf("%d\n", TestCase);
  int result;
	// read test case
  int N;
  int X;
  ein >> N >> X;
  vector<int> S(N);
  for (int n=0;n<N;n++)
	  ein >> S[n];
  sort(S.begin(),S.end());
  int o;
  int u;
  u=0;
  o = N-1;
  result = 0;
  while (u<=o)
  {
	  result++;
	  if (S[o]+S[u]>X)		 
	  {o--;}
	  else
	  {
		  o--;
		  u++;
	  }
  }
	// output result
    fprintf(aus, "Case #%d: %d\n", TestCase, result);     // %llu , %ll
}

void main()
{
	int NumTestCases;	
	ein.open("A-large.in");
	aus = fopen("ausgabe.txt","w");
	
	ein >> NumTestCases;
	for (TestCase = 1; TestCase <= NumTestCases; TestCase++)
		start();

	fclose(aus);
	ein.close();
}
