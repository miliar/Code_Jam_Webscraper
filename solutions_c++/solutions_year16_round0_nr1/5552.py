#include <fstream>
using namespace std;
ifstream ka("A-large.in");
ofstream ki("sheep.out");
bool este[10];
int n, t;
int main()
{
    ka >> t;
    for(int i = 1; i <= t; i++)
    {
        ka >> n;
        if(n != 0)
        {
            int f = n;
            int gasite = 0;
            int incercari = 0;
            for(int j = 0; j < 10; j++)
                este[j] = false;
            while(gasite < 10)
            {
                incercari++;
                int t = f;
                while(t)
                {
                    if(!este[t % 10])
                    {
                        gasite++;
                        este[t % 10] = true;
                    }
                    t /= 10;
                }
                f += n;
            }
            ki << "Case #" << i << ": " << f - n << '\n';
        }
        else
            ki << "Case #" << i << ": " << "INSOMNIA" << '\n';
    }
}
