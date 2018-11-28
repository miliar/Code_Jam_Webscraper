#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define MOD 1000000007
#define LIMIT 100000
#define MASK (1<<16) - 1

inline void readint(int *var)
{
    register char ch=0;
    *var=0;
    while (ch<33)
        ch=getchar_unlocked();
    //Consider only numerals
    while (ch>47 && ch<58)
    {
        *var=(*var * 10) + (ch-'0');
        ch=getchar_unlocked();
    }
}

int main(){
    int t, n, i, k,  count = 0;
    long long sum = 0, temp;
    char a[1005];
    cin>>t;
    rep(k,t){
        cin>>n;
        count = 0;
        sum = 0;
        scanf("%s", a);

        rep(i,n+1){
            if(sum<i){
 //               cout<<"i "<<i<<endl;
                temp = i - sum;
                count +=temp;
                sum = i;
                sum+=(a[i]-'0');
            }else
                sum+=(a[i]-'0');

        }
        cout<<"Case #"<<(k+1)<<": "<<count<<endl;

    }
	

}
