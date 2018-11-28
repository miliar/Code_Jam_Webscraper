#include<stdio.h>
#include<algorithm>
using namespace std;
main(){
    int T,Case=0;
    int a[10],b[10],x;
    int ra,rb;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&ra);
        for(int i=0;i<4;i++){
            if(i==ra-1){
                for(int j=0;j<4;j++)scanf("%d",a+j);
            }
            else{
                for(int j=0;j<4;j++)scanf("%d",&x);
            }
        }
        scanf("%d",&rb);
        for(int i=0;i<4;i++){
            if(i==rb-1){
                for(int j=0;j<4;j++)scanf("%d",b+j);
            }
            else{
                for(int j=0;j<4;j++)scanf("%d",&x);
            }
        }
        sort(a,a+4);
        sort(b,b+4);
        ra=rb=0;
        int cnt=0,p;
        while(ra<4&&rb<4){
            if(a[ra]<b[rb])ra++;
            else if(a[ra]>b[rb])rb++;
            else p=a[ra],ra++,rb++,cnt++;
        }
        if(cnt==0)printf("Case #%d: Volunteer cheated!\n",++Case);
        else if(cnt==1)printf("Case #%d: %d\n",++Case,p);
        else printf("Case #%d: Bad magician!\n",++Case);
    }
}
