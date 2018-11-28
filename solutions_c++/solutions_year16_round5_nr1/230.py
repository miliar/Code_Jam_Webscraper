#include <stdio.h>
#include <stack>
using namespace std;

void proc()
{
	stack<char> S;
	char str[20002];
	scanf ("%s",str);
	int ans = 0;
	for (int i=0;str[i];i++){
		if (!S.empty() && S.top() == str[i]){
			S.pop(); ans += 10;
		}
		else S.push(str[i]);
	}
	ans += S.size() / 2 * 5;
	printf ("%d\n",ans);
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}