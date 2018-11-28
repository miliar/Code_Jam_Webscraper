//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
//Other Includes
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<utility>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
//some common functionn
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define FOR(i,a,b)              for(int i=a;i<b;i++)
#define FORs(i,a,b)             for(int i=a;i>=b;i--)
#define fill(a,v)               memset(a,v,sizeof a)
#define abS(x)                  ((x)<0?-(x):(x))
#define mP                      make_pair
#define pB                      push_back
#define error(x)                cout << #x << " : " << (x) << endl
#define ALL(a)                  (a).begin(),(a).end()
#define SZ(a)                   ((int) a.size())
#define SORT(a)                  sort(ALL(a))

using namespace std;

typedef long long LL;



void chekarre(int * arr,int n)
{
    cout<<"[";
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<"]"<<endl;
}

bool comp(int i,int j) { return (i>j); }


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

       long int arr[]={0,1,2,3,11,22,101,111,121,202,212,
 1001,1111,2002,10001,10101,10201,11011,
 11111,11211,20002,20102,100001,
 101101,110011,111111,200002,1000001,
 1001001,
 1002001,
 1010101,
 1011101,
 1012101,
 1100011,
 1101011,
 1102011,
 1109111,
 1110111,
 1111111,
 2000002,
 2001002,
};

    int t,i,j,x=0;
    long long a,b,cnt=0;
    long long r[100];

    for(i=0;i<41;i++){
      r[i]=pow(arr[i],2);
    }

    cin >> t;

    while(x!=t){
        cnt=0;
        cin >> a>>b;
        for(j=0;j<41;j++)
        {
            if(r[j]>=a && r[j]<=b)
            cnt++;
        }
        cout<<"Case #"<<x+1<<":"<<" "<<cnt<<endl;
        x++;
    }

    return 0;
}
