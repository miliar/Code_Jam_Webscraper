/* Sayan Chaudhry
 * sheep.py
 */

#include <iostream>

#define ll long long

using namespace std;

int sleep(int);

int main()
{
    ll T;
    int n, i;
    
    cin >> T;
    
    for(i = 1; i <= T; i++)
    {
        cin >> n;
        
        if (n != 0)
            cout << "Case #" << i << ": " << sleep(n) << '\n';
        else
            cout << "Case #" << i << ": INSOMNIA" << '\n';
    }
    
    return 0;
    
}

int sleep(int n)
{
    int i = 1, tmp, dgt;
    int numbers[] = {0,0,0,0,0,0,0,0,0,0};
    
    while(1)
    {
        tmp = n * i;
//        cout << tmp << '\t';
        
        while(tmp!=0)
        {
            dgt = tmp % 10;
            tmp = tmp / 10;
            ++numbers[dgt];
        }
        
//        for(int j = 0; j < 10; j++)
//            cout << numbers[j] << '\t';
//        cout << '\n';
        
        if(numbers[0] > 0 && numbers[1] > 0 && numbers[2] > 0 && numbers[3] > 0 && numbers[4] > 0 && numbers[5] > 0 && numbers[6] > 0 && numbers[7] > 0 && numbers[8] > 0 && numbers[9] > 0)
            break;
        
        i = i + 1;
        
    }

    return n * i;
}
