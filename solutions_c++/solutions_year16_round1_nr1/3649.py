#include<cstdio>
#include<queue>
using namespace std;
const int MAX=1<<10;
char s[MAX];

int main()
{	
	int T;
	scanf(" %d",&T);
	int tc=1;
	for(tc=1;tc<=T;tc++){
		printf("Case #%d: ",tc);
		scanf(" %s",s);
		deque<char> Q;
		Q.push_back(s[0]);
		int i;
		for(i=1;s[i];i++){
			char &ch=s[i];
			if(Q.front()<=ch) Q.push_front(ch);
			else Q.push_back(ch);
		}

		while(Q.size()) { 
			printf("%c",Q.front());
			Q.pop_front();
		}
		printf("\n");
	}
	return 0;
}
