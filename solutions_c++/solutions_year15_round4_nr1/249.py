#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

void start()
{
	printf("%d\n", TestCase);
  int result;
	// read test case
  int R, C;
  ein >> R >> C;

  string a[100];
  for (int r=0;r<R;r++)
	  ein >> a[r];

  result = 0;
  for (int r=0;r<R;r++) {
	  for (int c=0;c<C;c++)
	  {
		  int dr,dc;
		  if (a[r][c]!='.')
		  {
			  int ok[4];
			  int sumok = 0;
			  for (int oi=0;oi<4;oi++)
		      {
				  switch(oi)
				  {
				  case 0:
					  dr=-1;
					  dc=0;
			          break;
				  case 1:
					  dr=1;
					  dc=0;
					  break;
				  case 2:
					  dr=0;
					  dc=1;
				      break;
				  case 3:
					  dr=0;
					  dc=-1;
				      break;
				  }
				  ok[oi] = 0;
				  int er=r+dr;
				  int ec=c+dc;
			  
				  while ((er>=0) && (er<R) && (ec>=0) && (ec<C))
			      {
  					if (a[er][ec]!='.')
						ok[oi] = 1;
					er+=dr;
					ec+=dc;
				  }

				  sumok += ok[oi];
			  }
		      int mydir;
			  if (a[r][c]=='^')
			  {
				  mydir = 0;
			  }
			  if (a[r][c]=='v')
			  {
				  mydir = 1;
			  }
			  if (a[r][c]=='>')
			  {
				  mydir = 2;
			  }
			  if (a[r][c]=='<')
			  {
				  mydir = 3;
			  }
			  if (ok[mydir] == 0)
			  {
				  if (sumok == 0)
					  result = -1;
				  else
					  result++;
			  }
		  }
		  if (result < 0)
			  break;
	  }
}
	// output result
    if (result>=0)
		fprintf(aus, "Case #%d: %d\n", TestCase, result);     // %llu , %ll
	else		
		fprintf(aus, "Case #%d: IMPOSSIBLE\n", TestCase);     // %llu , %ll
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
