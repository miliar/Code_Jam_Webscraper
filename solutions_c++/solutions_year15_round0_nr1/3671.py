#include <iostream>
#include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");

//#define in cin
//#define out cout

int main()
{
    int t;
    in>>t;
    for(int i=0;i<t;i++)
    {
        int m;
        in>>m;
        int p=0;
        int f=0;
        for(int j=0;j<m+1;j++)
        {
            char c;
            in>>c;
            int n=c-'0';
            if(p>=j)p+=n;
            else{f+=j-p;p=j+n;}
        }
        out<<"Case #"<<i+1<<": "<<f<<endl;
    }
    return 0;
}
