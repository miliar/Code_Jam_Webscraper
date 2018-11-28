#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
bool sort_check(double i,double j){
	return (i<j);
}
int main(){
	int t,n,i,j,q=1;
	int c1,c2;
	double a;
	vector<double> vec1,vec2;
	freopen("D-large.in","r",stdin);
	freopen("jam3_out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		vec1.clear();
		vec2.clear();
		for(i=0;i<n;i++){
			scanf("%lf",&a);
			vec1.push_back(a);
		}
		for(i=0;i<n;i++){
			scanf("%lf",&a);
			vec2.push_back(a);
		}
		std::sort(vec1.begin(),vec1.end(),sort_check);
		std::sort(vec2.begin(),vec2.end(),sort_check);
		i=0;j=0;
		c1=0; c2=0;
		while(i<n && j<n){
			if(vec1[i]>vec2[j]){j++; continue;}
			c2++; i++; j++;
		}
		i=0;j=0;
		while(i<n && j<n){
			if(vec1[i]<vec2[j]){i++; continue;}
			c1++; i++; j++;
		}
		printf("Case #%d: %d %d\n",q++,c1,n-c2);
	}
	return 0;
}
