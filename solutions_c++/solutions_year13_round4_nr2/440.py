#include<iostream>
#include<algorithm>

using namespace std;

int ok(long long N, long long P, long long k) {
  if (k==0) return 1;
  long long num = 1LL<<(N-1);
  if (P<=num) return 0;
  return ok(N-1,P-num, (k-1)/2);
}

int ok2(long long N, long long P, long long k) {
  if (k<P) return 1;
  if (P<=0) return 0;
  long long mid = 1LL<<N;
  if (k==mid-1) {
    return 0;
  }
  return ok2(N-1, P, (k+1)/2);
}

int main(){
int T;
cin>>T;
for (int t=1;t<=T;t++) {
	int N;
	cin>>N;
	long long M;
  cin>>M;
  long long mini = 0;
  long long maxi = (1LL<<N)-1;
  while (maxi-mini>0) {
    long long mid = (maxi+mini+1)/2;
    if (ok(N, M, mid)) {
      mini = mid;
    } else {
      maxi = mid-1;
    }
  }
  cout<<"Case #"<<t<<": "<<mini;
  mini = 0;
  maxi = (1LL<<N)-1;
  while (maxi-mini>0) {
    long long mid = (maxi+mini+1)/2;
    if (ok2(N, M, mid)) {
      mini = mid;
    } else {
      maxi = mid-1;
    }
  }
  cout<<" "<<mini<<endl;
}
}
