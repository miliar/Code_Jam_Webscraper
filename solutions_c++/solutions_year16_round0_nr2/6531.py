#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("blarge.out","w",stdout);
	int t; scanf("%d", &t);
	for(int tc=1;tc<=t;tc++)
	{
		char in[105]; scanf("%s", in);
		int len=0, id=strlen(in)-1;
		while(id>=0 && in[id]=='+') id--;
		printf("Case #%d: ", tc);
		if(id==-1) { printf("0\n"); continue; }
		len++;
		for(int i=id-1;i>=0;i--)
		{
			if(in[i]==in[i+1]) continue;
			len++;
		}
		printf("%d\n", len);
	}
	return 0;
}
