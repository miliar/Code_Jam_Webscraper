#include<bits/stdc++.h>

using namespace std;

#define size 10005

char mult[5][5] = 
    {
        {0,0,0,0,0},
        {0,1,2,3,4},
        {0,2,-1,4,-3},
        {0,3,-4,-1,2},
        {0,4,3,-2,-1}
    };

char oper(char x, char y){
    char sign = 1;
    if(x<0) {
        sign*=-1;
        x*=-1;
    }
    if(y<0) {
        sign*=-1;
        y*=-1;
    }
    return mult[x][y]*sign;
}

int main(){

    int T,cs,n,i,len,tot,cnt,diff,L,X,j;
    char a[size],arr[size],prfx[size],sffx[size];
    char res;
    scanf("%d", &T);

    for(cs=1;cs<=T;cs++){
        scanf("%d %d",&L,&X);
        scanf("%s",a);
        for(i=0;i<L;i++) a[i]=a[i]-'g';
        for(i=0;i<X;i++) memcpy(arr+i*L,a,L);
        tot=L*X;
        prfx[0]=arr[0];
        for(i=1;i<tot;i++)
            prfx[i]=oper(prfx[i-1],arr[i]);
        i=tot-1;
        sffx[i]=arr[i];
        for(i--;i>=0;i--)
            sffx[i]=oper(arr[i],sffx[i+1]);

        // for(i=0;i<tot;i++) printf("%d ",prfx[i]);
        // printf("\n");
        // for(i=0;i<tot;i++) printf("%d ",sffx[i]);
        // printf("\n");

        if(tot<3||prfx[tot-1]!=-1){
            printf("Case #%d: NO\n",cs);
            continue;
        }

        for(i=0;i<tot;i++){
            if(prfx[i]==2){
                for(j=i+2;j<tot;j++)
                    if(sffx[j]==4)
                        break;
                if(j<tot) break;
            }
        }

        if(i<tot)
            printf("Case #%d: YES\n",cs);
        else
            printf("Case #%d: NO\n",cs);

        
    }

    return 0;
}
