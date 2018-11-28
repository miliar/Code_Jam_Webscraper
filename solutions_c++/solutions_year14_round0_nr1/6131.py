#include <iostream>

using namespace std;

int T, ans, count, r1, r2;
int a[4][4], b[4][4];
int main() 
{
    cin>>T;
    for (int ii = 0; ii < T; ++ii)
    {
        cin>>r1;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                cin>>a[i][j];
            }
        }
        cin>>r2;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                cin>>b[i][j];
            }
        }
        count = 0;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                if (a[r1-1][i] == b[r2-1][j])
                {
                    count++;
                    ans = a[r1-1][i];
                }
            }
        }
        cout<<"Case #"<<ii+1<<": ";
        if (count == 0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else
        {
            if (count > 1)
            {
                cout<<"Bad magician!"<<endl;
            }
            else
            {
                cout<<ans<<endl;
            }
        }
    }
    return 0;
}