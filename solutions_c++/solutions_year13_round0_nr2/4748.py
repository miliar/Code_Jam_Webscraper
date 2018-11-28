#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <algorithm>
#include <vector>
using namespace std;

int C,N,M;




int input[100][100];
bool IsValid();
main () {
	FILE *fin  = fopen ("in", "r");
	FILE *fout = fopen ("out", "w");

fscanf( fin, " %d", &C);


for (int i = 0; i < C; i++)
 {
fscanf( fin, " %d", &N);
fscanf( fin, " %d", &M);
 for (int i = 0; i < N; i++)
  {
      for (int j=0;j< M;j++)
      {
        fscanf( fin, "%d", &input[i][j]);
      }
  }

if (IsValid())
{
   fprintf (fout, "Case #%d: YES\n",i+1);
}
else
{
   fprintf (fout, "Case #%d: NO\n",i+1);
}
 }




	return 0;
}
bool IsValid()
{
for (int i=0;i<N;i++)
{
    for(int j=0;j<M;j++)
    { int z=input[i][j];
        for(int k=0;k<M;k++)
        {int b=input[i][k];
            if (input[i][j] < input[i][k])
            {
                for (int l=0;l<N;l++)
                {int f=input[l][j];
                    if (input[i][j]< input[l][j])
                    {
                        return false;
                    }
                }

            }
        }
    }

}
return true;
}
