#include<iostream>
using namespace std;

int main(void)
{
freopen("input.txt","r",stdin);
freopen("output3.txt","w",stdout);
int tc,a,b,t=1;
int count;
scanf("%d",&tc);
while(t<=tc)
{           count=0;
            scanf("%d %d",&a,&b);
            for(int i=a;i<=b;i++)
            if(i==1||i==4||i==9||i==121||i==484)
            count++;
            cout<<"Case #"<<t<<": "<<count<<endl;
   t++;     
}
    
    
return 0;
}
