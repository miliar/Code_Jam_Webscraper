#include <iostream>
#include <set>

using namespace std;

void seen_digits(set<long>* seen, long num){
  long current = num;
  while(current>0){
    seen->insert(current%10);
    //cout << seen->size() << " " << current << endl;
    current /= 10;
  }
}

void sheep(int ncase, long init){
  if(init==0){
    cout << "Case #" << ncase << ": INSOMNIA" << endl;
    return;
  }
  set<long> seen;
  seen_digits(&seen, init);
  long current = init;
  while(seen.size()<10){
    current += init;
    seen_digits(&seen, current);
  }
  cout << "Case #" << ncase << ": " << current << endl;
  return;
}

int main() {
  int ncases;
  cin >> ncases;
  for(int i=1;i<=ncases;++i){
    long current;
    cin >> current;
    sheep(i, current);
  }
  return 0;
}
