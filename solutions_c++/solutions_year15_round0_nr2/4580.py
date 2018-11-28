// Aditya Varshney - coderaditya

#include <iostream>
#include <bitset>
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <climits>

#define pb push_back
#define mp make_pair

typedef long long int ll;

using namespace std;

#define getcx getchar//_unlocked

ll scan()
{
    ll n=0;
    char ch = getcx();
    int sign=1;
    while( ch < '0' || ch > '9' ) {
        if(ch=='-')
            sign = -1;
        ch=getcx();
    }
    while( ch >= '0' && ch <= '9' ) {
        n = (n<<3)+(n<<1) + ch-'0';
        ch=getcx();
    }
    return(n * sign);
}

int mini;

void rece(int maxi, priority_queue <int> pq, int ans) {
    if(maxi <= ans) {
        return;
    }
    mini = min(mini,pq.top()+ans);
    if(pq.top() != 1) {
        int fin = pq.top();
        pq.pop();
        for(int i=1;i<=fin/2;i++) {
            priority_queue<int> temp;
            temp = pq;
            temp.push(i);
            temp.push(fin - i);
            rece(maxi,temp,ans+1);
        }
    }
}

int main()
{
    freopen("in1.in","r",stdin);
    freopen("out3.txt","w",stdout);
    int i,x,t,p=0,n,maxi;
    t=scan();
    while(t--) {
        p++;
        n=scan();
        mini = INT_MAX;
        priority_queue <int> pq;
        maxi = INT_MIN;
        for(i=0;i<n;i++) {
            x=scan();
            maxi = max(maxi,x);
            pq.push(x);
        }
        rece(maxi,pq,0);
        printf("Case #%d: %d\n", p,mini);
    }
    return 0;
}
