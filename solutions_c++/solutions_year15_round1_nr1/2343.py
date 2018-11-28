#include<bits/stdc++.h>

using namespace std;

int main(){

    int T,cs,n,minAny, minConst,msInPlate[1005],mxDiff,i;
    scanf("%d", &T);

    for(cs=1;cs<=T;cs++){
        scanf("%d",&n);
        minAny=0;
        minConst=0;
        mxDiff = 0;
        for(i=0;i<n;i++){
            scanf("%d",&msInPlate[i]);
            if(i>0&&mxDiff<msInPlate[i-1]-msInPlate[i])
                mxDiff = msInPlate[i-1]-msInPlate[i];
        }

        for(i=1;i<n;i++){
            if(msInPlate[i]<msInPlate[i-1])
                minAny+=(msInPlate[i-1]-msInPlate[i]);
        }
                

        for(i=0;i<n-1;i++){
            if(msInPlate[i]>=mxDiff) minConst+=mxDiff;
            else minConst+=msInPlate[i];
        }


        printf("Case #%d: %d %d\n",cs,minAny,minConst);
        
    }

    return 0;
}
