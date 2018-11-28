#include <bits/stdc++.h>
#include <utility>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


#define mod 1000000007
#define maxs 1000000
#define array_size_limit 5000005
#define mins -1000000000
#define eps 0.000000000001
#define imax 2000000200
#define llmax 1000000002000000000ll


#define LL long long int
#define pb push_back
#define mp make_pair
#define gc getchar_unlocked
#define iosbase ios_base::sync_with_stdio(false)
#define pii pair<int,int>
#define pLL pair<LL,LL>
#define ppi pair<pair<int,int>,int>
#define ppl pair<pLL,LL>
#define vi vector<LL>
#define sc scanf
#define pr printf
#define lld I64d
#define F first
#define S second
#define siter set<int>::iterator
#define p_pq priority_queue
#define ub upper_bound
#define lb lower_bound
#define PI acos(-1)
#define CLEAR(A) memset(A,0,sizeof(A))
#define SETMAX(A) memset(A,0x7f,sizeof(A))
#define graph(n) vector<vector<pLL> >graph(n);



LL djik (LL src,LL des, vector<vector<pLL> > graph)
    {
        p_pq<pLL> que;
        que.push(mp(0, src));
        LL n = graph.size();
        vector<LL> distance(n,imax);

        LL nd, ed, ln;
        distance[src] = 0;

        while (1)
            {
                nd = (que.top()).second;
                ed = -(que.top()).first;
                if (nd == des)
                    return ed;
                que.pop();
                if (distance[nd] < ed)
                    continue;
                ln = graph[nd].size();

                for (int i = 0; i < ln; i++)
                    {
                        LL x = graph[nd][i].second;//cost
                        LL y = graph[nd][i].first;//node
                        if (ed + x < distance[y])
                            que.push(mp(-(distance[y] = ed + x), y));
                    }
            }

    }




set<LL> inset(LL n,set<LL> myset)
    {
        LL tmp=n;
        while(tmp)
            {
                myset.insert(tmp%10);
                tmp /= 10;
            }
        return myset;
    }




int main()
{
	iosbase;
	LL t,n;
    cin>>t;
    //t = 300;
    for (int i = 0; i < t; i++)
    {
        LL flag=0;
        cin>>n;
        //n = maxs+i;
        set<LL> myset;
        myset = inset(n,myset);
        //cout<<myset.size()<<endl;

        LL j=2;
        for (j = 2; j < maxs ; j++) {
            if(myset.size() == 10)
                {
                    flag = 1;
                    break;
                }

                myset = inset(j*n,myset);

        }

        if(flag)
            cout<<"Case #"<<i+1<<": "<<(j-1)*n<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;

    }
	return 0;
}