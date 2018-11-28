#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cases=0;
    scanf("%d",&T);
    while(T--){

        int X,R,C;
        scanf("%d%d%d",&X,&R,&C);

        int ans=0;
        switch(X)
        {
        case 1:
                ans=2;
                break;
        case 2:
                if(R%2 == 0 || C %2 == 0) ans=2;
                else ans=1;
                break;
        case 3:
                if(R%3 == 0 || C%3 == 0)
                {
                    if((R==3 && C==1) ||(R==1 &&C==3)){
                        ans=1;
                    }
                    else
                        ans=2;
                }
                else ans=1;
                break;
        case 4:
                if((R==4 && C == 3) ||(R==4 && C==4) ||(R==3 && C==4))
                {
                    ans=2;
                }
                else
                    ans=1;
                break;

        }

        printf("Case #%d: %s\n",++cases,ans==1? "RICHARD":"GABRIEL");

    }
    return 0;
}
