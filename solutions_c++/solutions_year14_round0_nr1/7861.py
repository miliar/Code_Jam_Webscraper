#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int T,tt;
    vector<int> vi;
    cin >> T;

    for(tt = 1;tt <= T;tt++)
    {

        vi.clear();

        int r[2],ta[2][4][4];

        for(int num=0;num<2;num++)
        {
            cin >> r[num] ;
            r[num]--;
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                    cin >> ta[num][i][j];
            }
        }

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(ta[0][r[0]][i] == ta[1][r[1]][j])
                    vi.push_back(ta[0][r[0]][i]);
            }
        }

        cout << "Case #" << tt << ": " ;
        if(vi.size() == 0)
            cout << "Volunteer cheated!";
        else if(vi.size() == 1)
            cout << vi[0];
        else
            cout << "Bad magician!";

        cout << '\n' ;
    }


    return 0;
}
