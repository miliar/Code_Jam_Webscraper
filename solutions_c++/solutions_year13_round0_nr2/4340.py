#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define CodeJam_main main
#define arraysize 128

int check(int a[arraysize][arraysize],int b[arraysize],int c[arraysize],int N,int M,int i)
{
  int j,k;
  for(j = 0;j < N;j++)
    {
      for(k = 0;k<M;k++)
        {
          if(a[j][k] < b[j] &&
               a[j][k] < c[k])
            {
              printf("Case #%d: NO\n",i);              
              return 0;
            }
        }
    }
  return 1;
}

int CodeJam_main(int argc,char **argv) 
{ 
#ifdef FILEIO
  freopen("2013CodeJam_in.txt","r",stdin); 
  freopen("2013CodeJam_out.txt","w",stdout); 
#endif

  int T;
  int N,M;

  int i;
  int j,k;
  int a[arraysize][arraysize];
  int b[arraysize];
  int c[arraysize];

  scanf("%d",&T);


  for(i = 1;i <= T;i++)
    {
      memset(a,0,arraysize*arraysize*sizeof(int));
      memset(b,0,arraysize*sizeof(int));
      memset(c,0,arraysize*sizeof(int));
      
      scanf("%d%d",&N,&M);

      for(j = 0;j<N;j++)
        {
          for(k = 0;k<M;k++)
            {
              scanf("%d",&a[j][k]);
              if(a[j][k]>b[j])
                b[j] = a[j][k];

              if(a[j][k]>c[k])
                c[k] = a[j][k];
            }
        }

      if(check(a,b,c,N,M,i) == 1) 
        {
          printf("Case #%d: YES\n",i);
        }
    }


#ifdef FILEIO
  fclose(stdin);
  fclose(stdout);
#endif

  return 0; 
} 
