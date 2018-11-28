#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    long long a,b,c,d,e,f,g,h,t;
    vector<long long> v, vec;
    vector<long long>::iterator i, it;
    ofstream out("B.txt");

    for(b=1; b<=31622777; b++)
    {
        e=b;
        f=0;
        while(e>0)
        {
            f*=10;
            f+=(e%10);
            e=(e/10);
        }
        if(b==f)
        {
            g=(b*b);
            e=g;
            f=0;
            while(e>0)
            {
                f*=10;
                f+=(e%10);
                e=(e/10);
            }
            if(f==g){v.push_back(g);}
        }

    }

    cin>>t;
    while(t>0)
    {
        cin>>a>>d;
        for(i=v.begin(), h=0; i!=v.end(); i++)
        {
            if(*i>d){break;}
            if(*i>=a){h++;}
        }
        vec.push_back(h);
        t--;
    }

    for(it=vec.begin(), b=1; it!=vec.end(); it++, b++)
    {
        out<<"Case #"<<b<<": "<<*it<<endl;
    }

    return 0;
}
