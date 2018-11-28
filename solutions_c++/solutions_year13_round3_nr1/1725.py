#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t;++i){
        string s;
        int n;
        cin>>s>>n;
        int ans=0;
        for(int l=1;l<=s.size();++l){
            for(int ii=1;ii<=s.size()-l+1;++ii){
                int jj=ii+l-1;
                int flag=0;
                int i1,i2;
                i1=ii-1;
                i2=jj-1;
                int idx1,idx2;
                idx1=i1;
                idx2=i1;
                //cout<<ii<<" "<<jj<<endl;
                while(idx1<=i2 && idx2<=i2){
                    if(s[idx2]=='a' || s[idx2]=='e' || s[idx2]=='i' || s[idx2]=='o' || s[idx2]=='u'){
                        idx1=idx2+1;
                        idx2++;
                    }
                    else
                        idx2++;
                    if(idx2-idx1==n){
                        flag=1;
                        break;
                    }
                }
                if(flag)
                    ans++;
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
