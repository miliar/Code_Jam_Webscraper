#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
    int t;

    FILE *ptr;
    FILE *ptr1;
    ptr1=fopen("file1.txt","r");
    ptr=fopen("file.txt","w");
    fscanf(ptr1,"%d",&t);

    for(int i=1;i<=t;i++)
    {
      int n,ans1=0,ans2=0;
      fscanf(ptr1,"%d",&n);

      double naomi[n],ken[n];
      int done[2003];

      for(int j=0;j<=2000;j++)
      done[j]=0;

      for(int j=0;j<n;j++)
        fscanf(ptr1,"%lf",&naomi[j]);

      for(int j=0;j<n;j++)
      fscanf(ptr1,"%lf",&ken[j]);

        sort(naomi,naomi+n);
        sort(ken,ken+n);

		int flag;
        for(int j=0;j<n;j++)
        {
        	flag=0;
            for(int k=0;k<n;k++)
            {
            	if(ken[k]>naomi[j] && done[k]==0)
            	{
            		flag=1;
            		done[k]=1;
            		break;
            	}
            }
            if(flag==0)
            ans2++;
        }

         for(int j=0;j<=2000;j++)
           done[j]=0;
        int index;

        for(int j=0;j<n;j++)
        {
            flag=0;
            for(int k=n-1;k>=0;k--)
            {
                if(naomi[j]>ken[k] && done[k]==0)
                {
                    flag=1;
                    index=k;
                }
            }
            if(flag==1)
            {
                done[index]=1;
                ans1++;
            }
            else
            {
              for(int k=n-1;k>=0;k--)
              {
                  if(done[k]==0)
                  {
                      done[k]=1;
                      break;
                  }
              }

            }
        }
        fprintf(ptr,"Case #%d: %d %d\n",i,ans1,ans2);
    }
    fclose(ptr);
    fclose(ptr1);
    return 0;
}
