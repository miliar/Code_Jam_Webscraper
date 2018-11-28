#include<stdio.h>
//#include<conio.h>
int main(){
    freopen("C:\\A\\input.txt","r",stdin);freopen("C:\\A\\output.txt","w",stdout);freopen("C:\\A\\err.txt","w",stderr);
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
            int arr[16]={0};
            for(int y=0;y<2;y++){
                    int l;
            scanf("%d",&l);
            for(int j=0;j<4;j++){
                    int k,p,m,n;
            scanf("%d%d%d%d",&k,&p,&m,&n);
            if(l==j+1){
            arr[k-1]++;
            arr[p-1]++;
            arr[m-1]++;
            arr[n-1]++;
           // printf("increase h %d\n",j);
            }//if
            }//j
            }//y
            int h=0,z=0;
            for(int x=0;x<16;x++){
                    if(arr[x]==2){ h++;  z=x+1;}
                    }
                    if(h==1){ printf("Case #%d: %d\n",i+1,z);}
                    else if(h>1){ printf("Case #%d: Bad magician!\n",i+1);}
                    else{ printf("Case #%d: Volunteer cheated!\n",i+1);}
            }
           // getch();
            return 0;
    }
