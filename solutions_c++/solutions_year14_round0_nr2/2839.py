#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    int t,i,j=1;
    double c,f,x,s,t1,t2,n;
    ifstream fin;
    ofstream fout;
    fin.open("abc.in");
    fout.open("out.out");
    fin>>t;
    while(t--)
    {
        fin>>c>>f>>x;
        if(x<=c)
            s=x/2;
        else
        { 
            i=1;
            n=0;
            while(1)
            {
                t1=x/(2+(f*(i-1)))+n;
                t2=c/(2+(f*(i-1)))+x/(f*i+2)+n;
                n+=c/(2+(f*(i-1)));
                if(t1<t2)
                    break;
                i++;
            }
            s=t1;
        }
        fout<<"Case #"<<j<<": ";
        fout<<std::fixed<<std::setprecision(7)<<s;
        fout<<endl;
        j++;
    }
    fin.close();
    fout.close();
    return 0;
}
            
