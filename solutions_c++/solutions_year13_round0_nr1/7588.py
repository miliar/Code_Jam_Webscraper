#include<iostream>
using namespace std;
#include<stdio.h>
int main ()
{
    int tc,i,j,rowSum,colSum[4];
    char a,b,c,d,waste;
    scanf("%d",&tc);
    scanf("%c",&waste);
    for(int t=1;t<=tc;t++)
    {
        int result=0,incomplete=0;
        int d1=0,d2=0;
        for(i=0;i<4;i++) 
            colSum[i]=0;
        for(i=0;i<4;i++) 
        {
            rowSum=0;
            scanf ("%c %c %c %c",&a,&b,&c,&d);
            if (result == 0 )
            {
                a=='X'?a=1:a=='O'?a=-1:a=='T'?a=0:a=100;
                colSum[0]+=a;
                b=='X'?b=1:b=='O'?b=-1:b=='T'?b=0:b=100;
                colSum[1]+=b;
                c=='X'?c=1:c=='O'?c=-1:c=='T'?c=0:c=100;
                colSum[2]+=c;
                d=='X'?d=1:d=='O'?d=-1:d=='T'?d=0:d=100;
                colSum[3]+=d;
                rowSum=a+b+c+d;
                i==0?d1+=a:i==1?d1+=b:i==2?d1+=c:d1+=d;
                i==0?d2+=d:i==1?d2+=c:i==2?d2+=b:d2+=a;
                if (rowSum == 4 || rowSum == 3)
                    result=1;
                else if (rowSum == -3 || rowSum== -4)
                    result=-1;
                else if (rowSum > 4) 
                    incomplete=1;
                }
                scanf("%c",&waste);
            }
            for(i=0;i<4;i++) 
            {
                if (colSum[i] == 4 || colSum[i] == 3)
                    result=1;
                else if (colSum[i] == -3 || colSum[i]== -4)
                    result=-1;
                else if (colSum[i] > 4) 
                    incomplete=1;
            }
        if (d1 == 4 || d1 == 3)
            result=1;
        else if (d1 == -3 || d1== -4)
            result=-1;
        else if (d1 > 4) 
            incomplete=1;    
        if (d2 == 4 || d2 == 3)
            result=1;
        else if (d2 == -3 || d2== -4)
            result=-1;
        else if (d2 > 4) 
            incomplete=1;
        if (result == 1)
        printf("Case #%d: X won\n",t);
        else if (result == -1)
        printf("Case #%d: O won\n",t);
        else if (result == 0 && incomplete == 0)
        printf("Case #%d: Draw\n",t);
        else printf("Case #%d: Game has not completed\n",t);
        scanf("%c",&waste);
    }
}
