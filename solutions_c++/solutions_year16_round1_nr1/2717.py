#include<bits/stdc++.h>
using namespace std;

#define	    ll 		    long long
#define	    si(x) 		scanf("%d",&x)
#define 	sc(ch)	 	scanf(" %c",&ch);
#define 	sl(x) 		scanf("%I64d",&x)
#define 	pi(x) 		cout << x <<" "
#define 	nl 		    cout << '\n'
#define 	mp	 	    make_pair
#define     pb 		    push_back
#define 	f 		    first
#define 	se 	    	second
#define 	pii 		pair<int,int>
#define 	RESET(a)    memset(a,-1,sizeof(a))
#define 	CLEAR(a) 	memset(a,0,sizeof(a))
#define 	all(v)   	v.begin(),v.end()
#define 	trv(it,v) 	for(it=v.begin();it!=v.end();it++)
#define 	rep(i,a,b) 	for(int i=a;i<b;i++)

#define mod 	1000000007
#define MIN 	INT_MIN
#define MAX 	INT_MAX
#define INF 	1e9

int main()
{
    std::ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("3.in", "r", stdin);
        freopen("out2.in", "w", stdout);
    #endif

    int t=1,T;
        cin >>  T;
    while(t<=T)
        {
            string s;
            cin >> s;
            deque<char> Q;
            Q.pb(s[0]);
            for(int i=1; i<s.size(); i++){
                if(s[i] >= Q.front())
                    Q.push_front(s[i]);
                else
                    Q.pb(s[i]);
            }
            cout <<"Case #"<<t<<": ";
            while(!Q.empty())
            {
                cout << Q.front();
                Q.pop_front();
            }
            nl;
            t++;
        }

   return 0;
}

