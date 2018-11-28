#include <iostream>
#include <cmath>
using namespace std;

int n,Case,cnt,a,b,up,down;

int palindrome(int x){
	int d[11],prt = 0;
	while(x > 0){
		d[prt++] = x % 10;
		x /= 10;
	}
	for(int i = 0; i < prt - i - 1; i ++){
		if(d[i] != d[prt-i-1])return 0;
	}
	return 1;	
}


int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> n;
	for(int Case = 1 ;Case <= n ; Case ++){
		printf("Case #%d: ",Case);
		scanf("%d %d",&a,&b);
		up = int(sqrt(double(b)));
		down = int(sqrt(double(a)));
		int cnt= 0;
		if(down * down < a)down ++;
		for(int i = down;i <= up ; i ++){
			if(palindrome(i) && palindrome(i*i))cnt ++;
		}
		printf("%d\n",cnt);		
	}
	return 0;
}
