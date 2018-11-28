#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;
void get_digits(set<int>& s, int num){
	do {
		s.insert( num % 10);
    	num /= 10;
    } while (num>0);
}
void solve(){
	int num;
	set<int>s1;
	set<int>s2;
	for (int i = 0; i < 10; ++i){
		s2.insert(i);
	}
	cin >> num;
	set<int>::iterator iter;
	if(num>9){
		get_digits(s1,num);
	}else {
		s1.insert(num);
	}
    if (num==0){
    	cout << "INSOMNIA" << endl;
    } else {
        int res;
    	int n = 1;
        while(s1!=s2) {
        	n+=1;
        	res =num * n;
        	if(res>9){
        		get_digits(s1,res);
	        }else {
	        	s1.insert(res);
	        }
        }
        cout << res << endl;
    }

}
int main() {
  int tn;
  scanf("%d", &tn);
  for(int t = 0;t<tn;t++){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}