#include<stdio.h>

int main(){
freopen("B-small-attempt0.txt","r",stdin);
freopen("output1.txt","w",stdout);
int t,n,m,i,j,k,k1,k2,min,temp=0,count=0;

scanf("%d",&t);

while(t--){
        count++;
int flag=0,flag1=0;
scanf("%d %d",&n,&m);

int a[100][100]={0};

for(i=0;i<n;i++){
for(j=0;j<m;j++)
scanf("%d",&a[i][j]);

}

for(i=0;i<n;i++){
    min=a[i][0];
    temp=0;
    for(j=0;j<m;j++){

        if(a[i][j]<min){
        min=a[i][j];
        temp=j;
        flag=1;
        }
        else if(a[i][j]>min)
            flag=1;
        if(flag==1){
            flag=0;

                for(k2=0;k2<n;k2++){
                        if(a[i][k2]==min){
                                temp=k2;
        for(k=0;k<n;k++){
            if(a[k][temp]>min){
                flag1=1;
                flag=1;
                break;
            }
        }
        }
        }
    }
    }


    if(flag1==1&&flag==1){
        printf("Case #%d: NO \n",count);
        break;
    }
}
if(flag1==0){
for(i=0;i<m;i++){
    min=a[0][i];
    temp=0;
    for(j=0;j<n;j++){

        if(a[j][i]<min){
        min=a[j][i];
        temp=j;
        flag=1;
        }
        else if(a[j][i]>min)
            flag=1;
    }

    if(flag==1){
            flag=0;
        for(k=0;k<m;k++){
            if(a[temp][k]>min){
                flag1=1;
                break;
            }
        }

    }
    if(flag1==1){
        printf("Case #%d: NO \n",count);
        break;
    }
}
}
if(flag1==0){
        printf("Case #%d: YES\n",count);
    }
}

return 0;
}
