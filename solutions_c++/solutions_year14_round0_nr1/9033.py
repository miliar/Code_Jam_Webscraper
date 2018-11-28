#include<cstdio>
#include<ctype.h>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<iostream>
#include<sstream>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

struct Guess
{
    int grid[4][4];
};

int GetAns(Guess guess, int row, vector<int> choose )
{
    int counter=0;
    int ans;
    int i,j;
    for(i=0;i<4;i++)
        for(j=0; j<choose.size();j++)
            if ( guess.grid[row][i] == choose[j])
            {
                counter++;
                ans = choose[j];
                break;
            }
    if (counter > 1) return -1;
    if ( counter == 1) return ans;
    return -2;
}

int main()
{
    //freopen("sample.txt","r",stdin);
    freopen("a.in","r",stdin);

    freopen("a.out","w",stdout);

    int kase=1;
    int test;
    cin>>test;

    while (test--)
    {
        int row;
        cin>>row;
        row--;
        int i,j;
        Guess guess;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>guess.grid[i][j];
        vector<int> choose;
        for(i=0;i<4;i++)
            choose.pb(guess.grid[row][i]);
        cin>>row;//second round
        row--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>guess.grid[i][j];

        int ans = GetAns(guess,row,choose);
        cout<<"Case #"<<kase<<": ";
        kase++;
        if ( ans > 0) cout<<ans<<endl;
        else if ( ans == -1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
