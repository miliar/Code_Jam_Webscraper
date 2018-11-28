#include <iostream>
#include <string>
#include <vector>

using namespace std;

void convert_to_number(const string& shyness, vector<unsigned int>& numbers)
{
    unsigned int current_entry;
    for(unsigned int i=0; i<shyness.size(); ++i)
    {
        if(shyness[i] == '0')
            current_entry = 0;
        if(shyness[i] == '1')
            current_entry = 1;
        if(shyness[i] == '2')
            current_entry = 2;
        if(shyness[i] == '3')
            current_entry = 3;
        if(shyness[i] == '4')
            current_entry = 4;
        if(shyness[i] == '5')
            current_entry = 5;
        if(shyness[i] == '6')
            current_entry = 6;
        if(shyness[i] == '7')
            current_entry = 7;
        if(shyness[i] == '8')
            current_entry = 8;
        if(shyness[i] == '9')
            current_entry = 9;

        numbers.push_back(current_entry);
    }
}

int main()
{
    unsigned int T;
    unsigned int num_ppl_standing;
    unsigned int num_ppl_needed;
    unsigned int shyness_level;

    string shyness;

    vector <unsigned int> numbers;

    cin >> T;

    for(unsigned int i=0; i<T; ++i)
    {
        num_ppl_standing = 0;
        num_ppl_needed = 0;

        shyness.clear();
        numbers.clear();

        cin >> shyness_level;
        cin >> shyness;

        convert_to_number(shyness, numbers);
        num_ppl_standing += numbers[0];

        if(numbers.size() > 1)
        {
            for(unsigned int j=1; j<numbers.size(); ++j)
            {
                if(numbers[j] > 0)
                {
                    if(j <= num_ppl_standing)
                    {
                        num_ppl_standing += numbers[j];
                    }
                    else
                    {
                        num_ppl_needed += j - num_ppl_standing;
                        num_ppl_standing += (j - num_ppl_standing);
                        num_ppl_standing += numbers[j];
                    }
                }
            }
        }

        cout << "Case #" << (i+1) << ": " << num_ppl_needed << "\n";

    }

    return 0;
}
