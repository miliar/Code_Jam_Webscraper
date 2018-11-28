#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;

typedef double lf;

const lf EPSILON = 1e-8;

inline bool lt(const lf& a, const lf& b) { return b-a > EPSILON; }

void obradi(int iteration, double C, double F, double X)
{

    ofstream outfile;
    outfile.open("outfile.txt",ios::in | ios::out | ios::app);

    double number_of_cookies = 2.0;

    double prvi = X / number_of_cookies;

    double drugi = C / number_of_cookies;

    while(true)
    {

        double dodatak = X / (number_of_cookies + F) ;
        if(lt(prvi, drugi + dodatak))
        {
            break;
        }
        else
        {

            prvi = drugi + dodatak;
            number_of_cookies += F;
            drugi += (C / number_of_cookies);
        }
    }

    outfile<<"Case #"<<iteration<<": ";
    outfile<<fixed;
    outfile<<setprecision(7);
    outfile<<prvi<<endl;
}

void ucitaj()
{
    ifstream infile("B.in");
    string line;
    getline(infile, line);
    int test_counter = atoi(line.c_str());

    for(int i=1; i<=test_counter; ++i)
    {
        getline(infile, line);
        vector<string> vektor(3);
        string temp;
        istringstream iss;
        iss.str(line);

        int temp_count = 0;
        while(getline(iss, temp, ' '))
        {
            vektor[temp_count] = temp;
            temp_count ++;
        }
        obradi(i, atof(vektor[0].c_str()), atof(vektor[1].c_str()), atof(vektor[2].c_str()));
    }
}

int main()
{
    ucitaj();

}
