
#include <cstdio>
#include <iostream>
#include<cstring>

using namespace std;

int main()
{

    //freopen("A-small-attempt0.in","r", stdin);
    //freopen("A-small-attempt0.out","w", stdout);
    int a,b,c,d,found,N,row,number;
    bool guess[17];
    scanf("%d",&N);
    for(int i=1;i<=N;i++){
            for(int j=0;j<=16;j++){
            guess[j]=false;
        }
        scanf("%d",&row);
        found=0;
        number=0;
        for(int j=1;j<=4;j++){
            if(row == j){
                scanf("%d %d %d %d",&a,&b,&c,&d);
                guess[a]=true;
                guess[b]=true;
                guess[c]=true;
                guess[d]=true;
            }
            else{
                scanf("%d %d %d %d",&a,&b,&c,&d);
            }
        }
        scanf("%d",&row);

        for(int j=1;j<=4;j++){
            if(row == j){
                scanf("%d %d %d %d",&a,&b,&c,&d);
                if(guess[a]==true){found++;number=a;}
                if(guess[b]==true){found++;number=b;}
                if(guess[c]==true){found++;number=c;}
                if(guess[d]==true){found++;number=d;}

            }
            else{
                scanf("%d %d %d %d",&a,&b,&c,&d);
            }
        }

        if(found==0){
            printf("Case #%d: Volunteer cheated!\n",i);
        }
        else{
                if(found==1){
                   printf("Case #%d: %d\n",i,number);
                }
                else{
                    printf("Case #%d: Bad magician!\n",i);
                }

        }


    }
    return 0;
}


