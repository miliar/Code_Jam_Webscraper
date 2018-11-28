#include<iostream>

using namespace std;

int ar[10001];
bool used[10001];
int main() {
  int cas; 
  cin>>cas;
  for(int ca=1; ca<=cas; ++ca) {
    int n, x;
    cin>>n>>x;
    memset(used, 0, sizeof(used));
    for(int i=0 ;i<n; ++i) {
      cin>>ar[i];  
    }
    sort(ar, ar + n);
    int end = n;
    int rtn = 0;
    for(int i=0 ;i<n; ++i) {
      if (used[i]) continue;
      int cur = ar[i];
      bool found = false;
      while (end > i) {
        end--;
//        cout<<cur+ar[end] <<" "<<x<<endl;
        if (cur+ar[end] <=x ) {
//          cout<<"found"<<endl;
          found = true; 
          used[end] = true;
          break;
        }
      }
      rtn++;
    }
    printf("Case #%d: %d\n", ca, rtn);
  }
}
