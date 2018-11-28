#include <iostream>
#include <fstream>
using namespace std;

int chkDig(int num)
{
    bool digits[10] = {0};
    int c = 0, i = 1;
    int temp;
    while(c < 10)
    {
        temp = num * i;
        while(c < 10 && temp > 0)
        {
            int d;
            d = temp % 10;
            if(digits[d] == 0)
            {
                digits[d] = 1;
                c++;
            }
            temp /= 10;
        }
        if(c == 10)
        {
            return num * i;
        }
        i++;
    }
}

int main()
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        int num, lstNum;
        cin >> num;
        if(num == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" <<endl;
            continue;
        }
        lstNum = chkDig(num);
        cout << "Case #" << i << ": " << lstNum << endl;
    }
}
