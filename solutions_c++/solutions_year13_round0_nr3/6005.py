#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int num;
	int rnum;
	int rem, onum;
	int sr = 0;
	int p1, s1, p2; 
	int tt;
	int count = 1;
	int m,n;
	int ans;
	cin >> tt;
    while(tt){
	cin >> m >> n;
	ans = 0;
	while(m <= n){
		p1 = 0, s1 = 0, p2 = 0;
		
		num = m;
		onum = m;
		rnum = 0;
		while(num > 0){
			rem = num%10;
			rnum = (rnum * 10) + rem;
			num = num/10;
	
		}
		if( rnum == onum){
			p1 = 1;
		}
		sr = sqrt(onum);
		if(onum == (sr*sr)){
			s1 = 1;
		}
		int srp = sr;
		rnum = 0;
		while(srp > 0){
			rem = srp%10;
			rnum = (rnum * 10) + rem;
			srp = srp/10;
	
		}
		if(sr == rnum)
			p2 = 1;

		if(p1 == 1 && s1 == 1 && p2 == 1){
			ans++;
		}
		m++;
	}
	cout <<"Case #"<<count<<": "<< ans <<endl;
	count++;
	tt--;
    }
	return 0;
}
