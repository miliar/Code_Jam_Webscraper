//#include <bits/stdc++.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <numeric>
#include <stack>
#include <functional>
#include <bitset>
#include <iomanip>

#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>
#include <cstdlib>

#define _ ios_base::sync_with_stdio(0);
#define ms(ar,val) memset(ar,val,sizeof(ar))
#define all(s) (s).begin(),(s).end()
#define rp1(i,s,n) for(int i=s;i<n;++i)
#define rp(i,n) rp1(i,0,n)
#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define pb push_back
#define LL long long
#define Read(x) freopen(x,"r",stdin)
#define Write(x) freopen(x,"w",stdout)
#define st(N,pos) (sts[N]=sts[N] | (1<<pos))
#define check(N,pos) ((bool)(sts[N] & (1<<pos)))
#define i_s(num)  static_cast<ostringstream*>( &(ostringstream() << num) )->str();
#define inf INT_MAX
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define PQ priority_queue
#define F first
#define S second
#define EPS 1e-11
#define hi 10

///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;


int a1[hi][hi],a2[hi][hi];
set <int> s;
int row1,row2;

int main()
{
//#if defined( rifat_pc )
    Write("out.txt");
    Read("A-small-attempt2.in");
//#endif
    int tst,cnt=1;
    cin>>tst;
    while(tst--)
    {

        s.clear();
        //scanf("%d",&row1);
        cin>>row1;
        rp(i,4)rp(j,4)cin>>a1[i][j];//scanf("%d",&a1[i][j]);
        rp(i,4)s.insert(a1[row1-1][i]);

        cin>>row2;//scanf("%d",&row2);
        rp(i,4)rp(j,4)cin>>a2[i][j];//scanf("%d",&a2[i][j]);
        rp(i,4)s.insert(a2[row2-1][i]);

        //printf("Case #%d: ",cnt++);

        int sz=(int)s.size();
        //cerr<<cnt<<"->"<<row1<<" "<<row2<<endl;

        if(sz==7)
        {
            for(int i=0; i<4; i++)
            {
                rp(j,4)
                if(a1[row1-1][i]==a2[row2-1][j]){
                    printf("Case #%d: %d\n",cnt++,a1[row1-1][i]);
                    break;
                }
            }
            //cerr<<"Working1"<<endl;
        }
        else if(sz==8)
        {
            printf("Case #%d: Volunteer cheated!\n",cnt++);
            //cerr<<"Working2"<<endl;
        }
        else
        {
            printf("Case #%d: Bad magician!\n",cnt++);
            //cerr<<"working3"<<endl;
        }
    }


    return 0;
}



