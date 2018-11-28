#include <bits/stdc++.h>
#include <iostream>
#include <list>
#include <cstdlib>
#include <limits.h>
#include <cstdio>
#include <map>
#include <queue>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <string.h>
using namespace std;


int main()
{
      int tests,standing,invited;char arr[10000];
       FILE *fp;
      fp = fopen("input.in","r");
      fscanf(fp, "%i", &tests);
      int ans[tests];int numcap;
      for(int i=0;i<tests;i++)
      {
          fscanf(fp, "%i %s\n",&numcap, arr);
          standing=arr[0]-48;

          invited=0;
          for(int j=1;j<numcap+1;j++)
          {
              if(standing>=j)
              standing=standing+arr[j]-48;

              else if(arr[j]>48)
              {
                  int changeinv=invited;
                  invited=invited+j-standing;
                  changeinv=invited-changeinv;
                  standing=changeinv+standing+arr[j]-48;

              }

          }
          ans[i]=invited;

      }

      fp = fopen("output.txt","w");

      for(int i=0;i<tests;i++)
      {
          fprintf(fp, "Case #%d: %d\n",i+1,ans[i]);
          printf("Case #%d: %d\n",i+1,ans[i]);

      }



}
