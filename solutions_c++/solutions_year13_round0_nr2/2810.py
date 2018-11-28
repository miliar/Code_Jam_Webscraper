#include<iostream>
#include<cstdio>
 
using namespace std;
int main()
{
    int t,i,j,k,f,maxr,maxc,n,m;
    int a[104][104],row[104],col[104];
        scanf("%d",&t);
        for(k=1;k<=t;k++) {
                scanf("%d %d",&n,&m);
                for(i=0;i<n;i++) {
                        for(j=0;j<m;j++) {
                                scanf("%d",&a[i][j]);
                        }
                }
                for(i=0;i<n;i++) {
                        maxr = a[i][0];
                //      maxc = a[0][i];
                        for(j=0;j<m;j++) {
                                if(maxr <= a[i][j]) {
                                        maxr = a[i][j];
                                        row[i]=maxr;
                                }
                        }
                }
                for(i=0;i<m;i++) {
                        maxc = a[0][i];
                        for(j=0;j<n;j++) {
                                if(maxc <= a[j][i]) {
                                        maxc = a[j][i];
                                        col[i] = maxc;
                                }
                        }
                }
                f = 0;
                for(i=0;i<n;i++) {
                        for(j=0;j<m;j++) {
                                if((a[i][j]<row[i]) && (a[i][j] < col[j])) {
                                        f=1;
                        //              printf("%d",a[i][j]);
                                        break;
                                }
                        }
                        if(f==1)
                        break;
                }
                if(f==1)
                printf("Case #%d: NO\n",k);
                else
                printf("Case #%d: YES\n",k);
        }
        return 0;
}
