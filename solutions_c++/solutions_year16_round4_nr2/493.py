#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
const int maxn = 255;

double solve(vector<double> v){
  double prob[maxn]={0};
  prob[0]=1;
  int k = v.size();
  for(int i=0;i<k;i++){
    //  printf("%lf |",v[i]);
    for(int j=k;j>0;j--){
      prob[j]=prob[j]*(1-v[i]) + prob[j-1]*v[i];
    }
    prob[0]=prob[0]*(1-v[i]);
  }
  // printf("%lf\n",prob[k/2]);
  return prob[k/2];
}
int main(){
  int tt;
  int n,k;
  double val[maxn];
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    scanf("%d %d",&n,&k);
    double ret= 0;
    for(int i=0;i<n;i++){
      scanf("%lf",&val[i]);
    }
    sort(val,val+n);
    //    for(int i=0;i<n;i++)printf("%lf\n",val[i]);
    for(int i=0;i<=k;i++){
      vector<double> vals;
      for(int j=0;j<i;j++){
	vals.push_back(val[j]);
      }
      for(int j=0;j+i<k;j++){
	vals.push_back(val[n-1-j]);
      }
     
      if(k==(int)vals.size()){
	ret = max(ret,solve(vals));
      }
    }
    printf("Case #%d: %.6lf\n",rr,ret);
  }
  return 0;
}
