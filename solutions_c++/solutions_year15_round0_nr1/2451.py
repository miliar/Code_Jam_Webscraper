#include <iostream>
#define REP(i, a, b)\
    for(int i = (int )a; i<=(int)b; i++)

using namespace std;

int main()
{
    int t; cin>>t;
    int count = 0;

    while(t--){
        count++;
        int n;
        cin>>n;
        string s ;
        cin>>s;

        int a[n+1];
        REP(i,0 ,n){
            a[i] = s[i]-'0';
        }
        REP(i, 1, n){
            a[i] += a[i-1];
        }
        int ans = 0;

        REP(i, 1, n){
            if(i>a[i-1]+ans && a[i]!=0){
                ans += i - a[i-1]-ans;
            }
        }

        cout<<"Case #"<<count<<": "<<ans<<endl;
    }

    return 0;
}


