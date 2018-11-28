#include<iostream>
#include<string>

using namespace std;

int main()
{
    int t, n, count, sum;
    string s;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        count = 0;
        sum = 0;
        cin >> n >> s;

        for(int j = 0; j < s.size(); j++)
        {
            if(sum < j)
            {
                count++;
                sum++;

                sum = sum + (s[j] - '0') ;
            }

            else
            {
                sum = sum + (s[j] - '0') ;
            }

        }

        cout << "Case #" << i+1 << ": " << count << endl;

    }
}
