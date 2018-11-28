#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t,sx,i,sum=0,sum1=0;
    string ch;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>sx;
        for(i=0;i<=sx;i++)
        {
            cin>>ch[i];
        }
        sum=sum1=0;
        if(ch[0]==48) {sum++; sum1++;}
        else sum1+=ch[0]-48;
        for(i=1;i<=sx;i++)
        {
            if(sum1<i){ sum++; sum1++; }
            sum1+=ch[i]-48;
        }
        printf("Case #%d: %d\n",j,sum);
    }
    return 0;
}