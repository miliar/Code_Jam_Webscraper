#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <sstream>
#include <list>


using namespace std;

unsigned long isqrt(unsigned long x)
{
    register unsigned long op, res, one;

    op = x;
    res = 0;

    /* "one" starts at the highest power of four <= than the argument. */
    one = 1 << 30;  /* second-to-top bit set */
    while (one > op) one >>= 2;

    while (one != 0) {
        if (op >= res + one) {
            op -= res + one;
            res += one << 1;  // <-- faster than 2 * one
        }
        res >>= 1;
        one >>= 2;
    }
    return res;
}

int cic(unsigned long tn)
{
            int l, j, out;
            string st;

            st = static_cast<ostringstream*>( &(ostringstream() << tn) )->str();

            l = st.length();
            j = 0; out = 1;
            while (j<l/2 && out==1)
            {
                if (st[j]!=st[l-j-1]) out = 0;
                j++;
            }

            return out;
}


int main(void)
{
	unsigned long N;


	//freopen("C-large.in", "rt", stdin);
	freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;

    unsigned long a, b, i, c, sq;



	unsigned long n;
	for (n=1;n<=N;n++)
	{
        c=0;

        cin >> a >> b;

        for (i=a; i<=b; i++)
        {
            //itoa(i, c, 10);

            sq = isqrt(i);
            if ( cic(i) && cic(sq) && sq*sq==i ) c++;


            //cout << i << " " << isqrt(i) << " " << c << endl;

        }


        cout << "Case #" << n << ": " << c << endl;
   	}


   	//for (int dp = 1000; dp < 100000; dp++)
   	//cout << dp << " -> " << cic(dp) << endl;


}
