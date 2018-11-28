#include"iostream"
#include"conio.h"
#include"fstream"
#include"string.h"
int main()
{   std::ifstream fin;
    std::ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-attempt0.out");

    int T;
    int maxshy,i,j;
    int p,f,s;
    fin>>T;
    char d;
    for(i = 0; i < T && !fin.eof(); i++)
    {   p = 0;f = 0;
        fin>>maxshy;
        d = fin.get();
        for(j=0;j<=maxshy;j++)
        {
            s = fin.get() - '0';
            if(p >= j)
            {
                p += s;
            }
            else
            {
                if(s != 0)
                {
                    f += j - p;
                    p += s + f;
                }
            }
        }


        std::cout<<"Case #"<<i+1<<": "<<f;
        fout<<"Case #"<<i+1<<": "<<f;
        if(i!=T-1)
        {   std::cout<<"\n";
            fout<<"\n";
        }

    }
    fin.close();
    fout.close();
    getch();
    return 0;
}
