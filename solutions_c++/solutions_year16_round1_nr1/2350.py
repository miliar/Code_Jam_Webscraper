#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <list>

using namespace std;

int main()
{
	int t, caseNum = 1, i;
	char c[1005];
	list <char> ans;
	list <char>::iterator it;
	scanf("%d", &t);
	while(t--){
		scanf("%s", c);
		ans.clear();
		ans.push_back(c[0]);
		for(i = 1;i < strlen(c);i++){
			if(ans.front() > c[i])
				ans.push_back(c[i]);
			else
				ans.push_front(c[i]);
		}
		printf("Case #%d: ", caseNum++);
		for(it = ans.begin();it != ans.end();it++)
			printf("%c", *it);
		printf("\n");
	}
	return 0;
}
