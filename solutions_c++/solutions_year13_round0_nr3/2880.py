#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

bool palin(int x){
	int qian = x / 1000;
	int bai = x % 1000 / 100;
	int shi = x / 10 % 10;
	int ge = x % 10;
	if(qian != 0){
	   if(ge == qian && shi == bai)
		   return true;
	   return false;
	}
	else if(bai != 0){
	   if(ge == bai)
		   return true;
	   return false;
	}
	else if(shi != 0){
	   if(ge == shi)
		   return true;
	   return false;
	}
	else{
	  return true;
	}
}

int main(){
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	int numcase;
	cin >> numcase;
	for(int cnt = 1; cnt <= numcase; ++cnt){
	   int lv,rv;
	   cin >> lv >> rv;
	   int ans = 0;
	   for(int i = lv; i <= rv; ++i){
	      int x = sqrt(double(i));
		  if(x * x != i)
			  continue;
		  if(palin(x) && palin(i)){
			  ans++;
		  }
	   }
	   printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;
}
