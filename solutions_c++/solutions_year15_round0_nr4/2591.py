#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("input.txt", ios::in);
    ofstream output("output.txt", ios::out | ios::trunc);

    if(input && output)
    {
        int nbTest;

        input >> nbTest;

        cout << "nombre de tests : " << nbTest << endl;

        for(int i(0); i < nbTest; i++)
        {
            int x, r, c;
            input >> x;
            input >> r;
            input >> c;

            bool rep(true);
/*
            if(x < 7)
            {/*
                if((r*c)%x != 0)
                    rep = false;
                if(x == 1)
                    if(r<1 || c<1)
                        rep =false;
                else if(x == 2)
                    if((r<2 || c<1) && (r<1 || c<2))
                        rep =false;
                else if(x == 3)
                    if((r<3 || c<2) && (r<2 || c<3))
                        rep =false;
                else if(x == 4)
                    if((r<4 || c<2) && (r<2 || c<4))
                        rep =false;
                else if(x == 5)
                    if((r<3 || c<5) && (r<5 || c<3))
                        rep =false;
                else
                    if((r<4 || c<6) && (r<6 || c<4))
                        rep =false;*//*

                if(x == 1)
                    rep = r>=1 && c>=1;
                else if(x == 2)
                    rep = (r>=2 && c>=1) || (r>=1 && c>=2);
                else if(x == 3)
                    rep = (r>=3 && c>=2) || (r>=2 && c>=3);
                else if(x == 4)
                    rep = (r>=4 && c>=2) || (r>=2 && c>=4);
                else if(x == 5)
                    rep = (r>=5 && c>=3) || (r>=3 && c>=5);
                else if(x == 6)
                    rep = (r>=6 && c>=4) || (r>=4 && c>=6);

                if((r*c)%x != 0)
                    rep = false;
            }
            else
                rep = false;*/

            ///SMALL

            if(x < 5)
            {
                if(x == 1)
                    rep = true;
                else if(x == 2)
                    rep = ((r*c)%2) == 0;
                else if(x == 3)
                {
                    rep = ((r*c)%3) == 0;
                    if(rep)
                        rep = (r>=3 && c>=2) || (r>=2 && c>=3);
                }
                else if(x == 4)
                {
                    rep = ((r*c)%4) == 0;
                    if(rep)
                        rep = (r>=4 && c>=3) || (r>=3 && c>=4);
                }
            }
            else
                rep = false;

            if(rep)
                output << "Case #" << i+1 << ": GABRIEL" << endl;
            else
                output << "Case #" << i+1 << ": RICHARD" << endl;
        }
    }
    return 0;
}
