#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

using namespace std;

typedef long long in;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int test=1;test<=t;test++){
    in n;
    cin >> n;
    if(n==0){
      cout << "Case #" << test << ": INSOMNIA" << endl;
      continue;
    }
    in a;
    in d;
    int ct=0;
    vector<int> had(10);
    for(in i=1;i<=1000;i++){
      a=n*i;
      while(a!=0){
	d=a%10;
	if(had[d]==0){
	  had[d]=1;
	  ct++;
	}
	a/=10;
      }
      if(ct==10){
	cout << "Case #" << test << ": " << n*i << endl;
	break;
      }
    }
    if(ct!=10){
      cout << "Case #" << test << ": INSOMNIA" << endl;
    }
  }
  return 0;
}
      
    
  