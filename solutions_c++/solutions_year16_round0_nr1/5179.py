#include<bits/stdc++.h>

using namespace std;

set<long long int> s;

void calculate(long long int x)
{
    long long int c;
    while(x>0)
    {
        c=x%10;
        s.insert(c);
        x=x/10;
    }
}

main()
{
    long long int T,cs,x,j,m;

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>T;

    for(cs=1;cs<=T;cs++)
    {
        cin>>x;
        j=1;
        if(x==0)
            cout<<"Case #"<<cs<<": INSOMNIA"<<endl;

        else
            while(1)
            {

                m=x*j;

                calculate(m);

                if(s.size()==10)
                {
                    cout<<"Case #"<<cs<<": "<<m<<endl;
                    break;
                }

                j++;

            }
        s.clear();
    }
    return 0;
}
