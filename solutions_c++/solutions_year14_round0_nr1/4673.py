#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
void solve_p(int t) {
	int mat1[4][4],mat2[4][4],n1,n2,i,j,s;
	vector<int> temp1;
	vector<int> temp2;
	vector<int> v(10);
	vector<int>::iterator it;
	scanf("%d",&n1);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			scanf("%d",&mat1[i][j]);
	for(i=0;i<4;i++)
		temp1.push_back(mat1[n1-1][i]);
	scanf("%d",&n2);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			scanf("%d",&mat2[i][j]);
	for(i=0;i<4;i++)
		temp2.push_back(mat2[n2-1][i]);
	//solving the magic
	sort(temp1.begin(),temp1.end());
	sort(temp2.begin(),temp2.end());
	it=set_intersection(temp1.begin(),temp1.end(),temp2.begin(),temp2.end(),v.begin());
	v.resize(it-v.begin());
	//for(it=v.begin();it!=v.end();it++)
	//	printf("%d\n",*it);
	s=v.size();
	//printf("Size=%d\n",s);
	if(s==1)
		printf("Case #%d: %d\n",t,*v.begin());
	else if(s==0)
		printf("Case #%d: Volunteer cheated!\n",t);
	else
		printf("Case #%d: Bad magician!\n",t);
}
int main() {
	int T,n,i,mat[4][4],ans;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
		solve_p(i);
	return 0;
}
