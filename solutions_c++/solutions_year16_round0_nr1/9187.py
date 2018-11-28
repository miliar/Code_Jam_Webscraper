#include <iostream>
#include <cstdio>
#include <set>

using namespace std;
int main()
{
    freopen("/home/shaza/Desktop/Projects/CJam16Q/A-large.in","r",stdin);
    freopen("/home/shaza/Desktop/Projects/CJam16Q/ALARGE_output.txt","w",stdout);
    int n;
    cin >> n;
    long t, y, num;
    int c;
    int d;
    for(int i = 0; i < n; i++)
    {
        cin >> t;
        set<int> digits;
        bool counting = true;
        c = 1;
        if(t == 0){
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" <<endl;
        }
        else{
        while(counting)
        {
            y = t * c;
            num = y;
            while (num)
                {
                    d = num % 10;
                    digits.insert(d);
                    num /= 10;
                }

            if(digits.size() == 10)
            {
                cout << "Case #" << i + 1 << ": " << y <<endl;
                counting = false;
            }
            c++;
        }
        }
    }

    return 0;
}
