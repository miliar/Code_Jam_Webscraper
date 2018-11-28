#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<cstdio>

using namespace std;
int A[10005];
int main(){
    int T,cas=0;
	freopen("Bl0.in","r",stdin);
	freopen("solution_Bl0","w",stdout);
    scanf("%d",&T);
    for(int cc=1;cc<=T;cc++){
        int maxi=-1,D;
        scanf("%d",&D);
        for(int i=1;i<=D;i++){
            scanf("%d",&A[i]);
            maxi=max(maxi,A[i]);
        }
        int res=maxi;
        for(int i=1;i<=maxi;i++){
            int curr=0;
	    int mx=-1;
            for(int j=1;j<=D;j++){
                if(A[j]>i){
                    curr+=((A[j]/i)+((A[j]%i==0)?0:1))-1;
                    mx=max(mx,i);
                }
                else mx=max(mx,A[j]);
            }
            curr+=mx;
            if(curr<res)res=curr;
        }
        printf("Case #%d: %d\n",cc,res);
    }
    return 0;
}
