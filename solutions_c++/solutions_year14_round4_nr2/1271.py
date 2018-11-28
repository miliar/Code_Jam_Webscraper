#include<bits/stdc++.h>

using namespace std;

#define vi vector < int >
#define pb push_back
#define mp make_pair
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define INF 2000000000
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define all(x) x.begin(),x.end()

int a[1003];
int b[1003];

int check(int n){
    int i = 1;
    while(i < n && a[i-1] < a[i])
        i++;
    while(i < n && a[i-1] > a[i])
        i++;
    return i == n;
}

int hs[1004];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    int t,i,j,tc=1;
    cin>>t;
    while(t--){
        int n;
        scanf("%d",&n);
        for(i=0;i<n;i++){
            cin>>a[i];
            b[i] = a[i];
        }
        sort(b,b+n);
        int sz = int(unique(b,b+n)-b);
        for(i=0;i<n;i++){
            a[i] = 1 + int(lower_bound(b,b+sz,a[i])-b);
            hs[a[i]] = i;
        }
        int ans = INF;
        int p[1004];
        for(i=0;i<n;i++){
            hs[a[i]]=i;
        }
        if(check(n)){
            printf("Case #%d: %d\n",tc++,0);
            continue;
        }
        sort(a,a+n);
        do{

            if(!check(n))
                continue;
            int l = 0;
            for(i=0;i<n;i++){
                for(j=i+1;j<n;j++){
                    if(hs[a[i]] > hs[a[j]])
                        l++;
                }
            }
            if(ans == 1)
                break;
            ans = min(ans,l);
        }while(next_permutation(a,a+n));
        assert(ans != INF);
        printf("Case #%d: %d\n",tc++,ans);
    }
    //system("pause");
    return 0;
}
