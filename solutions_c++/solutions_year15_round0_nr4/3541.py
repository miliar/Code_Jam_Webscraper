#include"iostream"
#include <fstream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    ofstream myfile;
    myfile.open ("output.txt");
    for(int i=1;i<=t;i++)
    {



        int x,r,c;
        cin>>x>>r>>c;
        int cc=0;
        if((r*c)%x==0)
        {
            if(x==1 || x==2)
            {

            }
            else if(r*c==x)
            {
                cc=1;
            }
            else
            {
                if(r==c && 2*r-1<=x)
                    cc=1;
                else if(r>c && 2*c-1<x)
                    cc=1;
                else if(2*r-1<x)
                    cc=1;
            }
        }
        else
        {
            cc=1;
        }
        if(cc==0)
        {
            //cout<<"Case #"<<i<<": GABRIEL"<<endl;
            myfile <<"Case #"<<i<<": GABRIEL"<<endl;
        }
        else
        {
            //cout<<"Case #"<<i<<": RICHARD"<<endl;
            myfile <<"Case #"<<i<<": RICHARD"<<endl;
        }
    }
    myfile.close();
    return 0;
}
