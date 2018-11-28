#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long ll;
typedef long long int lli;
#define mp make_pair
#define pb push_back

const int maxint=60000;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("inp.out", "w", stdout);
    int t; cin>>t;
    int n;
    double naomi[1001];
    double ken[1001];
    int start = 1;
    while(start<=t){
        cin>>n;
        memset(naomi,0,sizeof(naomi));
        memset(ken,0,sizeof(ken));
        for(int i=1;i<=n;i++){
            cin>>naomi[i];
        }
        sort(naomi+1,naomi+n+1);
        for(int i=1;i<=n;i++){
            cin>>ken[i];
        }
        sort(ken+1,ken+n+1);
        int i=1, j=1;
        int fake = 0, no_fake = 0;
        //War first
        while(i<=n){
            while(j<=n && ken[j]<naomi[i]){
                j++;
            }
            if(j>n)break;
            i++;j++;
        }
        if(i<=n)no_fake += n-i+1;
        i=1; j=1;
        while(j<=n){
            while(i<=n && naomi[i]<ken[j]){
                i++;
            }
            if(i>n)break;
            i++;j++;
            fake++;
        }
        printf("Case #%d: %d %d\n",start,fake,no_fake);
        start++;
    }
//    for(int i=1;i<=n;i++){
//        cout<<naomi[i]<<" ";
//    }
//    cout<<endl;
//    for(int i=1;i<=n;i++){
//        cout<<ken[i]<<" ";
//    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
