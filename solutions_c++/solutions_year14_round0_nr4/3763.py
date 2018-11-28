#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
  int T, cn=0, n, i, j;  
  
  cin>>T;
  while(cn != T) {
    cin>>n;
    vector<double> Naomi(n), Ken(n);
    int D=0, W=0;
    
    for(i=0; i<n; i++)
      cin>>Naomi[i];
    for(i=0; i<n; i++)
      cin>>Ken[i];
    
    sort(Naomi.begin(), Naomi.end());
    sort(Ken.begin(), Ken.end());
    
    j=0; i=0;
    while(i<n) {
      if(Naomi[i]>=Ken[j]) {
	j++;
	D++;
      }
      i++;
    }
    
    reverse(Naomi.begin(), Naomi.end());
    reverse(Ken.begin(), Ken.end());
    
    j=0; i=0;
    while(i<n) {
      if(Naomi[i]>Ken[j])
	W++;
      else
	j++;
      i++;
    }
    
    cout<<"Case #"<<++cn<<": "<<D<<" "<<W<<endl;
  }
  return 0;
}
