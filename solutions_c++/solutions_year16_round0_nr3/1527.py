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

int ans[9] = {3,2,5,2,7,2,9,2,11};
char result[34];

bool check(int val) 
{
	int div,i,odd,even,j;
	
	odd = even = 0;
	memset(result,'0',sizeof(result));

	result[31] = '1';
	result[0] = '1';
	div  = 1;
	for(i = 0;i < 14;i++) {
		if(div&val) {
			if(i&1)
				odd++;
			else
				even++;
			result[i+1] = '1';
		}
		else
			result[i+1] = '0';
		div = div*2;
	}
	result[32] = '\0';

	i = 0,j = 31;	
	while(i < j) {
		swap(result[i],result[j]);
		i++;
		j--;		
	}	
	
	if(odd == even)
		return true;
	else
		return false;	

}

void compute(int n,int j) 
{
	int i,val,z,cnt;

	val = 32768/2;
	cnt = 0;
	for(i  = 0;i < val;i++) {
		if(check(i)) {
			printf("%s ",result);
			for(z = 0;z < 9;z++)
				printf("%d ",ans[z]);
			cnt++;
			printf("\n");
		}
		if(cnt == j)
			break;	
	}	

}

int main() 
{
	int t,i,n,j;

	freopen("input6.txt", "r", stdin);
	freopen("output6.txt", "w", stdout);
	scanf("%d",&t);

	for(i = 0;i < t;i++) {
		scanf("%d %d",&n,&j);
		printf("Case #%d:\n",i+1);
		compute(n,j);	
	}
	
	return 0;
}
