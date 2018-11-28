#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int test = 0;test<T;test++)
    {
        long long int N;
        cin >> N;
        if(N==0)
        {
            cout << "Case #" << test+1 << ": INSOMNIA" << endl;
        }
        else
        {
            bool done = false;
            bool seen[10] = {0,0,0,0,0,0,0,0,0,0};
            long long int answer;
            for(long long int multi = 1;done == false;multi++)
            {
                done = true;
                int temp = N*multi;
                answer = temp;
                while(temp > 0)
                {
                    seen[temp%10] = true;
                    temp = temp/10;
                }
                for(int c = 0;c<10;c++)
                {
                    if(seen[c] == false)
                    {
                        done = false;
                    }
                }
            }
            cout << "Case #" << test+1 << ": " << answer << endl;
        }

    }
    return 0;
}
