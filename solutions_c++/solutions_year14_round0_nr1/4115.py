#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int tt=1;tt<=t;tt++) {
        int x , y;
        int a[5][5] , b[5][5];
        cin >> x;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >> a[i][j];
        cin >> y;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin >> b[i][j];
        vector <int> aa , bb;
        for(int j=0;j<4;j++) aa.push_back(a[x-1][j]);
        for(int j=0;j<4;j++) bb.push_back(b[y-1][j]);
        int co = 0 , ans;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(aa[i] == bb[j]) {ans = aa[i];co++;}
        if(co == 0) cout << "Case #" << tt << ": " << "Volunteer cheated!" << '\n';
        else if(co == 1) cout << "Case #" << tt << ": " << ans << '\n';
        else  cout << "Case #" << tt << ": " << "Bad magician!" << '\n';
    }
	return 0;
}
