#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int sheep(int n)
{
    bool check[10];
    for(int i=0;i<10;++i)
        check[i]=false;

    long long j=0;
    int k = 1;
    int inc = 0;
    int num = 0;

    if(n < 1)
        return -1;

    while(1)
    {
        j = n * k;
        inc = 0;
        while(j > 0)
        {
            num = j % 10;
            j /= 10;
            check [num] = true;
        }

        for(int i=0;i<10;++i)
        {
            if(check[i] == true)
                ++inc;
            if(inc == 10)
                return n * k;
        }
        ++k;
    }


    return -1;
}

int main()
{
    ifstream file("A-large.in");
    ofstream out("B-large.in");
    int t = 0;
    int n = 0;
    long long j = 0;
    file >> t;

    for(int i = 1; i <= t ; ++i)
    {
        file >> n;
        j = sheep(n);

        if (j == -1)
        {
            out << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            out << "Case #" << i << ": " << j << endl;
        }

    }

    out.close();
    file.close();
    return 0;
}
