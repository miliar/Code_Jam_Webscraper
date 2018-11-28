#include <iostream>
#include <vector>

using namespace std;

int main() {

  int nc;

  cin >> nc;

  for (int c=0;c<nc;c++) {

    int d;
    cin >> d;
    vector<int> p(d);

    int maxp = 0;
    for (int i=0;i<d;i++) {
      cin >> p[i];
      maxp = max(p[i],maxp);
    }

    int res = maxp;

    for (int i=1;i<maxp;i++) {
      int count = 0;
      for (int j=0;j<p.size();j++) {
	if (p[j] > i) {
	  count += ((p[j]-i)/i) + ((p[j]-i)%i ? 1 : 0);
	}	
      }
      res = min(res,count+i);
    }

    cout << "Case #" << c+1 << ": " << res << endl;

  }

  return 0;

}
