//#include<iostream>
//#include<cstdio>
//#include<cstring>
//#include<cmath>
//using namespace std;
//#define maxN 1005
//#define INF 0X7F7F7F7F
//
//int dp[maxN];
//int interrupt[maxN];
//
//int DP() {
//  dp[0] = 0;
//  dp[1] = 1;
//  interrupt[1] = 0;
//  for(int i = 1;i <= 1000;i++) {
//    dp[i] = i;
//    interrupt[i] = 0;
//    for(int j = 1;j < i;j++) {
//        if(dp[i] > max(dp[j]-interrupt[j],dp[i-j]-interrupt[i-j])+1+interrupt[j]+interrupt[i-j]) {
//            dp[i] = max(dp[j]-interrupt[j],dp[i-j]-interrupt[i-j])+1+interrupt[j]+interrupt[i-j];
//            interrupt[i] = 1+interrupt[j]+interrupt[i-j];
//        }
//    }
//  }
//  return 0;
//}
//
//int main()
//{
//{
//    freopen("B-small-attempt2.in","r",stdin);
//    //freopen("in.txt","r",stdin);
//    freopen("out2.txt","w",stdout);
//    int T;
//    int D,P,tmpP;
//    int eatTime,interruptTime;
//    memset(dp,0,sizeof(dp));
//    scanf("%d",&T);
//    DP();
//    for(int i = 1;i <= T;i++) {
//        printf("Case #%d: ",i);
//        eatTime = -1;
//        interruptTime = 0;
//        scanf("%d",&D);
//        while(D--) {
//            scanf("%d",&tmpP);
//            eatTime = max(eatTime,dp[tmpP]-interrupt[tmpP]);
//            interruptTime += interrupt[tmpP];
//        }
//        printf("%d\n",interruptTime+eatTime);
//    }
//    return 0;
//}
