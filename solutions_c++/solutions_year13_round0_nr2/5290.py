#include<stdio.h>
using namespace std;

int  main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,l,w;
    scanf("%d",&t);
    for (int k=1;k<=t;k++){
        scanf("%d %d",&l,&w);
        int tar [l][w];
        int lawn [l][w];
        for (int i =0;i<l;i++)
            for (int j=0;j<w;j++){
                scanf("%d",&tar[i][j]);
                lawn[i][j]=100;
            }
        for (int i=0;i<l;i++){
            int max = -1;
            for (int j=0;j<w;j++)
                if (tar[i][j]>max)
                    max = tar[i][j];
            for (int j =0;j<w;j++)
                if (lawn[i][j]>max)
                    lawn[i][j] = max;
        }
        for (int i=0;i<w;i++){
            int max = -1;
            for (int j=0;j<l;j++)
                if (tar[j][i]>max)
                    max = tar[j][i];
            for (int j =0;j<l;j++)
                if (lawn[j][i]>max)
                    lawn[j][i] = max;
        }
        int found = 1;
        for (int i =0;i<l;i++){
            for (int j=0;j<w;j++)
                if (lawn[i][j]!=tar[i][j]){
                    found = 0;
                    break;
                }
            if (!found)
                break;
        }
        if (found)
            printf("Case #%d: YES\n",k);
        else printf("Case #%d: NO\n",k);
    }
}
