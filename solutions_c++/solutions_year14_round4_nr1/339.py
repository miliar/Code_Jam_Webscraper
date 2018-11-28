#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,m;
        vector<int> u;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++){
            int x;
            scanf("%d",&x);
            u.push_back(x);
        }
        sort(u.begin(),u.end());
        int ans=0;
        while(u.size()){
            int x=u.back();
            u.pop_back();
            auto t=upper_bound(u.begin(),u.end(),m-x);
            if(t!=u.begin()) u.erase(--t);
            ans++;
        }
        printf("Case #%d: %d\n",++no,ans);
    }
}
