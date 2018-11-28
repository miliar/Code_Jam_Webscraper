#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream outf;
    ifstream inf;
    outf.open("a.out");
    inf.open("a.in");
    int T;
    inf >> T;
    for(int tt = 1 ; tt <= T ; tt++)
    {
        outf << "Case #" << tt << ": ";
        int b , m;
        inf >> b >> m;
        if(b == 2)
        {
            if(m == 1)
            {
                outf << "POSSIBLE" << endl;
                outf << "01" << endl << "00" << endl;
            }
            else
            {
                outf << "IMPOSSIBLE" << endl;
            }
        }
        else if(b == 3)
        {
            if(m == 1)
            {
                outf << "POSSIBLE" << endl;
                outf << "001" << endl << "000" << endl << "000" << endl;
            }
            else if(m == 2)
            {
                outf << "POSSIBLE" << endl;
                outf << "011" << endl << "001" << endl << "000" << endl;
            }
            else
            {
                outf << "IMPOSSIBLE" << endl;
            }
            
        }
        else if(b == 4)
        {
            if(m == 1)
            {
                outf << "POSSIBLE" << endl;
                outf << "0001\n0000\n0000\n0000" << endl;
            }
            else if(m == 2)
            {
                outf << "POSSIBLE" << endl;
                outf << "0101\n0001\n0000\n0000" << endl;
            }
            else if(m == 3)
            {
                outf << "POSSIBLE" << endl;
                outf << "0101\n0011\n0001\n0000" << endl;
            }
            else if(m == 4)
            {
                outf << "POSSIBLE" << endl;
                outf << "0111\n0011\n0001\n0000" << endl;
            }
            else
            {
                outf << "IMPOSSIBLE" << endl;
            }
        }
        else if(b == 5)
        {
            if(m == 1)
            {
                outf << "POSSIBLE" << endl;
                outf << "00001\n00000\n00000\n00000\n00000" << endl;
            }
            else if(m == 2)
            {
                outf << "POSSIBLE" << endl;
                outf << "01001\n00001\n00000\n00000\n00000" << endl;
            }
            else if(m == 3)
            {
                outf << "POSSIBLE" << endl;
                outf << "01001\n00101\n00001\n00000\n00000" << endl;
            }
            else if(m == 4)
            {
                outf << "POSSIBLE" << endl;
                outf << "01001\n00101\n00011\n00001\n00000" << endl;
            }
            else if(m == 5)
            {
                outf << "POSSIBLE" << endl;
                outf << "01011\n00101\n00011\n00001\n00000" << endl;
            }
            else if(m == 6)
            {
                outf << "POSSIBLE" << endl;
                outf << "01101\n00101\n00011\n00001\n00000" << endl;
            }
            else if(m == 7)
            {
                outf << "POSSIBLE" << endl;
                outf << "01111\n00101\n00011\n00001\n00000" << endl;
            }
            else if(m == 8)
            {
                outf << "POSSIBLE" << endl;
                outf << "01111\n00111\n00011\n00001\n00000" << endl;
            }
            else
            {
                outf << "IMPOSSIBLE" << endl;
            }
        }
        else if(b == 6)
        {
            if(m == 1)
            {
                outf << "POSSIBLE" << endl;
                outf << "000001\n000000\n000000\n000000\n000000\n000000" << endl;
            }
            else if(m == 2)
            {
                outf << "POSSIBLE" << endl;
                outf << "010001\n000001\n000000\n000000\n000000\n000000" << endl;
            }
            else if(m == 3)
            {
                outf << "POSSIBLE" << endl;
                outf << "010001\n001001\n000001\n000000\n000000\n000000" << endl;
            }
            else if(m == 4)
            {
                outf << "POSSIBLE" << endl;
                outf << "010001\n001001\n000101\n000001\n000000\n000000" << endl;
            }
            else if(m == 5)
            {
                outf << "POSSIBLE" << endl;
                outf << "010001\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 6)
            {
                outf << "POSSIBLE" << endl;
                outf << "010011\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 7)
            {
                outf << "POSSIBLE" << endl;
                outf << "010101\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 8)
            {
                outf << "POSSIBLE" << endl;
                outf << "011001\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 9)
            {
                outf << "POSSIBLE" << endl;
                outf << "011011\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 10)
            {
                outf << "POSSIBLE" << endl;
                outf << "011101\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 11)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001001\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 12)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001011\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 13)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001001\n000111\n000011\n000001\n000000" << endl;
            }
            else if(m == 14)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001111\n000101\n000011\n000001\n000000" << endl;
            }
            else if(m == 15)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001101\n000111\n000011\n000001\n000000" << endl;
            }
            else if(m == 16)
            {
                outf << "POSSIBLE" << endl;
                outf << "011111\n001111\n000111\n000011\n000001\n000000" << endl;
            }
            else
            {
                outf << "IMPOSSIBLE" << endl;
            }
        }
    }
}


















