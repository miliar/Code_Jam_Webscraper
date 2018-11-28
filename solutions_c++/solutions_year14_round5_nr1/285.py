#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;
  for (int t=1; t<=T; t++) {
    long long N,p,q,r,s;

    cin >> N >> p >> q >> r >> s;

    vector<long long> x(N);
    vector<long long> px(N+2);
    for (int i=0; i<N; i++)
      x[i]=((i*p+q) % r)+s;

    long long sum=0;
    for (int i=0; i<N; i++)
      sum += x[i];
    px[0]=px[N+1]=0;
    for (int i=1; i<N; i++)
      px[i] = x[i-1] + px[i-1];

    double answer = 0.0;
    for (int a=0; a<N; a++) {
      double big_part = px[a];

      int lo=a,hi=N-1;
      
      while (lo<=hi) {
	int b=(hi+lo)/2;
	answer = max(answer, 1.0-(double)(max( max(px[a], sum-px[b+1]), px[b+1]-px[a]))/sum);
	if (b==lo || sum-px[b+1] > px[b+1]-px[a]) 
	  lo=b+1;
	else
	  hi=b-1;	
      }
    };
    cout << setprecision(10) << "Case #" << t << ": " << answer << endl;
  };  
  return 0;
};
