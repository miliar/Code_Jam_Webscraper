#include <iostream>
#include<stdio.h>
using namespace std;
int t;
int n,i,max1,max2,ind1,ind2,cas;
int a[26];
int main() {
    scanf("%d",&t);
    cas=1;
    while(t--)
    {
        int flag=0;
        
        scanf("%d",&n);
        i=0;
        max1=0;
        max2=0;
        ind2=0;
        ind1=0;
        while(n--)
        {
            scanf("%d",&a[i]);
            if(max1<=a[i])
            {
                max2=max1;
                max1=a[i];
                ind2=ind1;
                ind1=i;
            }
            else if(max2<=a[i])
            {
                max2=a[i];
                ind2=i;
            }
            i++;
        }
        printf("Case #%d:",cas);
        while(max1)
        {
            if(max1>1 && max2>1)
            {
                printf(" %C%C",'A'+ind1,'A'+ind2);
                a[ind2]--;
                a[ind1]--;
            }
            else if(max1>1)
            {
                printf(" %C",'A'+ind1);
                a[ind1]--;
            }
            else if((i%2) && (!flag))
            {
                printf(" %C",'A'+ind1);
                a[ind1]--;
                flag=1;
            }
            else if(max1 && max2)
            {
                printf(" %C%C",'A'+ind1,'A'+ind2);
                a[ind2]--;
                a[ind1]--;
            }
            else if(max1)
            {
                printf(" %C",'A'+ind1);
                a[ind1]--;
            }
            n=i;
            i=0;
            max1=0;
            max2=0;
            ind2=0;
            ind1=0;
            while(n--)
            {
                if(max1<=a[i])
                {
                    max2=max1;
                    max1=a[i];
                    ind2=ind1;
                    ind1=i;
                }
                else if(max2<=a[i])
                {
                    max2=a[i];
                    ind2=i;
                }
                i++;
            }
            
        }
        printf("\n");
        cas++;
        
    }
	// your code goes here
	return 0;
}
