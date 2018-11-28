#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<cstring>
#include<set>
#include<sstream>
#include<string>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#define MAX 100000000000005

using namespace std;
bool arr[1005]={false};
int main()
{
  //  ios_base::sync_with_stdio(false);
    freopen("C-small-attempt0 (1).in","r",stdin);
  freopen("C.out","w",stdout);
    arr[1]=arr[4]=arr[9]=arr[121]=arr[484]=true;
    int t,test=0;
    cin>>t;
    while(t--)
    {
        long long a,b;
        cin>>a>>b;
        int res=0;
        for(int i=a;i<=b;i++)if(arr[i])res++;
        cout<<"Case #"<<++test<<": "<<res<<endl;

    }

    return 0;

}
