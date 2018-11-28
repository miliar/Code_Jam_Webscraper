# include<iostream>
# include <stdio.h>
# include <iomanip>

using namespace std;

int main()
{

    double c,f,x,p,r,q,i,t,z=2.0,k,s,w=0;
    int a,u;
    cin>>t;

    for(u=0;u<t;u++)
    {
                    z=2.0000000;
        cin>>c>>f>>x;

        if(c>x)
        {
            k=x/z;
            cout<<"Case #"<<u+1<<": "<<setprecision(10)<<k;
            if(w<t-1)
            {
              w++;
              cout<<endl;
            }

        }
        else
        {
            s=0;
            a=1;
            i=x/z;
            while(a)
            {

                p=c/z;
                s=s+p;
                z=z+f;
                q=x/z;
                r=s+q;
                if(i>r)
                {

                    i=r;
                }
                else
                {
                    a=0;
                }
            }
            cout<<"Case #"<<u+1<<": "<<setprecision(10)<<i;
            if(w<t-1)
            {
                w++;
                cout<<endl;
            }
        }

    }


}

