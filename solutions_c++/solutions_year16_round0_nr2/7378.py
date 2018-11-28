#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int test = 0;test<T;test++)
    {
        string start;
        cin >> start;
        char last = start[0];
        int answer = 0;
        for(int c = 0;c<start.length();c++)
        {
            if(last != start[c])
            {
                last = start[c];
                answer++;
            }
        }
        if(last == '-')
        {
            answer++;
        }
        cout << "Case #" << test+1 << ": " << answer << endl;

    }
    return 0;
}
