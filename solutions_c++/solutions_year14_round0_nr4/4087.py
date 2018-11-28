#include<cstdio>
#include<algorithm>
#include<functional>
#include<vector>
using namespace std;

int T;
int N;
double arr1[1005],arr2[1005];
int war, dwar;

int main(){
  scanf("%d",&T);
  for(int t=1; t<=T; t++){
    scanf("%d",&N);
    for(int i=0;i<N;i++) scanf("%lf",arr1+i);
    for(int i=0;i<N;i++) scanf("%lf",arr2+i);
    sort(arr1,arr1+N);
    sort(arr2,arr2+N);
    int k,l=0;
    war = dwar = 0;
    for(k=0;k<N;k++){
      while(l<N && arr1[k] > arr2[l]) l++;
      if(l == N){ war = N-k; break; }
      l++;
    }
    l=0;
    for(k=0;k<N;k++){
      while(l<N && arr1[k] > arr2[l]) l++;
      dwar = max(dwar, k-l+1);
    }
    printf("Case #%d: %d %d\n", t, N-dwar, war);
  }
}
