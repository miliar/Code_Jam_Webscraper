#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;

bool isUpandDown(vector<int> & w){
    int mx=0;
    for(int i = 1 ; i <w.size() ; ++ i ){
        if(w[i]>w[mx])mx=i;
    }

    for(int i = 1 ; i < mx ; ++ i ){
        if(w[i]<w[i-1])return false;
    }
    for(int i = mx+1;i<w.size() ; ++ i ){
        if(w[i]>w[i-1])return false;
    }
    return true;
}
int countDiff(vector<int> origin,vector<int> &dest){
    int ret=0;
    for(int i = 0 ; i < dest.size() ; ++ i ){
        if(dest[i]!=origin[i]){
            for(int j = i +1 ; j < origin.size() ; ++ j ){
                if(dest[i]==origin[j]){
                    while(dest[i]!=origin[i]){
                        swap(origin[j],origin[j-1]);
                        j--;
                        ret++;
                    }
                    break;
                }
            }
        }
    }
    return ret;
}


void solve(vector<int> v){
    vector<int> w = v;
    sort(w.begin(),w.end());
    int ans=1000000;
    vector<int> ansV;
    do{
        if(isUpandDown(w)){
            int z = countDiff(v,w);
            if(z<ans){

                ans=z;
                ansV=w;
            }
        }
    }while(next_permutation(w.begin(),w.end()));
    printf("%d\n",ans);


}

int getAns(vector<int> v,int med){
    int ret=0;
    for(int i = 1;i<med;++i){
        int j=i;
        while(j&&v[j]<v[j-1]){
            swap(v[j],v[j-1]);
            j--;
            ret++;
        }
    }
    for(int i = med+1;i<v.size() ; ++ i ){
        int j=i;
        while(v[j]>v[j-1]){
            swap(v[j],v[j-1]);
            j--;
            ret++;
        }
    }
    return ret;
}

void solveLarge(vector<int> v){
    int mx=0;
    int ans=0;

    while(v.size()>0){
        mx=0;
        for(int i = 1 ; i < v.size() ; ++ i ) if(v[i]<v[mx])mx=i;
        ans+=min(mx, int(v.size()-1-mx));
        v.erase(v.begin()+mx);

    }

    printf("%d\n",ans);

}

int main(){
    freopen("B-large"".in","r",stdin);
    freopen("B-large"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        int n;
        vector<int> v;
        scanf("%d",&n);
        for(int i = 0 ; i < n ; ++ i ){
            int k;
            scanf("%d",&k);
            v.push_back(k);
        }
        //solve(v);
        solveLarge(v);
    }
}
