#include<iostream>
#include<cstdio>
using namespace std;
int b[150000];
int mult(int a,int b){
    if(a<0)return -1*mult(a*-1,b);
    if(b<0)return -1*mult(a,b*-1);
    if(a==1)return b;
    if(b==1)return a;
    if(a==b)return -1;
    if(a==2&&b==3)return 4;
    if(a==3&&b==2)return -4;
    if(a==2&&b==4)return -3;
    if(a==4&&b==2)return 3;
    if(a==3&&b==4)return 2;
    if(a==4&&b==3)return -2;
}
int main(){
    int T,I;
    scanf("%d",&T);
    for(I=1;I<=T;I++){
        int l,x,a[10005];
        char s[10005];
        scanf("%d %d",&l,&x);
        scanf("%s",s);
        printf("Case #%d: ",I);
        int i,j,c=1,t=0,jj,ii;
        for(i=0;i<l;i++){
            if(s[i]=='i')a[i]=2;
            else if(s[i]=='j')a[i]=3;
            else a[i]=4;
        }
        for(i=0;i<l;i++){
            c=mult(c,a[i]);
        }
        if(c==-1){
            if(x%2!=1){
                printf("NO\n");
                continue;
            }
            for(ii=1;ii<16;ii+=2){
                if(ii>x||t==1)break;
                for(i=0;i<ii;i++){
                    for(j=0;j<l;j++){
                        b[i*l+j]=a[j];
                    }
                }
                int ti=1,tk=1;
                for(i=0;i<ii*l;i++){
                    ti=mult(ti,b[i]);
                    if(ti==2)break;
                }
                for(j=ii*l-1;j>=0;j--){
                    tk=mult(b[j],tk);
                    if(tk==4)break;
                }
                if(j>i){
                    t=1;
                    break;
                }
            }
            if(t==1)printf("YES\n");
            else printf("NO\n");
        }
        else if(c!=1){
            if(x%4!=2){
                printf("NO\n");
                continue;
            }
            for(ii=2;ii<=14;ii+=4){
                //printf("ii= %d\n",ii);
                if(ii>x||t==1)break;
                for(i=0;i<ii;i++){
                    for(j=0;j<l;j++){
                        b[i*l+j]=a[j];
                    }
                }
                int ti=1,tk=1;
                for(i=0;i<ii*l;i++){
                    ti=mult(ti,b[i]);
                    if(ti==2)break;
                }
                for(j=ii*l-1;j>=0;j--){
                    tk=mult(b[j],tk);
                    //printf("tk= %d\n",tk);
                    if(tk==4)break;
                }
                if(j>i){
                    t=1;
                    break;
                }
            }
            if(t==1)printf("YES\n");
            else printf("NO\n");
        }
        else{
            printf("NO\n");
        }
    }
    return 0;
}