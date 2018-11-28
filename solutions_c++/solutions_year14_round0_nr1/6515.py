#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    in.open("A-small-attempt0.in");
    ofstream out;
    out.open("out.txt");
    int T;
    in>>T;
    int a,b,c,d,e,f,g,h,n;
    int first, second, gar;
    for (int t=1; t<=T; t++)
    {
        in>>first;
        int count=0;
        for(int i=1; i<=4; i++)
        {
            if(i==first)
            {
                in>>a>>b>>c>>d;
            }
            else
            {
                in>>gar>>gar>>gar>>gar;
            }
        }
        in>>second;
        for(int i=1; i<=4; i++)
        {
            if(i==second)
            {
                in>>e>>f>>g>>h;
            }
            else
            {
                in>>gar>>gar>>gar>>gar;
            }
        }
        if(e==a || e==b || e==c || e==d)
        {
            count=count++;
            n = e;
        }
        if(f==a || f==b || f==c || f==d)
        {
            count=count++;
            n = f;
        }
        if(g==a || g==b || g==c || g==d)
        {
            count=count++;
            n = g;
        }
        if(h==a || h==b || h==c || h==d)
        {
            count=count++;
            n = h;
        }
        if(count==0)
        {
            out<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        }
        else if(count==1)
        {
            out<<"Case #"<<t<<": "<<n<<endl;
        }
        else if(count>1)
        {
            out<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
        }

    }
    in.close();
    out.close();
    return 0;
}
