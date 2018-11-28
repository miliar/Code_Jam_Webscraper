#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
bool ispalin(int,int);
bool ispalin(int num,int len)
{
    int arr[4];
    for(int j=0;j<len;j++)
    {
        arr[j]=num%10;
        num=num/10;
    }
    for(int j=0;j<len/2;j++)
    {
        if(arr[j]!=arr[len-1-j])
        return false;
    }

    return true;
}
int length(int num)
{
    int len=0;
    while(num>0)
            {
                len++;
                num=num/10;
            }
    return len;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int testcase,sq,temp,len=0;
    int a,b,i,k,count=0,tempa,tempb;
    float fa,fb;
    cin>>testcase;
    temp=testcase;
    while(testcase-->0)
    {
        cin>>a;
        cin>>b;
        count=0;
        fa=sqrt(a);
        tempb=sqrt(b);
        tempa=fa+0.999999;

        //cout<<tempa<<" "<<tempb;
        //getchar();
        for(i=tempa;i<=tempb;i++)
        {

            len=length(i);
            if(ispalin(i,len))
            {
                sq=i*i;
                len=length(sq);
                if(ispalin(sq,len))
                count++;
            }

            //getchar();
        }
        cout<<"Case #"<<temp-testcase<<": "<<count<<endl;
    }
    return 0;
}
