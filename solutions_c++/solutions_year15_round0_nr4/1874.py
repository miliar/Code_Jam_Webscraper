#include<iostream>
#include<fstream>

using namespace std ;

int main()
{
    ofstream fo ;
    fo.open("output.txt");
    ifstream fi;
    fi.open("input.in");
    int T, X, C, R, temp ;
    fi>>T ;
    for(int i=0;i<T;++i)
    {
        fi>>X>>R>>C ;
        if(R<C)
        {
            temp=R ;
            R=C ;
            C=temp ;
        }

        if(X>R)
            fo<<"Case #"<<i+1<<": Richard"<<endl ;
        else if(X==R)
        {
            if(C<=X-2)
                fo<<"Case #"<<i+1<<": Richard"<<endl ;
            else
                fo<<"Case #"<<i+1<<": Gabriel"<<endl ;
        }
        else
        {
            if(R*C%X==0)
                fo<<"Case #"<<i+1<<": Gabriel"<<endl ;
            else
                fo<<"Case #"<<i+1<<": Richard"<<endl ;
        }
    }
    fo.close();
    fi.close();
    return 0 ;
}
