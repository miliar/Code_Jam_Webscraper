#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{

    ifstream fin("A-small-attempt3.in");
    ofstream fout("A-large.out");
    int n;
    fin >> n;
    int k=0;
    while(n--)
    {
        ++k;
        fout << "Case #" << k <<": ";
        bool ju=0;
        int period=0;
        vector<char> v(16);
        for(int i=0; i<v.size(); ++i)
        {
            fin >> v[i];
            if(v[i]=='.')
                ++period;
        }
        int A,B;
        for(int i=0; i<v.size(); i+=4)
        {
            A=0,B=0;
            for(int j=i; j<i+4; ++j)
            {
                if(v[j]=='O')
                    ++A;
                else if(v[j]=='X')
                    ++B;
                else if(v[j]=='T')
                {
                    if(A>B)
                    {
                        ++A;
                    }
                    else
                    {
                        ++B;
                    }
                }
            }
            if(A==4)
            {
                fout << "O won" << endl;
                ju=1;
                break;
            }
            else if(B==4)
            {
                fout << "X won" << endl;
                ju=1;
                break;
            }
        }
        if(ju!=1)
        {
            for(int i=0; i<4; ++i)
            {
                A=0,B=0;
                for(int j=i; j<v.size(); j+=4)
                {
                    if(v[j]=='O')
                        ++A;
                    else if(v[j]=='X')
                        ++B;
                    else if(v[j]=='T')
                    {
                        if(A>B)
                        {
                            ++A;
                        }
                        else
                        {
                            ++B;
                        }
                    }
                }
                if(A==4)
                {
                    fout << "O won" << endl;
                    ju=1;
                    break;
                }
                else if(B==4)
                {
                    fout << "X won" << endl;
                    ju=1;
                    break;
                }
            }
        }
        int x[4]= {0,5,10,15},y[4]= {3,6,9,12};
        if(ju!=1)
        {
            A=0,B=0;

            for(int i=0; i<4; ++i)
            {
                if(v[x[i]]=='O')
                    ++A;
                else if(v[x[i]]=='X')
                    ++B;
                else if(v[x[i]]=='T')
                {
                    if(A>B)
                    {
                        ++A;
                    }
                    else
                    {
                        ++B;
                    }
                }
            }
            if(A==4)
            {
                fout << "O won" << endl;
                ju=1;

            }
            else if(B==4)
            {
                fout << "X won" << endl;
                ju=1;

            }
        }
        if(ju!=1)
        {
            A=0,B=0;
            for(int i=0; i<4; ++i)
            {
                if(v[y[i]]=='O')
                    ++A;
                else if(v[y[i]]=='X')
                    ++B;
                else if(v[y[i]]=='T')
                {
                    if(A>B)
                    {
                        ++A;
                    }
                    else
                    {
                        ++B;
                    }
                }
            }
            if(A==4)
            {
                fout << "O won" << endl;
                ju=1;
            }
            else if(B==4)
            {
                fout << "X won" << endl;
                ju=1;
            }
        }
        if(ju!=1)
        {
            if(period>0)
            {
                fout << "Game has not completed" << endl;
                ju=1;
            }
        }
        if(ju!=1)
            fout << "Draw" << endl;
    }
    return 0;
}
