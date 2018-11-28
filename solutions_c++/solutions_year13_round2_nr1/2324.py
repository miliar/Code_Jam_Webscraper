#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int
	T;

void copy_vector(const vector<int>& src, vector<int>& dest)
{
   for (vector<int>::const_iterator iter = src.begin(); iter != src.end(); iter++)
      dest.push_back(*iter);
}

int get_solution(int lA, int lN, const vector<int>& lm, int lastadd)
{
   bool
      bEvergrew = false,
      bGrew;

   vector<int>
      copy;
   
   copy_vector(lm, copy);

   do
      {
      bGrew = false;
      for (vector<int>::iterator iter = copy.begin(); iter != copy.end(); iter++)
         if (lA > *iter)
            {
            lA += *iter;
            copy.erase(iter);
            bGrew = true;
            bEvergrew = true;
            break;
            }
      }
   while (bGrew);

   if (copy.size() == 0)
      return (0);

   if (copy.size() == 1)
      return (1);

   int
      nBest = copy.size(),
      nCount = nBest,
      nCurr;

   if (*(copy.begin() + nCount - 1) != lastadd)
      {
      vector<int>
         copy2;

      copy_vector(copy, copy2);
      copy2.erase(copy2.begin() + nCount - 1);
      nCurr = 1 + get_solution(lA, nCount + 1, copy2, -1);

      if (nCurr == 1)
         return (1);

      if (nCurr < nBest)
         nBest = nCurr;
      }

   if (lA > 1)
      {
      vector<int>
         copy2;
      
      copy_vector(copy, copy2);
      copy2.push_back(lA - 1);
      sort(copy2.begin(), copy2.end());
      nCurr = 1 + get_solution(lA, nCount + 1, copy2, lA - 1);

      if (nCurr == 1)
         return (1);

      if (nCurr < nBest)
         nBest = nCurr;
      }

   return (nBest);
}

int main(int argc, char *argv[])
{
   FILE
	   *fpi = fopen("A-small.in", "r"),
	   *fpo = fopen("A-small.out", "w");

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
      int
         A,
         N;

      vector<int>
         m;

		fscanf(fpi, "%d", &A);
		fscanf(fpi, "%d", &N);

      for (int j = 0; j < N; j++)
         {
         int
            t;

   		fscanf(fpi, "%d", &t);
         m.push_back(t);
         }

      sort(m.begin(), m.end());
      fprintf(fpo, "Case #%d: %d\n", i + 1, get_solution(A, N, m, -1));
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
