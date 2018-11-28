#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>

#define f first
#define s second
#define pb push_back

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;

void compute(char str[])
{
	char prev;
	int len = strlen(str);
	int cnt = 0;

	prev = str[0];
	for(int i = 1;i < len;i++) {
		if(str[i] != prev)
			cnt++;
		prev  = str[i];
	} 
	if(prev == '-')
		cnt++;	

	printf("%d\n",cnt);

} 


int main() 
{
	int t,i;
	char str[110];

	freopen("input4.txt", "r", stdin);
	freopen("output4.txt", "w", stdout);
	scanf("%d",&t);
	cin.ignore();
	for(i = 0;i < t;i++) {
		scanf("%s",str);
		printf("Case #%d: ",i+1);		
		compute(str);					
	}
		
	return 0;

}

