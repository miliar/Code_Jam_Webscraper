#include <iostream>
using namespace std;
 
int main()
{
    int test=0,p=1;
    cin>>test;
    int a=0,b=0,c=0;
    for(p=1;p<=test;p++)
    {
        cin>>a>>b>>c;
        int sum=0;
        sum=b*c;
        if(sum%a==0)
        {
            if((a-1)>b || (a-1)>c)
            {
                cout<<"Case #"<<p<<": RICHARD"<<endl;
            }
            else
            {
                cout<<"Case #"<<p<<": GABRIEL"<<endl;
            }
        }
        else
        {
            cout<<"Case #"<<p<<": RICHARD"<<endl;
        }
    }
    return 0;
}