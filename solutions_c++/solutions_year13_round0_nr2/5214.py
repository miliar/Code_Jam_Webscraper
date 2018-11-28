
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
    int a[105][105];
    int b[105][105];
    int n,m,i,j,t,x=0,flag=0;
    cin >>t;
    while(x!=t){
        flag=0;
    cin >>n>>m;
    int mx=0;
    for(i=0;i<n;i++){
        mx=0;
        for(j=0;j<m;j++){
            cin >> a[i][j];
            mx = max(mx,a[i][j]);
        }
        //cout<<"i:"<<i<<endl;
        for(j=0;j<m;j++){
            b[i][j]=mx;
            //cout<<"outh: "<<b[i][j]<<endl;
        }
    }

    mx=0;
    for(i=0;i<m;i++){
        mx=0;
        for(j=0;j<n;j++){
            mx= max(mx,a[j][i]);
            //cout<<"m: "<<mx<<endl;
        }
        for(j=0;j<n;j++){
            if(b[j][i]>mx)
            b[j][i]=mx;
            //cout<<"outv: "<<b[j][i]<<endl;
        }
    }

    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            if(a[i][j]==b[i][j]){
                flag=1;
            }
            else{
                flag=0;
                break;
            }
        }
        if(flag==0){
            break;
        }
    }
    if(flag==1)
    cout<<"Case #"<<x+1<<": "<<"YES"<<endl;
    else
    cout<<"Case #"<<x+1<<": "<<"NO"<<endl;

    x++;
    }
 return 0;
}
