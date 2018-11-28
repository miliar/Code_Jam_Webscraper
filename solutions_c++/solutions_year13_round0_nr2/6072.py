#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

bool myfunction (int i,int j) { return (i<j); }

int main(){
    int t,n,m,i,j,k,val,a[102][102],b[102],c[100],tt,siz,x,y,cnt,row[100],col[100];
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++){
        for(i=0;i<100;i++)
        b[i]=0;
        k=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                scanf("%d",&val);
                a[i][j]=val;

                b[val]++;

                if(b[val]==1)
                c[k++]=val;
            }
        }
        sort(c,c+k,myfunction);
        siz=k;

        for(i=0;i<siz-1;i++){
            x=0;
            for(j=0;j<n;j++){
                cnt=0;
                for(k=0;k<m;k++){
                    if(a[j][k]==c[i])
                    cnt++;
                    else
                    break;
                }
                if(cnt==m)
                row[x++]=j;
            }

            y=0;
            for(j=0;j<m;j++){
                cnt=0;
                for(k=0;k<n;k++){
                    if(a[k][j]==c[i])
                    cnt++;
                    else
                    break;
                }
                if(cnt==n)
                col[y++]=j;
            }

            for(j=0;j<x;j++){
                for(k=0;k<m;k++)
                a[row[j]][k]=c[i+1];
            }
            for(j=0;j<y;j++){
                for(k=0;k<n;k++)
                a[k][col[j]]=c[i+1];
            }
        }
        cnt=0;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(a[i][j]==c[siz-1])
                cnt++;
            }
        }
        if(cnt==(m*n))
        printf("Case #%d: YES\n",tt);
        else
        printf("Case #%d: NO\n",tt);

    }
    return 0;
}
