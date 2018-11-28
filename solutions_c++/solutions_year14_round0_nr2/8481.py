#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t;
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    input>>t;
    int i=0;
    double c,f,x;
    double ini=2;
    double t1,t2,temp;
    output.precision(7);
    output.setf(ios::fixed);
    output.setf(ios::showpoint);
    for(i=0;i<t;++i)
    {
        input>>c;
        input>>f;
        input>>x;
        temp=0;
        ini=2;
        t1=0;
        t2=0;
        //cout<<ini;
        output<<"Case #"<<i+1<<": ";
        while(1)
        {
            t1=temp+c/ini+x/(ini+f);
            //cout<<"t1="<<t1<<endl;
            t2=temp+x/ini;
            //cout<<"t2="<<t2<<endl;
            if(t1<t2)
            {
                temp=temp+c/ini;
                //cout<<"temp="<<temp<<endl;
                ini=ini+f;
            }
            else
            {
                temp=t2;
                //cout<<"temp="<<temp<<endl;
                output<<temp<<"\n";
                break;
            }

        }

    }
    return 0;
}
