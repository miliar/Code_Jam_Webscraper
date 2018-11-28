#include <stdio.h>
#include <stdlib.h>

int table[105][105];
int getCut[105][105];
int r,c;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int zz,tt;
    scanf("%d",&zz);
    int i,j;
    for(int tt=1;tt<=zz;tt++){
        bool able = true;
        scanf("%d%d",&r,&c);
        for(i=1;i<=r;i++){
            for(j=1;j<=c;j++){
                scanf("%d",&table[i][j]);
                getCut[i][j] = 0;
            }
        }
        while(true){
            bool hasChange = false;
            for(i=1;i<=r;i++){
                int maxHasCut = -1;
                int same=-1;
                for(j=1;j<=c;j++){
                    if(getCut[i][j]){
                        if(maxHasCut<table[i][j]){
                            maxHasCut=table[i][j];
                        }
                        continue;
                    }else{
                        if(same==-1){
                            same = table[i][j];
                            continue;
                        }else if(same==table[i][j]){
                            continue;
                        }else{
                            break;
                        }
                    }
                }
                if(j==c+1 && same!=-1 && maxHasCut<=same){
                    for(j=1;j<=100;j++){
                        getCut[i][j] = 1;
                    }
                    hasChange = true;
                }
            }

            for(i=1;i<=c;i++){
                int maxHasCut = -1;
                int same=-1;
                for(j=1;j<=r;j++){
                    if(getCut[j][i]){
                        if(maxHasCut<table[j][i]){
                            maxHasCut=table[j][i];
                        }
                        continue;
                    }else{
                        if(same==-1){
                            same = table[j][i];
                            continue;
                        }else if(same==table[j][i]){
                            continue;
                        }else{
                            break;
                        }
                    }
                }
                if(j==r+1 && same!=-1 && maxHasCut<=same){
                    for(j=1;j<=100;j++){
                        getCut[j][i] = 1;
                    }
                    hasChange = true;
                }
            }

            if(!hasChange){
                break;
            }
        }
        for(i=1;i<=r;i++){
            for(j=1;j<=c;j++){
                if(getCut[i][j]==0){
                    able = 0;
                }
            }
        }
        printf("Case #%d: ",tt);
        if(able==0){
            printf("NO\n");
        }else{
            printf("YES\n");
        }
    }
	return 0;
}
/*
4
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
4 4
1 2 1 1
1 2 2 1
1 1 1 1
1 1 1 1
*/
