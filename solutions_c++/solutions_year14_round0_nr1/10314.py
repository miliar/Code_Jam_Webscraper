#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int n,map1[5][5] = {0},map2[5][5] = {0};
    cin>>n;
    for(int k = 1;k <= n;k++)
    {
        int a,b,cur[5] = {0},cur_[5] = {0},ans = 0,_ans = 0;
        memset(map1,0,sizeof(map1));
        memset(map2,0,sizeof(map2));
        cin>>a;
        for(int i = 1;i <= 4;i++)
            for(int j = 1;j <= 4;j++)
                {
                    cin>>map1[i][j];
                    if(i == a)
                         cur[j] = map1[i][j];
                }
        cin>>b;
        for(int i = 1;i <= 4;i++)
            for(int j = 1;j <= 4;j++)
                {
                    cin>>map2[i][j];
                    if(i == b)
                        cur_[j] = map2[i][j];
                }
        for(int i = 1;i <= 4;i++)
           for(int j = 1;j <= 4;j++)
           {
                   if(cur[i] == cur_[j])
                   {
                   ans++;
                   _ans = cur[i];
                   }
           }
        if(ans == 0) cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else if(ans == 1) cout<<"Case #"<<k<<": "<<_ans<<endl;
        else if(ans > 1) cout<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    //system("pause");
    return 0;
} 
/*
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main () { int T; freopen ("input.txt", "r", stdin); freopen ("ouutput.txt", "w", stdout); scanf ("%d", &T); for (int j = 1; j <= T; j++) { int ans[17] = {0}; int tmp, q, flag = 0, target; scanf ("%d", &q); for (int i = 1; i <= 16; i++) { scanf ("%d", &tmp); if (i / 4 == (q-1)) ans[tmp]++; } scanf ("%d", &q); for (int i = 1; i <= 16; i++) { scanf ("%d", &tmp); if (i / 4 == (q-1)) ans[tmp]++; } for (int i = 1; i <= 16; i++) if (ans[i] == 2) { flag++; target = i; if (flag > 1) break; } if (flag == 0) printf ("Case #%d: Volunteer cheated!\n", j); if (flag == 1) printf ("Case #%d: %d\n", j, target); if (flag > 1) printf ("Case #%d: Bad magician!\n", j); } return 0;} 

*/
