#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    
    int T,n,i,j,k;
    float inp;
    scanf("%d",&T);
    vector<float> v1;
    vector<float> v2;
    vector<float> v3;
    
    for(i=1;i<=T;++i){
        
        v1.erase(v1.begin(),v1.end());
        v2.erase(v2.begin(),v2.end());
        v3.erase(v3.begin(),v3.end());
        
        scanf("%d",&n);
        
        for(j=0;j<n;++j){
            scanf("%f",&inp);
            v1.push_back(inp);
            v3.push_back(inp);
        }
        for(j=0;j<n;++j){
            scanf("%f",&inp);
            v2.push_back(inp);
        }
        
        std::sort(v1.begin(),v1.end());
        std::sort(v2.begin(),v2.end());
        std::sort(v3.begin(),v3.end());
        k=n-1;
        
        for(j=n-1;j>=0;--j){
            //printf("%.3f#%.3f\t",v3[k],v2[j]);
            if(v3[k]<v2[j]){
                v3.erase(v3.begin());
                k--;
            }
            else k--;
        }
        
        for(j=0;j<n;++j){
            if(v1[0]<v2[j]){
                
                v1.erase(v1.begin());
            }
        }
        
        
        printf("Case #%d: %d %d\n",i,v3.size(),v1.size());
    }
    
    return 0;
}