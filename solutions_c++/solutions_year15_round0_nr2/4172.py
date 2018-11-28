#include<stdio.h>
#include<stdlib.h>
int pake[2048];
int max(int a,int b){
    return (a > b) ? a : b;
}

int d(int maxD, int l){
    int m = 0, m_index = -1;;
    for(int i=0;i<maxD;i++){
        if(m < pake[i]){
            m = pake[i];
            m_index = i;
        }
    }
    if(l > 10)return m;
    if(m == 2){
        //for(int i=0;i<maxD;i++)printf("%d ",pake[i]);
        //printf("\n");
        return 2;
    }
    int ans = m;
    for(int i=1;i<=m / 2;i++){
        //printf("l = %d i = %d\n",l,i);
        pake[maxD] = i;
        pake[m_index] -= i;
        int tmp_ans = d(maxD + 1, l + 1);
        pake[m_index] += i;
        pake[maxD] = 0;
        if(ans > tmp_ans + 1) ans = tmp_ans + 1;
    }
    return ans;

}
int main(){
    int T;
    scanf("%d",&T);
    for(int ca = 0;ca < T; ca++){
        int D;
        for(int i=0;i<2048;i++) pake[i] = 0;
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf("%d",&pake[i]);
        }
        int ans = d(D, 0 );
        printf("Case #%d: %d\n",ca + 1, ans);
        
    }
    return 0;
}
