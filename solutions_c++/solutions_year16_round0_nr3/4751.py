/*
*Rainto96
*Beijing University of Posts and Telecommunications School of Software Engineering
*http://blog.csdn.net/u011775691
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <climits>
using namespace std;
#define pb push_back
#define ALL(x) x.begin(),x.end()
#define VINT vector<int>
#define PII pair<int,int>
#define MP(x,y) make_pair((x),(y))
#define ll long long
#define ull unsigned long long
#define MEM0(x)  memset(x,0,sizeof(x))
#define MEM(x,val) memset((x),val,sizeof(x))
#define scan(x) scanf("%d",&(x))
#define scan2(x,y) scanf("%d%d",&(x),&(y))
#define scan3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define scan4(x,y,z,k) scanf("%d%d%d%d",&(x),&(y),&(z),&(k))
#define Max(a,b) a=max(a,b)
#define Min(a,b) a=min(a,b)
#define fuck(x) cout<<#x<<" - "<<x<<endl
int pn = 15;
int prm[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
int ans[1111];
int stk[1111];
int main()
{
    //freopen("C-small.in", "r",stdin);
    //freopen("C-small.out","w",stdout);
    int T;
    scanf("%d", &T);
    int cas = 1;
    while(T--)
    {
        int n, j;
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", cas++);
        int UP = n-2;
        for(int s = 0; (s < (1 << UP)) && j; s++)
        {
            ll cur = 1 << UP;cur+=s;cur<<=1;cur++;
            bool can = true;
            for(int i = 2; i <= 10 && can; i++)
            {
                ll gk = 0;
                for(int j = n-1; j >= 0; j--)
                {
                    gk = gk*i + ((cur & (1 << j)) != 0);
                }

                int tmp = -1;
                for(int j =0; j < pn; j++)
                {
                    if(gk%prm[j] == 0) {
                        tmp=prm[j];
                        break;
                    }
                }

                if(tmp == -1) can = false;
                else ans[i] = tmp;
            }
            if(can)
            {
                j--;
                int idx = 0;
                while(cur)
                {
                    stk[idx++] = cur & 1;
                    cur >>= 1;
                }
                while(idx--)
                {
                    printf("%d", stk[idx]);
                }
                for(int i = 2; i <= 10; i++) printf(" %d", ans[i]);
                putchar('\n');
            }
        }
        if(j) cout<<"not enough!!"<<endl;
    }
    return 0;
}
