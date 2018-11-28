/** ========================================**
 ** Bismillahi-Rahamanirahim.
 ** @Author: A Asif Khan Chowdhury
 /** ========================================**/

#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <deque>
#include <strings.h>
#include <cstdio>
#include <set>
#include <list>

using namespace std;

#define Set(N, j) (N|(1<<j))
#define reset(N, j) (N&~(1<<j))
#define Check(N, j) (bool)(N&(1<<j))
#define toggle(N, j) (N^(1<<j))
#define turnOff(N, j) (N & ~(1<<j))
#define CLEAR(A, x) ( memset(A,x,sizeof(A)) )
#define pii pair <int, int>
#define pb push_back
#define open freopen("D:/a.txt", "r", stdin);
#define write freopen("D:/b.txt","w", stdout);
#define inf (1ll<<28)
#define ll long long
#define mod 1000000007
#define gc getchar
#define ls(n) (n<<1)
#define rs(n) ls(n)|1
#define MID(a,b) ((a+b)>>1)
#define fs first
#define sc second
#define mx 100010

template<class T>inline bool read(T &x) {
    int c=getchar();
    int sgn=1;
    while((~c&&c<'0')||c>'9') {
        if(c=='-')sgn=-1;
        c=getchar();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=getchar())x=x*10+c-'0';
    x*=sgn;
    return ~c;
}
//int X[]= {-1, -1, -1, 0, 1, 1, 1, 0};   //x 8 direction
//int Y[]= {-1, 0, +1, 1, 1, 0, -1, -1};  //y 8 direction
int X[]= {-1, 0, 1, 0};   //x 4 direction
int Y[]= { 0, 1, 0, -1};  //y 4 direction

int n;
pii arr[30];

bool comp(pii a, pii b){
    
    return a.fs>b.fs;
}

int main() {
#ifdef DEBUG
    freopen("/Users/abuasifkhan/Desktop/Programming/ProblemSolving/ProblemSolving/a.in", "r", stdin);
    freopen("/Users/abuasifkhan/Desktop/Programming/ProblemSolving/ProblemSolving/b.out", "w", stdout);
#endif
    
    int test;
    read(test);
//    cout<<test<<endl;
    for(int C=1; C<=test; C++) {
        scanf("%d",&n);
        int sum=0;
        
        pii a[30];
        
        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
            a[i].first=x;
            a[i].second=i;
            sum+=a[i].first;
            
        }
        printf("Case #%d: ",C);
        
        while(sum>0)
        {
            sort(a,a+n);
            if(a[n-1].first==a[n-2].first and sum!=3)
            {
                cout<<char('A'+a[n-1].second)<<char('A'+a[n-2].second)<<" ";
                a[n-1].first--;
                a[n-2].first--;
                sum-=2;
            }
            
            else
            {
                cout<<char('A'+a[n-1].second)<<" ";
                a[n-1].first--;
                sum--;
            }
        }
        printf("\n");
    }
    
    return 0;
}








