#include <iostream>
#include <fstream>

using namespace std;




bool m[12];
int c;
void coun(int b)
{
    int a=b;
    int r;
    while(true)
    {
        r=a%10;
        if(m[r]==0)c++;
        m[r]=1;
        a=a/10;
        if(a==0)break;
    }
}


int main()
{
    int t,n,ns;

    ifstream in("in.txt");
    ofstream out("out.txt");
    in>>t;
    for(int p=1;p<=t;p++)
    {
        in>>n;
        ns=n;
        if(n==0)
            out<<"Case #"<<p<<": INSOMNIA"<<endl;
        else
            {
                coun(n);
                while(c!=10)
                {
                    n+=ns;
                    coun(n);;
                }
                out<<"Case #"<<p<<": "<<n<<endl;
                for(int k=0;k<=11;k++)m[k]=0;
                c=0;
            }
    }
    return 0;
}
