#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    long long int T,n,a,i,b;
    long long int ans;
    ifstream in;
    in.open("A-large.in");
    in>>T;
    ofstream out;
    out.open("out.txt");
    for(int t=1; t<=T; t++)
    {
        in>>n;
        ans =0;
        out<<"Case #"<<t<<": ";
        if(n==0)
        {
            out<<"INSOMNIA"<<endl;
        }
        else
        {
            i = 1;
            while(ans!=1023)
            {
                a = n*i;
                i++;
                while(a>0)
                {
                    b = a%10;
                    a = a/10;
                    ans = ans|(1<<b);
                }
            }
            out<<(i-1)*n<<endl;
        }
    }
    in.close();
    out.close();
    return 0;
}
