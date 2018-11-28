#include <iostream>
#include <set>

using namespace std;

bool contiene(set<int> a, int lim){
  int cont=0;
  for(int i=0; i<=lim ; ++i){
    if(a.count(i)) cont++;
  }
  if(cont==lim) return true;
  return false;
}

int main(){
  set<int> num;
  int t=0,n=0,r=1,i=2,temp=0;
  cin >> t;
  while(r<=t){
    cin >> n;
    if(n == 0) cout << "Case #" << r << ": INSOMNIA" << endl;
    else{
      temp =n;
      while(!contiene(num, 10)){
        while(temp!=0){
          num.insert(temp % 10);
          temp /= 10;
        }
        temp = n*i;
        ++i;
      }
      cout << "Case #" << r << ": " << temp-n<< endl;
    }
    r++;
    num.clear();
    i=2;
  }

  return 0;
}
