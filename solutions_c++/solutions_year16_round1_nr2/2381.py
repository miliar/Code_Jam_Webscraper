	// #CodeLikeTheMartian
#include <bits/stdc++.h>

#define     MOD       1000000007
#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     lb        lower_bound
#define     ub        upper_bound
#define     SIZE      1000001
#define     MAX       INT_MAX
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;
int arr[51][51];
int cnt[2507];
bool row[51];
bool col[51];
int N;
pair<int,int> getPos(int v)
{
    if(arr[0][0]==0)
    return mp(0,0);
    for(int i=0;i<N;++i)
        if(arr[0][i]==v)
            return mp(0,i);
        else if(arr[i][0]==v)
            return mp(i,0);
}
int main()
{
    int T;
    //FILE *fp=fopen("A_smallOutput.txt","w");
    cin>>T;
    for(int t=1;t<=T;++t)
    {

        memset(arr,0,sizeof(arr));
        memset(cnt,0,sizeof(cnt));
        cin>>N;
        for(int i=0;i<(2*N-1);++i)
        {
            for(int j=0;j<N;++j)
            {
                 cin>>arr[i][j];
                 ++cnt[arr[i][j]];
            }

        }
        cout<<"Case #"<<t<<": ";
        for(int i=1;i<=2500;++i)
            if(cnt[i]>0&&cnt[i]&1)
                cout<<i<<" ";
        cout<<endl;


    }
	return 0;
}

