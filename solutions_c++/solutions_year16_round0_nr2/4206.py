#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r" , stdin);
    freopen("outputB.txt", "w" , stdout);
    int T , length;
    string input;
    long long int counter;
    scanf("%d", &T);

    for(int i = 0 ; i < T ; i++)
    {
        cin >>input;
        counter = 0;

        length = input.length();

        for(int j = 0 ; j < length ; j++)
        {
            if(j== 0 && input[j] == '-')
            {
                counter++;
            }
            else if (input[j] == '+' && input[j+1] == '-' && j<=length-2)
            {
                counter += 2;
            }
        }
        printf("Case #%d: %lld\n", i+1 , counter);

    }
    return 0;
}
