#include<iostream>

using namespace std;

int main()
{
    long t,sp,req,i,smax;
    char  str[1005];

    cin>>t;
long test=0;
    while(t--)
    {
        test++;
        cin>>smax;
        cin>>str;
        req=0;

        sp=str[0]-'0';
        //cout<<sp<<endl;
        for(i=1;str[i]!='\0';++i)
        {

            if(sp>=i)
                sp=sp+str[i]-'0';
            else
            {
                req+=(i-sp);
                sp+=(i-sp+str[i]-'0');

            }
            //cout<<sp<<" "<<req<<endl;

           // cout<<sp<<endl;
        }

        cout<<"Case #"<<test<<": "<<req<<endl;

    }
    return 0;
}
