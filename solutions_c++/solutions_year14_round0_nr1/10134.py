#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int a,r1,r2,A[100][100],B[100][100],C[100],D[100];
    scanf("%d",&a);
    int m=0;
    for(int i1=1;i1<=a;i1++)
    {
        scanf("%d",&r1);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {

                scanf("%d",&A[j][k]);
                if(j+1==r1)
                {
                    C[k]=A[j][k];
                }
            }

        }
        scanf("%d",&r2);
        for(int p=0;p<4;p++)
        {
            for(int q=0;q<4;q++)
            {


                scanf("%d",&B[p][q]);
                if(p+1==r2)
                {
                    D[q]=B[p][q];
                }
            }

        }
        int f1=0;
        int f2=0;
        int x=0;
        int F[100];
        for(int i=0;i<4;i++)
        {

            for(int j=0;j<4;j++)
            {
                if(C[i]==D[j])
                {
                    f1++;
                    if(f1==1)
                    {
                        F[x]=C[i];
                    }
                }
                else if(C[i]!=D[j])
                {
                    f2++;

                }

            }
        }
        if(f1==1) printf("Case #%d: %d\n",++m,F[x]);
        else if(f1>1) printf("Case #%d: Bad magician!\n",++m);
        else if(f2==16) printf("Case #%d: Volunteer cheated!\n",++m);

    }
}
