#include<iostream>
#include<iomanip>
#include<algorithm>
using namespace std;

#define ld long double
#define mp make_pair
int main (){
  int tes;
  cin>>tes;
  std::cout << std::setprecision(10) << std::fixed;

  double a[1005], b[1005]; int n;
  pair <double, int> c [1005];
  for (int it = 1;it<=tes;++it){
    cin>>n;
    for (int i=0;i<n;++i)cin>>a[i];
    for (int i=0;i<n;++i)cin>>b[i];
    for (int i=0;i<n;++i)c[i] = mp (a[i], 1);
    for (int i=n;i<2*n;++i)c[i] = mp (b[i-n], -1);
    sort (a, a+n);    sort (b, b+n); sort (c, c+2*n);

    cout<<"Case #"<<it<<": ";

    int an = 0, cr = 0;
    for (int i=0;i<2*n;++i){
      if (c[i].second == -1) cr ++ ;
      else {
	if (cr>0){
	  cr--;
	  an++;
	}
      }
    }

    cout<<an<<" ";
    int mx = -1, cur = 0;
    for (int i=2*n-1;i>=0;--i){
      cur+=c[i].second;
      mx = max (mx, cur);
    }
    cout<<mx<<"\n";
  }
  return 0;
}
