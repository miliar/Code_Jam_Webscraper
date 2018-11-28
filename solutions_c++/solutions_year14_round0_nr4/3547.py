#include<iostream>
#include<cmath>
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<string.h>
#include<ctime>
#include<map>
#include<assert.h>
using namespace std;
typedef long long LL;



int main(){

    int t,n,x,y;
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    int N=t;
    while(t--){

        x=y=0;
        cin>>n;

        double arr[n],arrc[n];
        double brr[n],brrc[n];

        for(int i=0;i<n;i++)
            cin>>arr[i];

        for(int i=0;i<n;i++)
            cin>>brr[i];

        sort(arr,arr+n);
        sort(brr,brr+n);

        for(int i=0;i<n;i++)
            arrc[i]=arr[i],brrc[i]=brr[i];

        int x=0,y=0;

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(brr[j]&&brr[j]<arr[i]){
                    x++;brr[j]=0;arr[i]=0;
                    break;
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(brrc[j]&&brrc[j]>arrc[i]){
                    y++;brrc[j]=0;
                    break;
                }
            }
        }

        cout<<"Case #"<<N-t<<": ";
        cout<<x<<' '<<n-y<<endl;

    }

    return 0;
}
