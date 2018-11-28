#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
void prnt(vector<float> v) {
	int i;
	int N=v.size();
	for(i=0;i<N;i++)
		printf("%f ",v.at(i));
	printf("\n");
}	
int main() {
	int T,N,j,i,cnt,k,flag;
	float ele;
	vector<float>a;
	vector<float>b;
	scanf("%d",&T);
	for(k=0;k<T;k++) {
		scanf("%d",&N);
		a.clear();b.clear();
		for(i=0;i<N;i++) {
			scanf("%f",&ele);
			a.push_back(ele);
		}
		for(i=0;i<N;i++) {
			scanf("%f",&ele);
			b.push_back(ele);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		//prnt(a);
		//prnt(b);
		//calculation of DW
		i=N-1;j=N-1;cnt=0;flag=0;
		while(j!=-1) {
			while(a.at(i)>b.at(j)) {
				j--;i--;
				if(j==-1) {
					flag=1;
					break;
				}
			}
			if(flag==0) {
				j--;
			}
		}
		printf("Case #%d: %d",k+1,N-i-1);
		//calculation of W
		i=0;j=0;cnt=0;flag=0;
		while(j!=N) {
			while(a.at(i)>b.at(j)) {
				j++;
				if(j==N) {
					flag=1;
					break;
				}
			}
			if(flag==0) {
				i++;j++;
			}
		}
		printf(" %d\n",N-i);
	}
	return 0;
}
