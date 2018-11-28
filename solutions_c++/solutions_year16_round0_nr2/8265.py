#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>

using namespace std;

int got[20],N;
char s[100000];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&N);
	int cas=0;
	while	(N--){
		cas++;
		printf("Case #%d: ",cas);
		scanf(" ");
		gets(s);
		char last=s[0];
		vector<int> p;
		p.clear();
		p.push_back(0);
		int len=0;
		for	(int i=0;i<strlen(s);++i)
			if	(s[i]==last){
				p[len]++;
			}
			else{
				len++;
				p.push_back(1);
				last=s[i];
			}
		if	 (len==0){
			if	(s[0]=='-')	len=1;
		}
		else{
			len=len*2;
			if (s[0]=='-')	len--;
		}
		printf("%d\n",len);
	} 
}
