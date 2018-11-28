#include<cstdio>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int i=0;i<T;i++){
    printf("Case #%d: ", i+1);

    int arr[1001];
    int N;
    scanf("%d", &N);
    for(int j=0;j<N;j++){
      scanf("%d", &arr[j]);
    }

    int max=-1;
    int ans1=0;
    for(int j=1;j<N;j++){
      int temp=arr[j-1]-arr[j];
      if(temp<0)
        temp=0;

      if(max<temp)
        max = temp;

      ans1+=temp;
    }
    int ans2=0;
    for(int j=0;j<N-1;j++){
      if((arr[j]-max)>0)
        ans2+=max;
      else
        ans2+=arr[j];
    }

    printf("%d %d\n", ans1, ans2);
  }
}
