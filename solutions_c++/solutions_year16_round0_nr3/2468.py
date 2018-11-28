#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;

int main()
{
    FILE *fin = freopen("C-small.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("C-small.out", "w", stdout);
    int tries, N, J;
    bool check;
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> N;
        cin >> J;
        int arr[N], j = 0;
        long long div[9];
        fill_n(arr,N,0);
        arr[0] = 1;
        arr[11] = 1;
        arr[N-1] = 1;
        cout << "Case #" << i << ": " << endl;
        while (j < J)
        {
            fill_n(div,9,0);
            check = true;
            int x = 2;
            while (x <= 10)
            {
                long long powr = 1;
                for (int l = N-1; l >= 0; l--)
                {
                    div[x-2] += (powr*arr[l]);
                    powr *= x;
                }
                long long num = div[x-2];
                
                if (num%2 == 0)
                    div[x-2] = 2;
                else
                {
                    for (int l = 3; (l*l) <= num; l+=2)
                    {
                        if ((num%l) == 0)
                        {
                            div[x-2] = l;
                            break;
                        }
                        if (l > 19)
                        {
                            break;
                        }
                    }
                }
                if (div[x-2] == num)
                {
                    x = 11;
                    check = false;
                }
                
                x++;
            }
            if (check == true)
            {
                for (int k = 0; k < N; k++)
                    cout << arr[k];
                for (int m = 0; m < 9; m++)
                    cout << " " << div[m];
                cout << endl;
                j++;
            }
            for (int k = N-2; k > 0; k--)
            {
                if (arr[k] == 0)
                {
                    arr[k] = 1;
                    break;
                }
                else
                    arr[k] = 0;
            }
        }
        
    }
    return 0;
}
