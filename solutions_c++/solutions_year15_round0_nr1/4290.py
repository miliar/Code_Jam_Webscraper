#include<iostream>
using namespace std;

int main()
{
    char str[1005];
    int t,i,n,j,a,b,c;
    cin>>t;
    for(n=0;n<t;n++)
    {
     //   memset(str)
        cin>>c>>str;
        a=b=0;
        for(i=0;i<=c;i++)
        {

            if (str[i] == 48) continue;
            if(i<=a)
            {
                a+=(str[i]-48);
                continue;
            }

            j=i-a;
            b+=j;
            a+=j+(str[i]-48);

        }
        cout<<"case #"<<n+1<<": "<<b<<endl;
    }
}
