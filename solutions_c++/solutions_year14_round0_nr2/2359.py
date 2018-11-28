#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream fin ("B-large.in",ios::in);
    ofstream fout;
    fout.open ("B-large.txt");
    int t,n=1;
    fin>>t;
    double c,f,x,c1,p,q,r,s;
    fout.precision(7);
    fout.setf( ios::fixed, ios::floatfield );
    while(n<=t)
    {
        c1=2;p=0;q=0;
        fin>>c>>f>>x;
        s=r=x/(c1);
        while(true)
        {
            p=c/c1;
            q=q+p;
            r=x/(c1+f);
            if(q+r<s)
                s=q+r;
            else
            {
                fout<<"Case #"<<n<<": "<<s<<endl;
                break;
            }
            c1=c1+f;

        }
        n++;
    }
    return 0;
}
