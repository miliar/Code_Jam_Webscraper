#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;

void print( int t, bool ans)
{
    cout << "Case #" << t << ": " << (ans ? "YES" : "NO") << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        int n,m;
        cin >> n >> m;
        
        VVI a(n,VI(m,0));
        for (int i=0;i<n;++i)
        {
            for (int j=0;j<m;++j)
            {
                cin >> a[i][j];
            }
        }

        VVB b(n,VB(m,false));

        for (int i=0; i<n;++i)
        {
            int _max = 0;
            for (int j=0;j<m;++j)
            {
                if (_max < a[i][j]) _max = a[i][j];
            }

            for (int j=0;j<m;++j)
                if ( _max == a[i][j]) b[i][j]=true;
        }
        
        for (int j=0; j<m;++j)
        {
            int _max = 0;
            for (int i=0;i<n;++i)
            {
                if (_max < a[i][j]) _max = a[i][j];
            }

            for (int i=0;i<n;++i)
                if ( _max == a[i][j]) b[i][j]=true;
        }

        bool ans = true;
        for (int i=0;i<n;++i)
        {
            for (int j=0;j<m;++j)
                if ( !b[i][j]) ans = false;
        }

        print( t+1, ans);

    }
    return 0;
}
