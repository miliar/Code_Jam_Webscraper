/* https://code.google.com/codejam/contest/2974486/dashboard#s=p3
 * Problem D. Deceitful War
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{

    int t,l;
    scanf("%d",&t);
    for( l=1;l<=t;l++)

    {
        int n,start,end,start1,end1,i,j,y,z;
        y=0;
        z=0;
        scanf("%d",&n);
        float naomi[n],ken[n];
        for(i=0;i<n;i++)
            scanf("%f",&naomi[i]);

        for(j=0;j<n;j++)
            scanf("%f",&ken[j]);


        sort(naomi,naomi+n);
        sort(ken,ken+n);

        start=0;
        end=n-1;
        start1=0;
        end1=n-1;

        //war
        while(start<=end)
            {
            if(naomi[end]>ken[end1])
                {
                    end--;

                    z++;
                }
            else
                {
                    end1--;
                    end--;
                }
            }

        //deciteful war
        start=0;
        end=n-1;
        start1=0;
        end1=n-1;

         while(start<=end)
            {

                 if(naomi[start]<ken[start1])
                    {
                        end1--;
                        start++;
                    }
                else if((naomi[start]>ken[start1])&&(naomi[end]>ken[end1]))

                    {
                        start++;
                        start1++;
                        y++;
                    }
                else
                    {
                        start++;
                        end1--;
                    }
            }
        printf("Case #%d: %d %d\n",l,y,z);
    }
return 0;
}
