#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <string>
#include <climits>

using namespace std;



long long count(long long in)
{
    if(in == 0)
    {
        return -1;
    }

    bool num[10] = {false};
    long long i = 1,in2,temp;
    bool good = false;
    bool killNext = false;
    while(!killNext)
    {
        in2 = in * i;
        if( (LLONG_MAX - in)   < in2)
        {
            killNext = true;
        }
        temp = in2;
        while(temp > 0)
        {
            num[temp%10] = true;
            temp = temp / 10;
        }
        good = true;
        for(int j = 0; j < 10 && good;j++)
        {
            if(!num[j])
                good = false;
        }
        if(good)
        {
            return in2;
        }

        i++;
    }
    return -1;
}


int main()
{
    long long times;
    long long num;
    long long result;
    cin >> times;
    for(long long i = 1; i <= times; i++)
    {
        cin >> num;
        result = count(num);
        cout << "Case #" << i << ": ";

        if(result ==  -1)
        {
            cout << "INSOMNIA" << endl;
        }
        else
        {
            cout << result << endl;
        }
    }

}
