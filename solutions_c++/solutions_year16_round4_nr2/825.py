#include<stdio.h>

double p[200]={0};
bool check[200]={0};
bool check2[200]={0};
int n,k;
int cnt = 0;
int cnt2 = 0;
double temp_ans = 0.0;
double ans = 0.0;

double c[20][20]={{0}};

void f2(int idx){
	if(idx == n){
		if(cnt2 != k/2) return;
		double temp = 1.0;
		for(int i=0;i<n;i++){
			if(!check[i]) continue;
			if(check2[i]) temp *= p[i];
			else temp *= (1.0-p[i]);
		}
		temp_ans += temp;
		return;
	}	
	if(!check[idx]){
		f2(idx+1);
		return;
	}
	if(n-idx==(k/2)-cnt){
		check2[idx] = true;
		cnt2++;
		f2(idx+1);
		cnt2--;
		check2[idx] = false;
	}
	else{
		if(cnt2 == k/2){
			f2(idx+1);
		}
		else{
			f2(idx+1);
			check2[idx] = true;
			cnt2++;
			f2(idx+1);
			cnt2--;
			check2[idx] = false;
		}
	}
}
void f(int idx){
	if(idx == n){
		temp_ans = 0.0;
		cnt2 = 0;
		f2(0);
		/*if(temp_ans/c[k][k/2] > ans){
			ans = temp_ans/c[k][k/2];
		}*/
		if(temp_ans > ans) ans = temp_ans;
		return;
	}
	if(n-idx==k-cnt){
		check[idx] = true;
		cnt++;
		f(idx+1);
		cnt--;
		check[idx] = false;
	}
	else{
		if(cnt == k){
			f(idx+1);
		}
		else{
			f(idx+1);
			check[idx] = true;
			cnt++;
			f(idx+1);
			check[idx] = false;
			cnt--;
		}
	}
}
int main()
{	
	int i,j;
	c[0][0] = c[1][0] = c[1][1] = 1.0;
	for(i=2;i<20;i++){
		c[i][0] = c[i][i] = 1.0;
		for(j=1;j<i;j++){
			c[i][j] = c[i-1][j] + c[i-1][j-1];
		}
	}
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-smout.out","w",stdout);
	int test, t;
	scanf("%d",&test);
	for(t=1;t<=test;t++){
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++) scanf("%lf",&p[i]);
		ans = 0.0;
		f(0);
		printf("Case #%d: %lf\n", t, ans);
	}
	return 0;
}
