#include <iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int M[1001];
int MT[1001];
int gcd(int a, int b){
    if (a<b) return gcd(b,a);
    if (a%b==0) return b;
    else return gcd(b, a%b);
}

int lcm(int a, int b){
    return ((a*b)/gcd(a,b));

}

int main()
{

    freopen("F:\\input.txt","rb",stdin);
    freopen("F:\\output.txt","wb",stdout);
    int T,B,N;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d %d",&B,&N);
        int l = 1;
        for(int j=1;j<=B;j++)
        {
            scanf("%d",&M[j]);
            MT[j] = 0;
            l = lcm(M[j],l);
        }

        int numberOfCuts = 0;
        for(int j=1;j<=B;j++)
        {
            numberOfCuts += (l/M[j]);
        }

        N = N%numberOfCuts;
        //N++;
        if(N==0)
            N = numberOfCuts;

              int cur = 0;
        bool isvalid = true;
        while(1)
        {
            for(int k=1;k<=B;k++)
           {
                if(MT[k]==0)
                {
                    MT[k] = M[k];
                    cur++;
                    if(cur==N)
                    {
                        printf("Case #%d: %d\n",i,k);
                        isvalid = false;
                        break;
                    }
                }
                MT[k]--;
            }
            if(!isvalid)
                break;
        }

    }
    return 0;
}
