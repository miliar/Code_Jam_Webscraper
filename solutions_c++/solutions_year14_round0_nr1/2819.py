#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;

    for (int tt = 0; tt < T; ++tt)
    {
        int a, b;
        int card_a[16], card_b[16];
        cin >> a;
        for (int i = 0; i < 16; ++i)
        {
            cin>>card_a[i];
        }
        cin >> b;
        for (int i = 0; i < 16; ++i)
        {
            cin>>card_b[i];
        }

        int find = 0;
        int result = 0;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                if (card_a[(a-1)*4+i] == card_b[(b-1)*4+j])
                {
                    ++ find;
                    result = card_a[(a-1)*4+i];
                }
            }
        }

        cout << "Case #" << tt+1 << ": " ;
        switch (find)
        {
            case 0:
                cout << "Volunteer cheated!" << endl;
                break;
            case 1:
                cout << result << endl;
                break;
            default:
                cout << "Bad magician!" << endl;
                break;
        }
    }
    return 0;
}