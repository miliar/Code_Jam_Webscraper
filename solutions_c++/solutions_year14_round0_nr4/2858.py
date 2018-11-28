#include<iostream>
#include<algorithm>
using namespace std;
bool func(double a,double b){
     return a > b;
}
int main(){
    int t,n,ans1=0,ans2=0;
    double na[1001],ken[1001];
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
      ans1 = 0;
      ans2 = 0;
      scanf("%d",&n);
      for(int i=0;i<n;i++){
       scanf("%lf",&na[i]);
      }
      for(int i=0;i<n;i++){
       scanf("%lf",&ken[i]);
      }
      sort(na,na+n,func);
      sort(ken,ken+n,func);
      /*
      for(int i=0;i<n;i++)
      {
              printf("%lf ",na[i]);
      }
      printf("\n");
      
      for(int i=0;i<n;i++)
      {
              printf("%lf ",ken[i]);
      }
      printf("\n");
      */
      int start1 = 0;
      int start2 = 0;
      int end1 = n-1;
      int end2 = n-1;
      
      for(int i=0;i<n;i++){
         if(na[end1] > ken[end2]){
          ++ans1;
          end2--;
         }
         else{
          if(na[end1] > ken[start2]) ans1++;
          start2++;
          
         }
         end1--;
      }
     
      int j = n-1;
      
      for(int i=n-1;i>=0;i--){
        if(j<0)
         break;
        while(j >= 0 && ken[j] < na[i]){
          j--;
        }
        if(na[i] <= ken[j])
         {
          ++ans2;
          j--;
         }
      }
      
      ans2 = n - ans2;
      
      printf("Case #%d: %d %d\n",tc,ans1,ans2);
      
    }
    
    return 0;
}
