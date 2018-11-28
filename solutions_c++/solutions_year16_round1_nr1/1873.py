#include<iostream>
#include<cstring>
#include<cstdio>
#include<queue>
using namespace std;
deque <char> q;
char str[1010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%s",str);
		int len=strlen(str);
		for(int i=0;i<len;i++){
			if(q.empty()) q.push_back(str[i]);
			else{
				if(str[i]>=q.front()){
					q.push_front(str[i]);
				}else{
					q.push_back(str[i]);
				}
			}
		}
		printf("Case #%d: ",cas);
		while(!q.empty()){
			printf("%c",q.front());
			q.pop_front();
		}
		puts("");
		
	}
	return 0;
}
