#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq=1;qq<=tt;qq++) {
        printf("Case #%d: ", qq);
        int n;
        cin>>n;
        vector<char> s(n+1);
        for(int i=0; i<=n; i++){
            cin>>s[i];
        }

        int missing=0, count=s[0]-'0';
        for(int i=1; i<=n; i++){
            if(s[i]>='1'){
                if(count<i){
                    missing+=i-count;
                    count+=missing+s[i]-'0';
                }
                else{
                    count+=s[i]-'0';
                }
            }
        }
        cout<<missing<<endl;
    }
    return 0;
}
