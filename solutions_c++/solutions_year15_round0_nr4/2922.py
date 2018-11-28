#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("D-small-attempt1.in");
    ofstream fout("c.txt");
    int t, i, j, x, r, c;
    if(fin)
    {
        fin>>t;
        for(i=1; i<=t; i++)
        {
            fin>>x>>r>>c;
            //cout<<i<<". "<<x<<" "<<r<<" "<<c<<endl;
            if(x==1)
            {
                fout<<"Case #"<<i<<": GABRIEL"<<endl;
            }
            else if(x==2)
            {
                if((r*c)%2==0)
                    fout<<"Case #"<<i<<": GABRIEL"<<endl;
                else
                    fout<<"Case #"<<i<<": RICHARD"<<endl;
            }
            else if(x==3)
            {
                if((r==3 and c>1) or (c==3 and r>1))
                    fout<<"Case #"<<i<<": GABRIEL"<<endl;
                else
                    fout<<"Case #"<<i<<": RICHARD"<<endl;
            }
            else if(x==4)
            {
                if((r==4 and c==3) or (r==4 and c==4) or (r==3 and c==4))
                    fout<<"Case #"<<i<<": GABRIEL"<<endl;
                else
                    fout<<"Case #"<<i<<": RICHARD"<<endl;
            }
        }
    }
    return 0;
}
