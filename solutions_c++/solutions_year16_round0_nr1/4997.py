#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,a,b,tc=0;
    lli n;
    scanf("%d",&t);
    while(t--){
        scanf("%lld",&n);
        int arr[10]={0};
        if(n==0){
            printf("Case #%d: INSOMNIA\n",++tc);
            continue;
        }
        lli x=1,y=n,z;
        while(1){
            z=n*x;
            y=z;
            x++;
            while(y > 0 ){
                a=y%10;
                arr[a]=1;
                y/=10;
            }
            bool ok=true;
            for(i=0;i<10;i++){
                if(arr[i]==0)ok=false;
            }
            if(ok){
                printf("Case #%d: %lld\n",++tc,z);
                break;
            }
        }
    }



    return 0;
}

