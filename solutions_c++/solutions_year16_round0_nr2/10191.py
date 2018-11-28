// consciousbot
// danilod100 at gmail.com
// http://danilo.gr

#include <iostream>
#include <vector>

using namespace std;


class Pancake
{
    vector<bool> b;
    public:
        Pancake(const string& p) : b(p.length(), false)
        {
            for (unsigned int i=0; i < p.length(); ++i)
            {
                if (p[i] == '+') b[i] = true;
            }
        }

        // assuming pos >= 0 & < length
        // not testing it because it's gcj
        void flipPancakes(int pos)
        {
            while(pos >= 0)
            {
                b[pos] = !b[pos];
                --pos;
            }
        }

        unsigned int makeHappy()
        {
            unsigned int ret = 0;


            for (int i = b.size()-1; i >= 0; --i)
            {
                if (!b[i])
                {
                    ++ret;
                    flipPancakes(i);
                }
            }

            return ret;
        }

};




int main(int argc, char *argv[])
{
    cout.sync_with_stdio(false);
    unsigned int T;

    cin >> T;
    unsigned int counter = 0;
    while (T--)
    {
        string ps;
        cin >> ps;
        Pancake p(ps);
        cout << "Case #"<<++counter<<": " << p.makeHappy() << '\n';
    }

    return 0;
}
