#include <iostream>
#include <cstdio>
using namespace std;

int main(){
   int T;
   cin >> T;
   
   for(int t=1; t<=T; t++){
      double C,F,X;
      cin >> C >> F >> X;
      double now_cokkie = 2.0;
      double ans = (X / 0.000001) / (now_cokkie * 1000000);
      double time = 0;

      int cnt = 0;
      while(true){
	 cnt++;
	 if(cnt == 100010)break;
	 time += (C / 0.000001) / (now_cokkie * 1000000);
	 now_cokkie += F;
	 ans = min(ans,time + ((X / 0.000001) / (now_cokkie * 1000000)));
      }

      printf("Case #%d: %.7f\n",t,ans);
      
   }
   return 0;
}
