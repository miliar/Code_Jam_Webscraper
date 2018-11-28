#include <bits/stdc++.h>
using namespace std;
int t=1, u, k, cnt, i, j;
bool flag;
string S;
int main(){
	for(scanf("%d", &u); t<=u; t++){
		cin>>S>>k;
		flag=true;
		for(i=cnt=0; i<=(int)S.size()-k; i++){
			if(S[i]=='-'){
				for(j=i; j<i+k; j++)
					S[j]=(S[j]=='-')?'+':'-';
				cnt++;
			}
		}
		for(i=1; i<k; i++)
			if(S[(int)S.size()-i]=='-')
				flag=false;
		if(!flag)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
