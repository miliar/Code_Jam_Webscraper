#include<bits/stdc++.h>
using namespace std;
void pancake(int x, FILE *fp)
{
	char p[1000];
	int k, n = 0;
	vector<bool> pan;
	scanf("%s %d", p, &k);
	fprintf(fp, "Case #%d: ", x);
	for(int i=0;i<sizeof(p);i++)
		if(p[i] == '+') pan.push_back(1);
		else if(p[i] == '-') pan.push_back(0);
		else break;
	for(int i=0;i<pan.size()-k+1;i++)
		if(!pan[i]) 
		{
			for(int j=0;j<k;j++) pan[i+j] = 1-pan[i+j];
			n++;
		}
	for(auto i:pan) 
		if(!i) 
		{
			fprintf(fp, "IMPOSSIBLE\n");
			return;
		}
	fprintf(fp, "%d\n", n);
}
int main(void)
{
	int a;
	scanf("%d", &a);
	FILE *fp = fopen("Output.txt", "w+");
	for(int x=0;x<a;x++)
		pancake(x+1, fp);
} 
