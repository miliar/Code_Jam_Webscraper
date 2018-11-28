#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I=0;I<N;I++){
        int RN1,RN2,re;
        int LA[4],LB[4];
        scanf("%d",&RN1);
        for(int i=0;i<4;i++){
                if(RN1==i+1)scanf("%d %d %d %d",&LA[0],&LA[1],&LA[2],&LA[3]);
                else scanf("%d %d %d %d",&re,&re,&re,&re);
        }
        scanf("%d",&RN2);
        for(int i=0;i<4;i++){
                if(RN2==i+1)scanf("%d %d %d %d",&LB[0],&LB[1],&LB[2],&LB[3]);
                else scanf("%d %d %d %d",&re,&re,&re,&re);
        }
        int answer,sum=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(LA[i]==LB[j]){answer=LA[i];sum++;}
            }
        }
        printf("Case #%d: ",I+1);
        if(sum==1)printf("%d\n",answer);
        if(sum>1)printf("Bad magician!\n");
        if(sum==0)printf("Volunteer cheated!\n");
    }
    fclose(stdout);
}
