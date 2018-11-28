#include <iostream>
using namespace std;

int N, M;
int board[100][100];

bool judgeheight(int cutoff)
{
    for (int i=0;i<N;i++)
        for (int j=0;j<M;j++)
            if (board[i][j]<=cutoff)
            {
                bool Q= true, R = true;
                for (int k = 0; k<N;k++)
                    if (board[k][j]>cutoff)
                        Q = false;
                for (int k = 0; k<M;k++)
                    if (board[i][k]>cutoff)
                        R = false;
                if (!Q && !R)
                    return false;
            }
    return true;
}

bool real_main()
{
    cin>>N>>M;
    for (int i=0;i<N;i++)
        for (int j=0;j<M;j++)
            cin>>board[i][j];
    for (int i = 99; i>0; i--)
        if (!judgeheight(i))
            return false;
    return true;
}

int main()
{
    int T; cin>>T;
    for (int i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if (real_main())
            cout<<"YES";
        else
            cout<<"NO";
        cout<<endl;
    }
    return 0;
}
