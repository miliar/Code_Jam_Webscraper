#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream f_in;
    ofstream f_out;
    f_in.open("input.txt");
    f_out.open("output.txt", ios_base::trunc );

    string temp;
    getline(f_in, temp);
    int T = stoi(temp);
    string S;
    vector<int> res;
    string::size_type s1;

    for(int i=1; i<T+1; i++)
    {
        getline(f_in, S);

        s1 = S.find_first_of('Z'); //ZERO
        if ( !S.empty() )
        {

            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                s1 = S.find_first_of('E');
                S.erase( s1 , 1);
                S.erase( S.find_first_of('R') , 1);
                S.erase( S.find_first_of('O') , 1);
                res.push_back(0);
                s1 = S.find_first_of('Z'); //ZERO
            }
        }

        s1 = S.find_first_of('U'); //FOUR
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('F') , 1);
                S.erase( S.find_first_of('O') , 1);
                S.erase( S.find_first_of('R') , 1);
                res.push_back(4);
                s1 = S.find_first_of('U'); //FOUR
            }
        }

        s1 = S.find_first_of('X'); //SIX
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('S') , 1);
                S.erase( S.find_first_of('I') , 1);
                res.push_back(6);
                s1 = S.find_first_of('X'); //SIX
            }
        }

        s1 = S.find_first_of('G'); //EIGHT
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('E') , 1);
                S.erase( S.find_first_of('I') , 1);
                S.erase( S.find_first_of('H') , 1);
                S.erase( S.find_first_of('T') , 1);
                res.push_back(8);
                s1 = S.find_first_of('G'); //EIGHT
            }
        }

        s1 = S.find_first_of('F'); //FIVE
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('I') , 1);
                S.erase( S.find_first_of('V') , 1);
                S.erase( S.find_first_of('E') , 1);
                res.push_back(5);
                s1 = S.find_first_of('F'); //FIVE
            }
        }


        s1 = S.find_first_of('I'); //NINE
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('N') , 1);
                S.erase( S.find_first_of('N') , 1);
                S.erase( S.find_first_of('E') , 1);
                res.push_back(9);
                s1 = S.find_first_of('I'); //NINE
            }
        }

        s1 = S.find_first_of('V'); //SEVEN
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('S') , 1);
                S.erase( S.find_first_of('E') , 1);
                S.erase( S.find_first_of('E') , 1);
                S.erase( S.find_first_of('N') , 1);
                res.push_back(7);
                s1 = S.find_first_of('V'); //SEVEN
            }
        }

        s1 = S.find_first_of('R'); //THREE
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('T') , 1);
                S.erase( S.find_first_of('H') , 1);
                S.erase( S.find_first_of('E') , 1);
                S.erase( S.find_first_of('E') , 1);
                res.push_back(3);
                s1 = S.find_first_of('R'); //TWREE
            }
        }

        s1 = S.find_first_of('N'); //ONE
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('O') , 1);
                S.erase( S.find_first_of('E') , 1);
                res.push_back(1);
                s1 = S.find_first_of('N'); //ONE
            }
        }

        s1 = S.find_first_of('T'); //TWO
        if ( !S.empty() )
        {
            while( s1!=std::string::npos )
            {
                S.erase( s1 , 1);
                S.erase( S.find_first_of('W') , 1);
                S.erase( S.find_first_of('O') , 1);
                res.push_back(2);
                s1 = S.find_first_of('T'); //TWO
            }
        }

        sort( res.begin(), res.end() );
        cout << "Case #" << i << ": ";
        for( auto t : res )
            cout << t;
        cout << endl;

        f_out << "Case #" << i << ": ";
        for( auto t : res )
            f_out << t;
        f_out << endl;

        res.clear();

    }

    f_in.close();
    f_out.close();
    return 0;
}
