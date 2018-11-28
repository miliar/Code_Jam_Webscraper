#include <iostream>
#include <string>
#include <bitset>
#include <sstream>
#include <string.h>

using namespace std;

class Case
{
    public:
        Case(int n): num(n), count(0) {}
        int step() { return num*(++count); }

    private:
        int num;
        int count;
};


bool find(int source, int n)
{
    stringstream ss (stringstream::in | stringstream::out);
    ss << source;
    const char *test = ss.str().c_str();
    char *pch = (char*) memchr (test, n+48, strlen(test));

    return (pch != NULL);
}


int main()
{
    int T, t, ctemp, fi, current, state;
    cin>>T;

    for(t=1; t<=T; t++)
    {
        cin>>ctemp;
        if(!ctemp)
        {
            cout<< "Case #" << t << ": " << "INSOMNIA" << endl;
            continue;
        }

        Case c(ctemp);
        state = 0;

        while(state < 1023)
        {
            current = c.step();
            for(fi=0; fi<10; fi++)
            {
                if(find(current, fi)) state |= (1<<fi);
            }
        }

        cout<< "Case #" << t << ": " << current << endl;

    }


  return 0;
}
