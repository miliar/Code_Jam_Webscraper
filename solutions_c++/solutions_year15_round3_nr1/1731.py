#include<iostream>
#include<fstream>

using namespace std ;

int main()
{
    int T,R,C,W ;
    ifstream fi ;
	ofstream fo ;
	fi.open("input.in") ;
	fo.open("output.txt") ;
	int c ;

	fi>>T ;
	for(int i=0;i<T;++i)
    {
        c=0 ;
        fi>>R>>C>>W ;
        if(W==1)
            c = R*C ;
        else
        {
            c = (int)((R*C)/W) + W-1 ;
            if((R*C)%W!=0)
                c = c + 1 ;
        }
        fo<<"Case #"<<i+1<<": "<<c<<endl ;
    }
	fi.close();
	fo.close();
	return 0;
}
