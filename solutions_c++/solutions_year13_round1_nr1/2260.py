#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define CodeJam_main main

int CodeJam_main(int argc,char **argv) 
{ 
#ifdef FILEIO
  freopen("2013CodeJam_in.txt","r",stdin); 
  freopen("2013CodeJam_out.txt","w",stdout); 
#endif

  int T;
  int r,t;
  int i;
  int result;

  scanf("%d",&T);

  for(i = 1;i <= T;i++)
    {
      scanf("%d %d\n",&r,&t);

      result = (int)(sqrt((float)t/(float)2  + ((float)(2*r - 1)/(float)4)*((float)(2*r - 1)/(float)4)) - ((float)(2*r - 1)/(float)4));
      
      printf("Case #%d: %d\n",i,result);
    }
    


#ifdef FILEIO
  fclose(stdin);
  fclose(stdout);
#endif

  return 0; 
} 
