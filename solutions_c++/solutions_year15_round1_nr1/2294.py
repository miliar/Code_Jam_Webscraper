#include <iostream>

using namespace std;

int main() {
  int cases=0;
  cin >> cases;
  int caseNum=0;
  while (caseNum < cases) {
    caseNum++;
    int n=0;
    cin >> n;
    int last=0;
    int next=0;
    cin >> last;
    int first=last;
    n--;
    long long min1=0;
    long long min2=0;
    int most_eaten=0;
    int secondpass[n];
    for (int i=0; i<n;i++) {
	    cin >> next;
	    if (next < last) min1+=last-next;
	    if (last-next > most_eaten) most_eaten=last-next;
	    secondpass[i]=last;
	    last=next;
    }
    for (int i=0; i<n; i++) {
	    if (secondpass[i] < most_eaten)
		   min2+=secondpass[i];
	    else
		   min2+=most_eaten;
    }
    cout << "Case #" << caseNum << ": " << min1 << " " << min2 << endl;
  }
  return 0;
}

