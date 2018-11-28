#include<iostream>
using namespace std;

int w[16];

int main()
{
    int t, r, a, l, odp;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        cin >> r;
        r--;
        for(int j = 0; j < 16; j++)
        {
            cin >> a;
            if(j / 4 == r)
            {
          //      cout<<"    "<<a<<"\n";
                w[a - 1]++;
            }
        }
        cin >> r;
        r--;
        for(int j = 0; j < 16; j++)
        {
            cin >> a;
            if(j / 4 == r)
            {
                w[a - 1]++;
          //      cout<<"    "<<a<<"\n";
            }
        }
        l = 0;
        for(int j = 0; j < 16; j++)
        {
            if(w[j] == 2)
            {
                l++;
       //         cout << j;
                odp = j + 1;
            }
            w[j] = 0;
        }
        cout << "Case #" << i << ": ";
        if(l == 0)
            cout << "Volunteer cheated!\n"; 
        if(l == 1)
            cout << odp << "\n";
        if(l > 1)
            cout << "Bad magician!\n";
    }
    return 0;
}
                
