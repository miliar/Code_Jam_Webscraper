#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    int i=0;
    int A[t];
    while(i<t)
    {
        int a;
        string p;
        scanf("%d",&a);
        cin>>p;
        int j=0;
        int num=0;
            int count=0;
            num=num+p[0]-48;
        for(j=1;j<=a;j++)
        {
            if(j<=num)
                num=num+p[j]-48;
                else
                {
                    count=count+j-num;
                    num=j+p[j]-48;
                }


        }
A[i]=count;







        i++;
    }
    for(i=1;i<=t;i++)
        cout<<"Case #"<<i<<": "<<A[i-1]<<endl;


}