#include <iostream>
#include<string>
using namespace std;


int main()
{
    int t,si,flip,count=0,flag;
  string c;

    cin>>t;
    while(t--)
    {
        count++;
        flip=0;
        flag=0;
        cin>>c;

            si=c.size();
            for(int i=0;i<si-1;i++)
         {

             if(c[i]=='-'&&c[i+1]=='+'&&flag==0)
                {
                  flip=flip+1;

                }
                else if(c[i]=='+'&&c[i+1]=='-')
                  {

                    flip=flip+2;
                    flag=1;
                  }
            }
            if(flip==0)
            {
                if (c[si-1]=='-')
                    flip=1;
            }
            cout<<"Case #"<<count<<": "<<flip<<"\n";





    }

}
