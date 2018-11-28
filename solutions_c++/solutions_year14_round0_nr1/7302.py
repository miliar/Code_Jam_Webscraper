#include <iostream>
using namespace std;

int main()
{
    int T, a, b;
    int arr[8];
    int tmp;

    cin >> T;

    for(int i=0; i<T; ++i)
    {
        cin >> a;
        for(int j=1; j<5; ++j)
        {
            if(j==a)
                cin>> arr[0] >> arr[1] >> arr[2] >> arr[3];
            else
                cin >> tmp >> tmp >> tmp >> tmp;
        }

        cin >> b;
        for(int j=1; j<5; ++j)
        {
            if(j==b)
                cin>> arr[4] >> arr[5] >> arr[6] >> arr[7];
            else
                cin >> tmp >> tmp >> tmp >> tmp;
        }

        int match = 0;
        int matched;
        
        for(int j=0; j<4; ++j)
        {
            int temp = arr[j];
            for(int k=4; k<8; ++k)
            {
                if(temp == arr[k])
                {
                    match += 1;
                    matched = temp;
                }
            }
        }

        switch(match)
        {
            case 0: cout << "Case #" << i+1 << ": Volunteer cheated!\n"; break;
            case 1: cout << "Case #" << i+1 << ": " << matched << "\n"; break;
            default: cout << "Case #" << i+1 << ": Bad magician!\n";
        }
    }
}
