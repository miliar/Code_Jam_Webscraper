#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<cstring>
#include<fstream>

using namespace std;
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

    int cases;
    in >> cases;


    for(int i = 1; i<= cases; ++i)
    {
        int maxim;
        char theString[1000];

        in >> maxim;

        in >> theString;




        int total = theString[0] - '0';


        int adaugat = 0;
        for(int j = 1; j<=maxim; ++j)
        {
            int caracter;
            caracter = theString[j] - '0';

            if(caracter != 0 && total < j)
            {
                adaugat += j - total;


                total = j + caracter;

            }
            else
            total += caracter;


        }

        out << "Case #"<<i<<": "<<adaugat<<endl;


    }
    in.close();
    out.close();
    return 0;
}
