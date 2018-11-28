#include <bits/stdc++.h>
using namespace std;
bool found;
int main(){
    int T, cases=1;
    freopen("B-large-attempt0.in", "r", stdin);
    freopen("B-large-attempt0.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        string l;
        int ans=0;
        found = false;
        cin>>l;
        for(int i=0;i<l.size();i++){
            if(l[i]=='+')found=true;
            else{
                if(found)ans+=2;
                else ans++;
                while(i<l.size()&&l[i]=='-')i++;
                found=true;
                i--;
            }
        }
        printf("Case #%d: %d\n", cases++, ans);
    }
    return 0;
}
