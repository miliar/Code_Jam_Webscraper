#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream f;
    fstream o;
    f.open("A-large.in", ios::in);
    o.open("output.txt", ios::out);
    int T(0), N(0);
    f >> T;
    for(int a(1); a <= T; a++)
    {
        f >> N;
        int n(0), i(1);
        bool test[10] = {false};
        int base = N;
        if (N == 0)
        {
            o << "Case #" << a << ": " << "INSOMNIA" << endl;
        }
        else
        {
            while(1)
            {
                while(N != 0)
                {
                    if(test[N%10] == false)
                    {
                        test[N%10] = true;
                        n++;
                    }
                    N /= 10;
                    
                }
                if(n == 10)
                {
                    o << "Case #" << a << ": " << base*i << endl;
                    break;
                }
                else
                {
                    i ++;
                    N = base * i;
                }
            }
        }
    }
    f.close();
    o.close();
}
