#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
bool myfunction (int i,int j) { return (i<j); }
bool mynotfunction (int i,int j) { return (i>j); }
int main()
{
    freopen ("c.in","r",stdin);
    freopen ("myfile.txt","w",stdout);
    int t,n;
    scanf("%d",&t);
    int counter=1;
    while(t--)
    {
        scanf("%d",&n);
        //double a[n];
        int i;
        vector<double> a(n);
        vector<double> b(n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
          for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
          sort(a.begin(),a.end());
          sort(b.begin(),b.end());
//          for(i=0;i<n;i++)
//          {
//            printf("%lf ",a[i]);
//          }
//          printf("\n");
//            for(i=0;i<n;i++)
//          {
//            printf("%lf ",b[i]);
//          }
//          printf("\n");
int c=0,c1=0;
int count=0,count1=0;
            for(i=0;i<n;i++)
            {
                if(a[i]>b[c])
                {
                    count++;
                    c++;
                }
            }
            for(i=0;i<n;i++)
            {
                if(b[i]>a[c1])
                {
                    c1++;
                }
                else
                {
                    count1++;
                    //c1++;
                }
            }
            printf("Case #%d: %d %d\n",counter++,count,count1);

    }
    fclose(stdout);
    return 0;
}
