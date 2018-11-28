#include<stdio.h>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;

string print_case(int n, int rps){
	if(n==0){
		string ret = "";
		if(rps == 0) ret += "R";
		else if(rps == 1) ret += "P";
		else ret += "S";
		return ret;
	}
	string p, q;
	if(rps == 0){
		p = print_case(n-1, 0);
		q = print_case(n-1, 2);
	}
	else if(rps == 1){
		p = print_case(n-1, 1);
		q = print_case(n-1, 0);
	}
	else{
		p = print_case(n-1, 1);
		q = print_case(n-1, 2);
	}
	for(int i=0;i<p.length();i++){
		if(p[i] < q[i]) {
			return p+q;
		} else if(p[i] > q[i]){
			return q+p;
		}
	}
}
int main()
{
	int test, t;
	//scanf("%d",&test);
	freopen("A-large.in", "r", stdin);
	freopen("A-larout.out", "w", stdout);
	scanf("%d",&test);
	for(t=1;t<=test;t++){
		int n, r, p, s;
		bool flag = false;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		while(1){
			if(r+p+s == 1) break;
			if( r+p<s || r+s<p || s+p<r){
				flag = true;
				break;
			}
			if( (r+p-s)%2!=0 || (r+s-p)%2!=0 || (p+s-r)%2!=0){
				flag = true;
				break;
			}
			int next_r = (r+s-p)/2;
			int next_p = (r+p-s)/2;
			int next_s = (s+p-r)/2;
			r = next_r;
			p = next_p;
			s = next_s;
		}
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else{
			printf("Case #%d: ",t);
			if(r) cout << print_case(n, 0);
			else if(p) cout << print_case(n, 1);
			else cout << print_case(n, 2);
			printf("\n");
		}
	}
	return 0;
}
