#include <iostream>
#include <algorithm>
#include <stdio.h>

    using namespace std;

#define foru(i,l,r) for(int i=l; i<=r; i++)
#define LL long long
#define maxn 5

int a[maxn][maxn], b[maxn][maxn], x,y, res, ntest,resi;

int main()
{
    freopen("test.txt","r",stdin);
    freopen("solution.txt","w",stdout);

    cin >> ntest;

    foru(test,1,ntest)
    {
        cin >> x;
        foru(i,1,4)
            foru(j,1,4)
                cin >> a[i][j];
        cin >> y;
        foru(i,1,4)
            foru(j,1,4)
                cin >> b[i][j];

        res = 0;

        foru(i,1,4)
        {
            foru(j,1,4)
                if (a[x][i]==b[y][j])
                {
                    res++;
                    resi = a[x][i];
                    break;
                }
        }

        if (res==0)
        {
            cout << "Case #" << test << ": Volunteer cheated!" << endl;
        }
        else
            if (res==1)
                cout << "Case #" << test << ": " << resi << endl;
            else
                cout << "Case #" << test << ": Bad magician!" << endl;
    }
}
