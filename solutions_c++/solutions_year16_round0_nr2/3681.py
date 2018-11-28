#include <iostream>
#include <vector>
#include <math.h>
#include <cmath>

using namespace std;

int LIMIT = (1<<10)-1;

int main(){
    int tc,n,ans;
    string cur;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++){
        cin >> cur;
        ans = cur[0]=='-';
        for(int i=0;i<cur.length()-1;i++){
            if(cur[i]=='+' && cur[i+1] == '-')
                ans += 2;
        }
        printf("Case #%d: %d\n",tci,ans);
    }
    return 0;
}