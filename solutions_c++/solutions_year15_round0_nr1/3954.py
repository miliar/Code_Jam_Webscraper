#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream out("A-large.out");
    ifstream in("A-large.in");

    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
        int S_max=0;
        in>>S_max;
        char buf[1002];
        in>>buf;
        int iout=0;
        int already=0;
        for(int j=0;j<S_max+1;j++)
        {
            if(already<j)
            {
                //printf("need %d, we have %d\n",j,already);
                iout+=j-already;
                already=j;
            }
            already+=int(buf[j]-'0');
        }
        out<<"Case #"<<i+1<<": "<<iout<<"\n";
    }
    in.close();
    out.close();
    return 0;
}
