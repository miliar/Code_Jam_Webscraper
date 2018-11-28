#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("output.txt");
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
       int case2=0,case1=0,n,j;
       double naomi_wts[1001],ken_wts[1001];
       scanf("%d",&n);
       for(int p=0; p<n; p++)
           scanf("%lf",&naomi_wts[p]);
       for(int p=0; p<n; p++)
           scanf("%lf",&ken_wts[p]);
       sort(naomi_wts,naomi_wts+n);
       sort(ken_wts,ken_wts+n);
        for(int p=0,j=0;p<n;p++)
        {
            if(naomi_wts[p]>ken_wts[j])
            {
                case2++;
                j++;
            }
        }

        for(int p=0,j=0;p<n;p++)
        {
            if(ken_wts[p]>naomi_wts[j])
            {
                case1++;
                j++;
            }
        }
        fout<<"Case #"<<i<<": "<<case2<<" "<<(n-case1)<<endl;
    }
    return 0;
}
