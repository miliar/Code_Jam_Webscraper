#include<iostream>
#include<string>
#include<vector>
//#include<math.h>
//#include<utility>

using namespace std;

int main()
{
    int T;
    cin >> T;
    int cases = 0;
    for(int i = 0; i < T; i++)
    {
        cases++;
        vector<int> row;
        vector<int> cards;
        int answer;
        cin >> answer;
        for(int j = 1; j <= 4; j++)
        {
            for(int k = 1; k <= 4; k++)
            {
                int temp;
                cin >> temp;
                if(j == answer)
                    row.push_back(temp);
            }
        }
        cin >> answer;
        int length = 0;
        for(int j = 1; j <= 4; j++)
        {
            for(int k = 1; k <= 4; k++)
            {
                int temp;
                cin >> temp;
                if(j == answer)
                {
                    bool isinrow = false;
                    for(int z = 1; z <= 4; z++)
                        isinrow = (isinrow || (temp == row[z-1]));
                    if(isinrow)
                    {
                        length++;
                        cards.push_back(temp);
                    }
                }
            }
        }
        cout << "Case #" << cases << ": ";
        if(cases < T)
        {
            if(length == 0)
                cout << "Volunteer cheated!\n";
            if(length >= 2)
                cout << "Bad magician!\n";
            if(length == 1)
                cout << cards[0] << endl;
        }
        else
        {
            if(length == 0)
                cout << "Volunteer cheated!";
            if(length >= 2)
                cout << "Bad magician!";
            if(length == 1)
                cout << cards[0];
        }
    }
}
