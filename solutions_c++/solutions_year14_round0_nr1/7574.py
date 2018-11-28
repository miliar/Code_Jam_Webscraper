#include <cstdio>
#include <algorithm>
using namespace std;

int T, first_row, second_row, t=1;
int arr[5][5]={0,};
int arr1[5][5]={0,};

void input()
{
	scanf("%d", &first_row);
	for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
			scanf("%d", &arr[i][j]);

	scanf("%d", &second_row);
	for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
			scanf("%d", &arr1[i][j]);

}

void make()
{
	int mem[5]={0,};
	for (int i=1; i<=4; i++) {
		mem[i]=arr[first_row][i];
		//printf("mem[%d] = %d\n", i, mem[i]);
	}

	int cnt=0;
	int ans=0;
	for (int i=1; i<=4; i++) {
		for (int j=1; j<=4; j++) {
			//printf("arr1[second_row][%d] = %d\n", i, arr1[second_row][i]);
			if(mem[i]==arr1[second_row][j]) {
				cnt++;
				ans=mem[i];
				//printf("ans=%d", ans);
			}
		}
	}
	if (cnt==1)
		printf("Case #%d: %d\n", t, ans);
	else if (cnt==0)
		printf("Case #%d: Volunteer cheated!\n", t);
	else 
		printf("Case #%d: Bad magician!\n", t);

	return;
}
int main()
{
	freopen("A-small-attempt3.in", "r", stdin);
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		input();
		make();
	}
	return 0;
}