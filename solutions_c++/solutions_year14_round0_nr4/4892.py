#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
    {
      int j,i,k,n,ans_1=0,ans_2=0;
      cin>>n;
      double KEN[n],NAO[n];
      for(i=0;i<n;i++)
          scanf("%lf",&NAO[i]);
      sort(NAO,NAO+n);
      i=0;
      for(j=0;j<n;j++)
          scanf("%lf",&KEN[j]);
      sort(KEN,KEN+n);
      j=0;
      while(j<n && i<n){
      if(NAO[i]>KEN[j])
        ans_1++, i++,j++;
      else
        i++;}
      i=0,j=0;
      while(j<n && i<n) {
          if(NAO[i]<KEN[j])
                    ans_2++, i++,  j++;
          else
            j++;}
      cout<<"Case #"<<t<<": "<<ans_1<<" "<<n-ans_2<<endl;;
    }
  return 0;
}
