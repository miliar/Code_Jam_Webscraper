#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t,smax,i,num,j;
    string str;
    cin>>t;
    {

        for(j=1;j<=t;j++)
        {
            int standing=0,need=0;
            cin>>smax>>str;
            i=0;
            num=str[0]-'0';
            if(num>0)
            {
                standing=num; i++;
            }
            while(num==0)
            {
                i++;
                num=str[i]-'0';
            }
            for(;i<=smax;i++)
            {
              num=str[i]-'0';
              if(num && standing>=i)
                standing+=(str[i]-'0');
              else if(num)
              {
                  need+=(i-standing);
                  standing+=(str[i]-'0');
                  standing+=need;
              }

            }
cout<<"Case #"<<j<<": "<<need<<endl;

        }

    }

   return 0;
}
