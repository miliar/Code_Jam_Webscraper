#include<bits/stdc++.h>
#define loop(i, a, b)  for(int i=a;i<b;i++)
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    int t, r1, r2;
    int grid1[4][4];
    int grid2[4][4];
    cin>>t;
    loop(te, 0, t)
    {
        vector<int> v1;
        vector<int> v2;
        cin>>r1;
        loop(i, 0, 4)
            loop(j, 0, 4)
                cin>>grid1[i][j];
        cin>>r2;
        loop(i, 0, 4)
            loop(j, 0, 4)
                cin>>grid2[i][j];
        loop(i, 0, 4)
            v1.push_back(grid1[r1-1][i]);
        loop(i, 0, 4)
            v2.push_back(grid2[r2-1][i]);
        int cnt = 0;
        int ans = 0;
        loop(i, 0, 4)
        {
            loop(j, 0, 4)
            {
                if(v1[i]==v2[j] && cnt==0)
                {
                    ans = v1[i];
                    cnt++;
                }
                else if(v1[i]==v2[j] && cnt>=1)
                {
                    ans = 99;
                    break;
                }
            }
            if(ans==99) break;
        }
        cout<<"Case #"<<te+1<<": ";
        if(ans==0)
            cout<<"Volunteer cheated!\n";
        else if(ans==99)
            cout<<"Bad magician!\n";
        else
            cout<<ans<<endl;
    }
    return 0;
}
