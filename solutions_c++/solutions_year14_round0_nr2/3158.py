#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    std::cout.precision(7);

    uint64_t T;
    cin >> T;

    double C, F, X;
    double current_answer;
    double minimal_answer;
    double time_taken_prev;
    double curr_cookie_count;

    for(uint64_t i=0; i<T; ++i)
    {
        current_answer = 0;
        minimal_answer = 0;
        time_taken_prev = 0;
        curr_cookie_count = 2;

        cin >> C;
        cin >> F;
        cin >> X;

        current_answer = X / curr_cookie_count;
        minimal_answer = current_answer;
        time_taken_prev = C / curr_cookie_count;
        curr_cookie_count += F;

        // Logic for the next cookie
        while(true)
        {
            current_answer = time_taken_prev + (X / curr_cookie_count);
            if(current_answer < minimal_answer)
            {
                minimal_answer = current_answer;
                time_taken_prev += (C / curr_cookie_count);
                curr_cookie_count += F;
            }
            else
            {
                break;
            }
        }

        cout << "Case #" << (i+1) << ": ";
        cout << std::fixed << minimal_answer << "\n";
    }

    return 0;
}
