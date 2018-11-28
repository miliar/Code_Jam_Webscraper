#include <cstdio>
#include <set>

using namespace std;

int main()
{
	int t_case;
	FILE *input = freopen("input.txt","r",stdin);
	FILE *output = freopen("output.txt","w+",stdout);
	scanf("%d",&t_case);

	for(int j=1;j<=t_case;j++){
		set<int> num_set;
		int n;
		int cnt = 0;
		int i = 1;

		scanf("%d",&n);

		if(n==0){
			printf("Case #%d: INSOMNIA\n",j);
			continue;
		}
		while(true){
			int ni = n * i++;

			while(ni >= 10){
				num_set.insert(ni%10);
				ni /= 10;
			}
			num_set.insert(ni%10);
			if(num_set.size() == 10){
				i--;
				break;
			}
			
		}
		printf("Case #%d: %d\n",j,n*i);
	}


	return 0;
}