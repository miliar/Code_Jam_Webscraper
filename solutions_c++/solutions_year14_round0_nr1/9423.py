#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;
    int t;
    cin >> t;
    int a[4][4];
    int ans1,ans2;
    for(i=1;i<=t;i++)
    {
        bool hash[17]={0};
        int count=0;
        cin >> ans1;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            cin >> a[j][k];
        //cout << "here " << endl;
        for(j=0;j<4;j++)
            hash[a[ans1-1][j]]=1;
        //cout << "here" << endl;
        cin >> ans2;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            cin >> a[j][k];
        int ans;
        //cout << "here" << endl;
        for(j=0;j<4;j++)
            if(hash[a[ans2-1][j]])
            {
                ans=a[ans2-1][j];
                count++;
            }
       // cout << "here" << endl;
        if(count==0)
        cout << "Case #" << i << ": Volunteer cheated!" << endl;
        else if(count==1)
        cout << "Case #" << i << ": " << ans << endl;
        else
        cout << "Case #" << i << ": Bad magician!" << endl;
    }
    return 0;
}
