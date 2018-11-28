#include <bits/stdc++.h>
using namespace std;
#define infinity (1000000007)
#define ll long long
#define s(n) scanf("%d",&n)
#define p(n) printf("%d\n",n)
#define rep(i,n) for(int i=0;i<n;++i)
char arr[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
int sn[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

int get_index(char a){
	int ans;
	switch(a){
		case '1': ans=0; break;
		case 'i': ans=1; break;
		case 'j': ans=2; break;
		case 'k': ans=3; break;
	}
	return ans;
}

int main() {
	//ios_base::sync_with_stdio(0);
	//freopen("inp31.in","r",stdin);
	int t,l,x;
	int sign,ans,cnt;
	int r,c;
	char temp;
	string s;
	s(t);
	for(int v=1;v<=t;v++){
		s(l);
		s(x);
		cin >> s;
		sign = 1;
		ans = 0;
		cnt = 0;
		temp = '1';
		for(int i=1;i<=x;i++){
			for(int j=0;j<l;j++){
				r = get_index(temp);
				c = get_index(s[j]);
				
//				cout << "\tr= " << r << endl;
//				cout << "\tc= " << c << endl;
				
				temp = arr[r][c];
//				cout << "\ttemp= " << temp << endl;
				if(sn[r][c]==-1){
					sign *= -1;
				}
//				cout << "\tsign= " << sign << endl;
				
				if(cnt==0 && temp=='i'){
					cnt++;
					temp = '1';
				}
				else if(cnt==1 && temp=='j'){
					cnt++;
					temp = '1';
				}
				else if(cnt==2 && temp=='k' && i==x && j==l-1){
					cnt++;
					temp = '1';
				}
//				cout << "\tcnt= " << cnt << endl;
			}
		}
//		cout << "\toutside loop" << endl;
//		cout << "\tsign= " << sign << endl;
//		cout << "\tcnt= " << cnt << endl;
		if(sign==1 && cnt==3){
			ans = 1;
		}
		if(ans==1){
			printf("Case #%d: YES\n",v);
		}
		else{
			printf("Case #%d: NO\n",v);
		}
	}
	return 0;
}
