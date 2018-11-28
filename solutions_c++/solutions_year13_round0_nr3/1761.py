    #include<iostream>
#include<stdio.h>
using namespace std;


int main()
{
    int l=0;
    FILE *fp;
    fp=fopen("output.txt","w");
    long long int a[]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
    for(int i=0;i<39;i++)
    {
        a[i]=a[i]*a[i];
    }


    int t;
    scanf("%d",&t);
    while(t--)
    {l++;
        long long int a1,b;
        scanf("%lld%lld",&a1,&b);
        int count1=0;
        for(int i=0;i<39;i++)
        {
            if(a1<=a[i]&&b>=a[i])
            {
                count1++;
            }
        }
        fprintf(fp,"Case #%d: %d\n",l,count1);
    }


    return 0;
}
