#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        int r1,r2;
        int a1[4][4],a2[4][4];
        cin >> r1;
        for(int i=0; i<16; i++)
            cin >> *(*a1+i);
        cin >> r2;
        for(int i=0; i<16; i++)
            cin >> *(*a2+i);
        int *p1 = *(a1+(r1-1));
        int *p2 = *(a2+(r2-1));
        int count = 0, nbr;
        for (int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(p1[i]==p2[j])
                {
                    count++;
                    nbr = p1[i];
                    break;
                }
            }
        }

        if(count==0)
            cout << "Case #" << t << ": Volunteer cheated!" << endl;
        else if(count==1)
            cout << "Case #" << t << ": " << nbr << endl;
        else
            cout << "Case #" << t << ": Bad magician!" << endl;
    }
    return 0;
}
