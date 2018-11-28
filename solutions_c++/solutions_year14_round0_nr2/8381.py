#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main() {

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out","wt",stdout);
	//freopen("B.txt", "rt", stdin);
	//freopen("B.out","wt",stdout);
  int nt, len, i;
  double C, F, X, waitForX, buyCAndWaitForX, timeToBuy, increment = 2.0;
  vector<double> answer;
  cin>>nt;
  len = nt;

  while(nt--)
  {
    cin>>C;
    cin>>F;
    cin>>X;

    increment = 2.0;
    timeToBuy = C/increment;
    waitForX = X/increment;
    increment += F;
    buyCAndWaitForX = timeToBuy + X/increment;

    while(waitForX > buyCAndWaitForX)
    {
      waitForX = buyCAndWaitForX;
      timeToBuy += C/increment;
      increment += F;
      buyCAndWaitForX = timeToBuy + X/increment;
    }

    answer.push_back(min(waitForX, buyCAndWaitForX));
  }

  cout<<setprecision(7);
  cout<<fixed;
	for(i=0;i<len;i++)
  {
    cout<<"Case #"<<i+1<<": "<<answer[i]<<endl;
  }

	return 0;
}
