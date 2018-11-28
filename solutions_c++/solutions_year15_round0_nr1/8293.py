#include <iostream>

using namespace std;

int solve()
{
    int max_shyness;
    int required_people = 0;
    int people_so_far = 0;
    cin >> max_shyness;
    //cout << "DEBUG: max_shyness=" << max_shyness << endl; 
    for(int i=0;i<=max_shyness;i++)
    {
        char num_with_this_shyness_char;
        cin >> num_with_this_shyness_char;
        int num_with_shyness = num_with_this_shyness_char - '0';
        //cout << "DEBUG: num_with_shyness=" << num_with_shyness << " shyness=" << i << endl;
        if(people_so_far < i && num_with_shyness > 0)
        {
            required_people += i - people_so_far;
            people_so_far += i-people_so_far;
        }
        people_so_far += num_with_shyness;
        //cout << "DEBUG: people_so_far=" << people_so_far << endl;
    }
    return required_people;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
    {
        int res = solve();
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
