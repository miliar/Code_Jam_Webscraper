#include <iostream>
#include <string>

using namespace std;

int char_to_int(unsigned char c)
{
    return (c-0x30);
}

int main()
{
    int T;
    cin >> T;
    for(int tt = 1; tt<= T; tt++)
    {
        unsigned int Smax;
        string s;
        int cnt = 0;
        int sum = 0;
        cin >> Smax >> s;
        for(int i = 0; i < s.length()-1; i++)
        {
            int new_int = char_to_int(s[i]);
            sum += new_int;
            if(sum < i+1)
            {
                cnt += (i+1)-sum;
                sum = i+1;
            }
        }
        cout << "Case #" << tt << ": " << cnt << endl;
    }
    return 0;
}
