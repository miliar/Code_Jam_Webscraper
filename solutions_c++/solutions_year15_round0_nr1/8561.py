#include <iostream>

using namespace std;

int CharToInt(char character)
{
    return character - '0';
}

int main()
{
    int test_cases;

    cin >> test_cases;

    for(int i = 0; i < test_cases; i++)
    {
        int max_shyness;
        cin >> max_shyness;

        string audience_shyness;
        cin >> audience_shyness;

        int standing_people = 0;
        int needed_people = 0;

        for(int j = 0; j <= max_shyness; j++)
        {
            if(standing_people < j)
            {
                needed_people += j - standing_people;
                standing_people += j - standing_people;
            }

            standing_people += CharToInt(audience_shyness[j]);
        }

        cout << "Case #" << i + 1 << ": " << needed_people << endl;
    }

    return 0;
}
