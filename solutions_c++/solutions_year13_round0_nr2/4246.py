#include<cstdio>
#include<memory.h>
#include<algorithm>
#define MAX 100
using namespace std;

int map[MAX+1][MAX+1];
int n_max[MAX+1];
int m_max[MAX+1];

void process(){
	int n, m;
	memset(map,0,sizeof(map));
	memset(n_max,0,sizeof(n_max));
	memset(m_max,0,sizeof(m_max));

	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			scanf("%d",&map[i][j]);
			n_max[i] = max(n_max[i], map[i][j]);
			m_max[j] = max(m_max[j],map[i][j]);
		}
	bool sw = true;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(map[i][j] < n_max[i] && map[i][j] < m_max[j])	sw = false;
	if(sw)
		printf("YES\n");
	else
		printf("NO\n");

}
int main(){
	int c;
	scanf("%d",&c);
	for(int i=1;i<=c;i++){
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}