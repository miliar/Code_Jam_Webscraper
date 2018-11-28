#include <bits/stdc++.h>
#define ull unsigned long long int
using namespace std;

int main()
{
    int t;
    cin>>t;
    ull x,y,c;
    int cs=1,remaining;
    bool a[10];
    while(t--)
    {
        remaining=10;
        cout<<"Case #"<<cs<<": ";
        cs++;
        cin>>x;
        y=x;
        if(x==0)
            cout<<"INSOMNIA"<<endl;

        else
        {
            memset(a,false,10*sizeof(bool));
            c=1;
            while(remaining>0)
            {
                x=y*c;
                 while(x!=0)
                {

                    if(a[x%10]==false)
                    {
                        a[x%10]=true;
                        remaining--;

                        if(remaining<=0)
                        {
                            cout<<y*c<<endl;
                            break;
                        }
                    }
                    x=x/10;
                }
                c++;

            }




        }

    }

}
