//counting sheep
#include<iostream>
int main()
{   using namespace std;
    long unsigned int num;
    unsigned int t,n[100],digit[10]={0,0,0,0,0,0,0,0,0,0},x,i;
        cin>>t;
    for(i=0;i<t;i++)
        cin>>n[i];
    i=0;
    while(i<t)
        {   if(n[i]==0)
                cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
            else
            {
            for(int a=1;;a++)
            {
                num=n[i]*a;
                 while(num)
                 {
                     x=num%10;
                     num=num/10;
                     digit[x]=1;
                 }
                 if(digit[0]+digit[1]+digit[2]+digit[3]+digit[4]+digit[5]+digit[6]+digit[7]+digit[8]+digit[9]==10)
                {
                     cout<<"Case #"<<i+1<<": "<<n[i]*a<<"\n";
                     break;
                }
            }
            }
            i++;
            for(int j=0;j<10;j++)
            {
               digit[j]=0;

            }
        }
return 0;
}
