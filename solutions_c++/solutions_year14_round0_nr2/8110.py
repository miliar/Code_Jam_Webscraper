#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    stringstream couta;
    int casos;
    cin>>casos;
    couta << fixed;

    for(int i=1;i<=casos;++i)
    {
        long double C, F, X,best,worst,temp,cont;
        cont = 0;
        cin>>C>>F>>X;

        worst= X/2.0;
        temp=C/2.0;
        cont+=1.0;
        best= temp + X/(cont*F+2.0);

        /*cout<<best<<" "<<worst<<endl;*/

        while(best<worst)
        {

            worst = best;
            temp+=C/(cont*F+2.0);
            cont+=1.0;
            best= temp + X/(cont*F+2.0);
            /*cout<<best<<" "<<worst<<endl;
            int lol;
            cin>>lol;*/
        }

        couta<<"Case #"<<i<<": "<<std::setprecision(7)<<worst<<endl;

        string myString = couta.str();
        std::ofstream myfile;
        myfile.open ("CookieClickerOUT.txt");
        myfile << myString;
        myfile.close();

    }



}
