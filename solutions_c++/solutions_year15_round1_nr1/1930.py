#include <iostream>
#include <fstream>
using namespace std;

int m[10010]={0};
int main()
{
    ifstream f1("A-large.in");
    ofstream f2("2.out");
    int T;
    f1>>T;
    int N;
    int y,z,max;
    for(int i=0;i<T;++i)
    {
        f1>>N;
        y=0;z=0;
        max=0;
        for(int j=0;j<N;++j)
        {
            f1>>m[j];
        }
        for(int j=0;j<N-1;++j)
        {
            if(m[j]>m[j+1])
            {
                y+=m[j]-m[j+1];
                if(max<(m[j]-m[j+1]))
                {
                    max=m[j]-m[j+1];
                }
            }
        }
        for(int j=0;j<N-1;++j)
        {
            if(m[j]>max){z+=max;}
            else{z+=m[j];}
        }
        f2<<"Case #"<<i+1<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
