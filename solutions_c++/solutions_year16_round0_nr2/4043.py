#include<bits/stdc++.h>
using namespace std;


int main()
{
    //freopen("in3.in","r",stdin);
    //freopen("out3.out","w",stdout);

    int i,j,k;
    int a,b,c;
    long long n,x,y;
    int t;
    string str,str2;

    cin>>t;

    i=1;

    while(t--)
    {
        cin>>str;
        j=0;
        x=0;

        //count initial ones
        if(str[0]=='-')
        {
            x++;

            while(j<str.length() && str[j]=='-')
            {
                j++;
            }

        }

        while(j<str.length())
        {
            //first get all the +'s
            while(j<str.length() && str[j]=='+')
            {
                j++;
            }
        
            //now, get the ones if there
            if(str[j]=='-')
            {
                x+=2;

                while(j<str.length() && str[j]=='-')
                {
                    j++;
                }

            }
        }


        cout<<"Case #"<<i<<": ";
        cout<<x;
        cout<<endl;

        i++;
    }
   
    return 0;
}
