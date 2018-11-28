#include <iostream>
using namespace std;

bool fillNumber(unsigned int n, bool number[])
{
    unsigned int pn = n;
    while(true)
    {
        unsigned int g = pn%10;
        number[g] = true;
        pn = pn/10;
        if(pn==0) break;
    }
    bool allFilled = true;
    for(int i=0; i<10; ++i)
    {
        if(!number[i])
        {
            allFilled = false;
            break;
        }
    }
    return allFilled;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;
    for(int i=0; i<T; ++i)
    {
        unsigned int N;
        cin >> N;
        cout << "Case #" << i+1 << ": ";
        if(N==0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        unsigned int DN = N; 
        unsigned int m = 1;
        bool number[10]={0};
        while(true)
        {
            DN = N * m;
            if(fillNumber(DN, number))
            {
                break;
            }
            ++m;
        }
        cout << DN << endl;
    }
    return 0;
}

