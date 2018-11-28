#include<iostream>
using namespace std;
int main()
{
    int T;
    int r,t,count,sum,a=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&r,&t);
        count=0;
        while(t>=0)
        {
            sum=(2*r)+1;
            t-= sum;
            r+= 2;
            ++count;
        }
        a++;
        printf("Case #%d: %d\n",a,count-1);
    }
    return 0;    
}            
