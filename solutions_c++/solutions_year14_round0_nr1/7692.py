#include <iostream>

using namespace std;

int main()
{
    int numTestCases = 0;
    cin>>numTestCases;

    int ans1, ans2;
    int first[4][4], second[4][4];

    for (int tc = 1; tc <= numTestCases; tc++)
    {
        cin>>ans1;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin>>first[i][j];
            }
        }

        cin>>ans2;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin>>second[i][j];
            }
        }

        int count = 0;
        int save = 0;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (first[ans1-1][i] == second[ans2-1][j])
                {
                    count++;
                    save = i;
                }
            }
        }
        //cout<<count<<endl;

        if (count > 1)
            cout<<"Case #"<<tc<<": Bad magician!"<<endl;
        else if (count == 0)
            cout<<"Case #"<<tc<<": Volunteer cheated!"<<endl;
        else
            cout<<"Case #"<<tc<<": "<<first[ans1-1][save]<<endl;
    }

    return 0;
}
