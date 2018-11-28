#include<string>
#include<fstream>
#include<cstdlib>
using namespace std;

ifstream f ("A-large.in");
ofstream g ("output.txt");

int main()
{
        unsigned int Cases,MaxShyness,BonusGuests,StandingGuests,Aux,i,j;
        string Levels;

        f>>Cases;
        for(i=1;i<=Cases;i++)
        {
            f>>MaxShyness;
            f>>Levels;
            BonusGuests=0;
            StandingGuests=Levels[0]-'0';

            for(j=1;j<Levels.size();j++)
            {
                Aux=Levels[j]-'0';
                if(j>StandingGuests)
                {
                    BonusGuests=BonusGuests+(j-StandingGuests);
                    StandingGuests=StandingGuests+Aux+(j-StandingGuests);
                }
                else
                    StandingGuests=StandingGuests+Aux;
            }
            g<<"Case #"<<i<<": "<<BonusGuests<<"\n";
        }

        f.close();
        g.close();
}

