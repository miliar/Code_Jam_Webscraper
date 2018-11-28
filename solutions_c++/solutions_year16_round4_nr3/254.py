#include<stdio.h>

int r,c;
int arr[100]={0};
bool check[16]={0};
bool visit[18]={0};

int f2(int idx, int dir, int out){
	int x = idx / c;
	int y = idx % c;
	if(y==0 && dir==3 && out==1){
		return 2*c + r + r-x;
	}
	else if(y==c-1 && dir==1 && out==1){
		return c+x+1;
	}
	else if(x==0 && dir==0 && out==1){
		return y+1;
	}
	else if(x==r-1 && dir==2 && out==1){
		return r+c+c-y;
	}
	if(out == 1){
		if(dir == 0) return f2( (x-1)*c+y, dir, 0);
		else if(dir == 1) return f2( x*c+y+1, dir, 0);
		else if(dir == 2) return f2( (x+1)*c+y, dir, 0);
		else return f2( x*c+y-1, dir, 0);
	}
	if(check[idx]){
		if(dir == 0) return f2( idx, 1, 1);
		else if(dir == 1) return f2(idx, 0, 1);
		else if(dir == 2) return f2(idx, 3, 1);
		else return f2(idx, 2, 1);
	}
	else{
		if(dir == 0) return f2(idx, 3, 1);
		else if(dir == 1) return f2(idx, 2, 1);
		else if(dir == 2) return f2(idx, 1, 1);
		else return f2(idx, 0, 1);
	}
}
bool f(int idx){
	if(idx == r*c){
		int temp;
		for(int i=0;i<r+c;i++){
			if(arr[i*2]<=c){
				temp = f2(arr[i*2]-1, 2, 0);
				if(temp != arr[i*2+1]) return false;
			}
			else if(arr[i*2]<=c+r){
				temp = f2(c-1 + c*(arr[i*2]-c-1), 3, 0);
				if(temp != arr[i*2+1]) return false;
			}
			else if(arr[i*2]<=2*c+r){
				temp = f2( (r-1)*c+ c-(arr[i*2]-r-c), 0, 0);
				if(temp != arr[i*2+1]) return false;
			}
			else{
				temp = f2( c*( r-(arr[i*2]-2*c-r)), 1, 0);
				if(temp != arr[i*2+1]) return false;
			}
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(check[i*c+j]) printf("/");
				else printf("\\");
			}
			printf("\n");
		}
		return true;
	}
	check[idx] = true;
	if(f(idx+1)){
		check[idx] = false;
		return true;
	}
	check[idx] = false;
	if(f(idx+1)){
		return true;
	}
	return false;
}
int main()
{
	int t,test;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Cout.out","w",stdout);
	scanf("%d",&test);
	for(t=1;t<=test;t++){
		scanf("%d%d",&r,&c);
		for(int i=0;i<2*(r+c);i++){
			scanf("%d",&arr[i]);
		}
		printf("Case #%d:\n", t);
		if(!f(0)) printf("IMPOSSIBLE\n");
	}
	return 0;
}
