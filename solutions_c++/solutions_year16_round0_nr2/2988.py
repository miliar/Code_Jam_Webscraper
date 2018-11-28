#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define ff first
#define ss second

int main(){
    freopen ("B-large.in", "r", stdin);
	freopen ("ans.out","w",stdout);
    int t;
    cin >> t;
    for(int z = 1; z <= t;++z){

        string y;
        cin >> y;
        int i = 0 , k = y[0] == '-'  ? 1 : 0 , ans = 0;
        while(i+1 < y.length()){

            if(y[i+1] == y[i])++i;
            else{
                y[i] = y[i] == '-'? '+' : '-';
                ++ans;
                k = y[i+1] == '-'  ? 1 : 0;
                ++i;
            }

        }
        printf("Case #%d: %d\n" , z , ans+k);


    }

    return 0;
}
