#include <iostream>
#include <vector>

using namespace std;

bool lleno(bool *arr)
{
    bool a = true;
    for(int i = 0; i < 10; i++) 
    {
        a = (a && arr[i]);
    }

    return a;
}



int main()
{
    int T, N, j;
    long long int temp;
    bool inso;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        cin >> N;
        inso = true;
        bool digitos[10] = {0,0,0,0,0,0,0,0,0,0};
        for(j = 1; j <= 100; j++)
        {
            temp = N*j;
            while(temp > 0)
            {
                digitos[temp%10] = true;
                temp = temp/10;
            }

            if(lleno(digitos))
            {
                inso = false;
                break;
            }
        }
        cout << "Case #" << i+1 << ": ";
        if(inso)
        {
            cout << "INSOMNIA" << endl;
        }
        else
        {
            cout << j*N << endl;
        }
    }
}
