#include <iostream>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

class FairSq
{
public:

    FairSq() :
        m_infileName(""),
        m_outfileName(""),
        m_T(0),
        m_A(0.0),
        m_B(0.0),
        m_numString("")
    {
    }

    FairSq( string infileName, string outfileName ) :
        m_infileName(infileName),
        m_outfileName(outfileName),
        m_T(0),
        m_A(0.0),
        m_B(0.0),
        m_numString("")
    {
    }

    ~FairSq()
    {
    }

    void setInfile( string infileName )
    {
        m_infileName = infileName;
        m_T = 0;
        m_A = 0.0;
        m_B = 0.0;
        m_numString = "";
    }

    void setOutfile( string outfileName )
    {
        m_outfileName = outfileName;
        m_T = 0;
        m_A = 0.0;
        m_B = 0.0;
        m_numString = "";
    }

    static long double PerfectSquare( long double num )
    {
        long double retVal = -1.0;

        long double sr = sqrt( num );
        long double fl = floor( sr );

        if ( (fl * fl) == num )
        {
            retVal = fl;
        }

        return retVal;
    }

    static bool IsPalindrome( long double num )
    {
        bool retVal = false;
        string strRep = to_string( num );

        string intRep = strRep.substr( 0, strRep.find( '.' ) );
        string revIntRep = intRep;

        reverse( revIntRep.begin(),revIntRep.end() );

        if (intRep.compare(revIntRep) == 0 )
        {
            retVal = true;
        }

        return retVal;
    }

    void ParseFileAndProcessAlgorithm()
    {
         ifstream inputFile( m_infileName.c_str() );
         ofstream outputFile( m_outfileName.c_str() );

         string line;
         getline( inputFile, line );
         stringstream ss(line);
         ss >> m_T;

         for ( unsigned i = 0; i < m_T; i++ )
         {
             unsigned count;
             count = 0;

             getline( inputFile, line );
             stringstream ss(line);
             ss >> m_A >> m_B;

             for ( long double i = m_A; i <= m_B; i += 1.0 )
             {
                 if ( IsPalindrome( i ) )
                 {
                     long double perSq = PerfectSquare( i );
                     if ( perSq > 0.0 )
                     {
                         if (IsPalindrome( perSq ) )
                         {
                             count++;
                         }
                     }
                 }
             }

             // cout << "Case #" << i + 1 << ": " << count << endl;
             outputFile << "Case #" << i + 1 << ": " << count << endl;
         }
    }

private:

    string m_infileName;
    string m_outfileName;

    unsigned m_T;
    long double m_A;
    long double m_B;

    string m_numString;
};


int main(int argc, char *argv[])
{
    string inputFN = ".\\A-small-practice.in";
    string outputFN = ".\\out.txt";

    if ( argc == 2 )
    {
        inputFN = argv[1];
    }
    else if ( argc == 3 )
    {
        inputFN = argv[1];
        outputFN = argv[2];
    }

    FairSq fs( inputFN, outputFN );
    fs.ParseFileAndProcessAlgorithm();

    return 0;
}

