#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("c:\\temp\\in.txt","r",stdin);
    freopen("c:\\temp\\out.txt","w",stdout);
    int test_case;
    scanf("%d",&test_case);
    for(int ca=1;ca<=test_case;ca++)
    {
        int n;
        scanf("%d",&n);
        double na[1500],ken[1500];
        for(int i=0;i<n;i++)
            scanf("%lf",&na[i]);
        sort(na,na+n);
        for(int i=0;i<n;i++)
            scanf("%lf",&ken[i]);
        sort(ken,ken+n);
        ///when naomi playing optimally
        int i=0,j=0,opt=0;
        while(i<n && j<n)
        {
            if(na[i]<ken[j])
            {
                i++;j++;
                opt++;
            }
            else j++;
        }
      opt=n-opt;
    ///when playing deceitful
     i=0;j=0;int dec=0;
     while(i<n)
     {
        if(na[i]<ken[j])
            i++;
        else
        {
            dec++;i++;j++;
        }
     }
     printf("Case #%d: %d %d\n",ca,dec,opt);
    }
    return 0;
}
