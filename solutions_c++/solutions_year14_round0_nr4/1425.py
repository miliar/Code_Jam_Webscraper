#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
    int t,te;
    scanf("%d",&t);
    //printf("%d\n",t);
    for(te=1;te<=t;te++)
    {
        int n,i,j,so=0,sor=0,nt;
        double wei;
        scanf("%d",&n);
        //printf("%d\n",n);
        nt=n;
        vector<double> ne;
        vector<double> ken;
        vector<double> bac;
        for(i=0;i<n;i++){scanf("%lf",&wei);ne.push_back(wei);}
        for(i=0;i<n;i++){scanf("%lf",&wei);ken.push_back(wei);}
        sort(ne.begin(),ne.end());
        sort(ken.begin(),ken.end());
        bac=ken;
        for(i=0;i<n;i++)
            {
                for(j=0;j<nt;j++)
                {
                    if(ken[j]>ne[i]){ken.erase(ken.begin()+j);break;}
                }
                if(j==nt){ken.erase(ken.begin());so++;}
                nt--;
            }
        ken=bac;
        nt=n;
        for(i=0;i<n;i++)
        {
            if(ne[i]>ken[0]){ken.erase(ken.begin());sor++;nt--;}
            else {ken.erase(ken.begin()+nt-1);nt--;}
            //else (ne[i]<ken[nt-1]
            //{
            //    sor++;
            //    ken.erase(ken.begin());
            //}
        }
        printf("Case #%d: %d %d\n",te,sor,so);
    }
    return 0;
}
