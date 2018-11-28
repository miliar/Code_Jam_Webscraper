#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
   // freopen("A-large.in" , "r" , stdin );
     //freopen("out1.txt","w",stdout);
    int cou = 0;
    int t;
    int smax;
    int cas=1;
    int res=0;
    int a =0;
    int b =1;
    string smaxx;
    cin>>t;

    while (t>cou)
    {
        cin>>smax;
        if ( smax >=0 && smax <=1000)
        {
        cin>>smaxx;
        if ( smaxx.length()==smax+1)
        {

            int arr[smaxx.length()];
            for ( int i = 0 ; i < smaxx.length() ; i++)
            {
                arr[i]= smaxx[i]-'0';
            }
            for (int i = 0 ; i <smaxx.length() ; i++)
            {
                a +=arr[i];
                if ( a+res<b )
                {
                    res++;
                }
                b++;
            }
        cout<<"Case #"<<cas<<": "<<res<<endl;
        }
        }
        cas++;
        cou++;
        res =0;
        a = 0;
        b = 1;
    }
    return 0;

}
