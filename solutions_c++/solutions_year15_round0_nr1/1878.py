#include<iostream>
#include<fstream>
#include<cstring>
#include<stdio.h>
#include<assert.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define F first
#define S second
#define ll long long
#define pp pair<int,int>
#define SS system("pause")
#define INF 1000000000
#define dd double
#define vec vector<int>::iterator
using namespace std;
const int N=40;
int T,t,i,j,now,ans,n;
string s;

int main()
{freopen("A-large.in","r",stdin);
 freopen("out.txt","w",stdout);
 cin>>T;
 for(t=1;t<=T;t++){
    cin>>n;
    n++;
    cin>>s;
    ans=now=0;

    for(i=0;i<n;i++){
        if(now<i)ans+=i-now,now=i;
        now+=(int)s[i]-'0';
    }

    cout<<"Case #"<<t<<": "<<ans<<endl;
 }
 return 0;
}
