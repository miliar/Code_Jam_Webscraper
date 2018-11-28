#include<cstdio>
#include<algorithm>
using namespace std;

int tab[5],tab1[5];
int main(){
    int t,x,y,a,b,l,pom;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d",&x);
        for(int j=0;j<4;j++){
            if(j==x-1){
                for(int k=0;k<4;k++)scanf("%d",&tab[k]);
            }
            else for(int k=0;k<4;k++)scanf("%d",&pom);
        }
        scanf("%d",&y);
        for(int j=0;j<4;j++){
            if(j==y-1){
                for(int k=0;k<4;k++)scanf("%d",&tab1[k]);
            }
            else for(int k=0;k<4;k++)scanf("%d",&pom);
        }
        sort(tab,tab+4);
        sort(tab1,tab1+4);
        a=0;
        b=0;
        l=0;
        while(a<4&&b<4){
            if(tab[a]==tab1[b]){
                x=tab[a];
                l++;
                a++;
                b++;
            }
            if(tab[a]<tab1[b])a++;
            if(tab[a]>tab1[b])b++;
        }
        if(l>1)printf("Case #%d: Bad magician!\n",i+1);
        if(l==1)printf("Case #%d: %d\n",i+1,x);
        if(l==0)printf("Case #%d: Volunteer cheated!\n",i+1);
    }
}
