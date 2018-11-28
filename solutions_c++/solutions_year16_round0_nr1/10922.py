#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int test,count=1;
    cin>>test;
    while(test--)
    {
        int num,div,rem=0,i=2,x=0,y;
        cin>>num;
        if(num==0)
        {
            cout<<"Case #"<<count<<": "<<"Insomnia"<<endl;
        }
        else
        {
            y=num;
            int a[10]={10,10,10,10,10,10,10,10,10,10};
            int b[10]={0,1,2,3,4,5,6,7,8,9};
            while(x!=10)
            {
                if(a[0]!=b[0] || a[1]!=b[1] || a[2]!=b[2] || a[3]!=b[3] || a[4]!=b[4] || a[5]!=b[5] || a[6]!=b[6] || a[7]!=b[7] || a[8]!=b[8] || a[9]!=b[9])
                {
                    div=y;
                    while(div!=0)
                    {
                        rem=div%10;
                        a[rem]=rem;
                        div=div/10;
                    }
                    y=i*num;
                    i++;
                }
                else
                {
                    x=10;
                }
            }
            cout<<"Case #"<<count<<": "<<y-num<<endl;
        }
        count++;
    }
    return 0;
}
