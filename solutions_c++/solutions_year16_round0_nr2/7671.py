#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
int t;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("res.txt","w",stdout);
    cin>>t;
    for(int no = 1 ; no <= t ; no++ )
    {
        queue<string> Q;
        string cake;
        cin>>cake;
        while(!Q.empty()) Q.pop();
        map<string, int> chk;
        chk.clear();
        Q.push(cake); chk[cake] = 1;
        while( !Q.empty() )
        {
            string now = Q.front(); Q.pop();
            int cnt = 0;
            for(int i = 0 ; i < now.size() ; i++ )
                if( now[i] == '+' ) cnt++;
            if( cnt == now.size() )
            {
                printf("Case #%d: %d\n", no, chk[now]-1);
                break;
            }
            for(int i = 1 ; i <= now.size() ; i++ )
            {
                string next = now, temp = now.substr(0, i);
                for(int j = i-1, k = 0 ; j >= 0 ; j--, k++ )
                    next[j] = (temp[k]=='+'?'-':'+');
                
                if( !chk[next] ) Q.push(next), chk[next] = chk[now]+1;
            }
        }
    }
}




