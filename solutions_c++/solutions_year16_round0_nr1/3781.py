#include "Libs.h"

using namespace std;

int nTests;

int g_nbNbSeen = 0;
bool g_numbersSeen[] = { 0,0,0,0,0,0,0,0,0,0 };

void checkNumbers(long long int n)
{
    while (n > 0)
    {
        if(g_numbersSeen[n % 10] == 0)
        {
            g_numbersSeen[n % 10] = 1;
            ++g_nbNbSeen;
        }
       
        n /= 10;
    }
}

bool allGood()
{
    for (int j = 0; j < 10; ++j)
        if (!g_numbersSeen[j]) return false;
    return true;
}

int main()
{
	ofstream out("output.txt");
	ifstream in("A-large.in");

	in >> nTests;

	for (int i = 1; i <= nTests; ++i)
	{
        long long int nb = 0, cnt = 1;
        in >> nb;

        if (nb == 0)
            out << "Case #" << i << ": INSOMNIA" << endl;


        else
        {
            while (g_nbNbSeen != 10)
                checkNumbers(nb * cnt++);
            
            out << "Case #" << i << ": " << (nb * --cnt) << endl;

            for (int j = 0; j < 10; ++j)
                g_numbersSeen[j] = 0;

            g_nbNbSeen = 0;
        }
	}


	return 0;
}