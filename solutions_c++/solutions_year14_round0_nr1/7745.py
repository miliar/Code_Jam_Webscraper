#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <climits>
#include <map>

using namespace std;



int main() {
    //freopen("/Users/l/Documents/codejam/A-small-attempt0.in.txt", "r", stdin);
    //freopen("/Users/l/Documents/codejam/A-small-attempt0.out.txt", "w", stdout);
    int T,out = 1;
    scanf("%d",&T);
    //printf("%d\n",T);
    //return 0;
    while (T--) {
        printf("Case #%d: ",out++);
        int row,tmp,ans,cnt = 0;
        map<int ,int> mp;
        scanf("%d",&row);
        for(int i=1;i<=4;i++)
        {
            if(i == row)
            {
                for(int i=1;i<=4;i++){
                    scanf("%d",&tmp);
                    mp[tmp] = 1;
                }
            }
            else {
                for(int i=1;i<=4;i++)
                    scanf("%d",&tmp);
            }
            
        }
        scanf("%d",&row);
        for(int i=1;i<=4;i++)
        {
            if(i == row)
            {
                for(int i=1;i<=4;i++){
                    scanf("%d",&tmp);
                    if(mp[tmp] == 1)
                    {
                        ans = tmp;
                        cnt++;
                    }
                }
            }
            else {
                for(int i=1;i<=4;i++)
                    scanf("%d",&tmp);
            }
        }
        if(cnt == 0) puts("Volunteer cheated!");
        else if(cnt == 1) printf("%d\n",ans);
        else  puts("Bad magician!");
    }
    return 0;
}

