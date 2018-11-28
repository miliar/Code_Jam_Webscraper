#include <bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int a[10],t,count,c;
  long long int n,val,temp;

  cin >> t;
  for(int i=0;i<t;i++){
    cin >> n;
    count = 0;
    fill(a,a+10,0);
    val = 0;
    if(n == 0){
      cout << "Case #" << i+1 << ": INSOMNIA\n";
    }else{
      while(count < 10){
        val += n;
        temp = val;
        while(temp){
          c = temp % 10;
          if(a[c] == 0){
            a[c] = 1;
            count++;
          }
          temp /= 10;
        }
      }
      cout << "Case #" << i+1 << ": " << val << '\n';
    }
  }

  return 0;
}
