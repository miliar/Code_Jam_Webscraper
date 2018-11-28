#include<bits/stdc++.h>

using namespace std;

int cnt[10];

bool check() {
	for(int i=0; i<10; ++i)
	  if (cnt[i] == 0)
		return false;
	return true;
}

void process(long long num) {
  while (num > 0) {
	cnt[num%10]++;
	num/=10;
  } 
}

int main() {
  int N, T;
  int caso = 0;
  scanf("%d",&T);
  while (T--) {
	scanf("%d",&N);
	for(int i=0; i<10; ++i)
	  cnt[i] = 0;
	printf("Case #%d: ", ++caso);
	if (N == 0) {
	  puts("INSOMNIA");
	} else {
	  for(int i=1; i<=100; ++i) {
		process(1LL*i*N);
		if(check() == true) {
		  printf("%lld\n", 1LL*i*N);
		  break;
		}
	  }
	}
  }
}