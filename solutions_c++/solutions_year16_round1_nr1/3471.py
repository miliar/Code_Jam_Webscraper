#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large_1A.out","w",stdout);
    int t,j=1;
    scanf("%d",&t);
    while(t--){
        string str;
        cin >> str;
        string ans;
        ans.insert(ans.begin(),str[0]);
       // cout << ans << endl;
        int len = str.length(),i;
        for(i=1; i<len; i++){
            if(str[i] >= ans[0])
                ans.insert(ans.begin(),str[i]);
            else
                ans.insert(ans.end(),str[i]);
        }
        printf("Case #%d: ",j);
        cout << ans << endl;
        j++;
    }
    return 0;
}
