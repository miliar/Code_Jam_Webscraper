#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
using namespace std;
int main()
{
    int T;
    int n;
    cin >> T;
    int dummy;
    int cards[4];
    int card;
    int possible;
    for(int t = 0; t < 2*T;t++)
    {
        possible = 0;
        if(t%2 != 1)
            memset(cards,0,sizeof(int) * 4);
        cin >> n;
        for(int i = 0 ; i < 4; i++)
            for( int j = 0;j < 4;j++ )
            {
                cin >> dummy;
                if(i + 1 == n)
                    if(t%2)
                    {
                            for(int i = 0; i < 4 && possible < 2; i++ )
                                if(cards[i] == dummy)
                                 {
                                     card = cards[i];
                                    possible++;
                                 }
                    }
                    else
                        cards[j] = dummy;
             }
        if(t%2)
        {
            cout << "Case #" << t/2+1 << ": ";
            if(possible == 0)
                cout << "Volunteer cheated!";
            else if (possible == 1)
                cout << card;
            else
                cout << "Bad magician!";
            cout << endl;
        }
    }
}
