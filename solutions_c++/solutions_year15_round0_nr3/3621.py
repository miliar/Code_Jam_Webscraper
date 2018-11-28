#include<iostream>

using namespace std;
char s[100000];
int v[100000];

int a[4][4] = {
				{1, 2, 3, 4},
				{2,-1, 4,-3},
				{3,-4,-1, 2},
				{4, 3,-2,-1}
				};
				
	

int mul(int x,int b){
	return a[x-1][b-1];
}


int mod(int a){
	if(a<0)
		return -a;
	return a;
}			
	
int getmap(int a){
	if(mod(a)<'i'){
		return a;
	}
	else{
		return (mod(a)-'g')*(a/mod(a));
	}
	
	
	
	
}			
				
int main(){
	int t,x,l,n,j;
	int i,m,c,r;
	FILE *inp,*out;
	inp = fopen("C-small-attempt0.in","r");
	out = fopen("C-small-attempt0.out","w");
	
	fscanf(inp,"%d",&t);
	x=t;
	while(t--){
		m=1;
		fscanf(inp,"%d %d",&n,&l);
		fscanf(inp," %s",s);
		
		
		for(j=0;j<l;j++){
			for(i=0;i<(n);i++){
				v[(i) + (j*n)] = getmap(s[i]);
			}
		}
		i=0;
		c=2;
		r=v[0];
		while(1){
			if((r)==c){
				c++;
				r=1;
			}
			if(i >= (n*l)-1){
				break;
			}
			
			m = r/mod(r);
			r = mod(r);
			
			r = mul(r,v[i+1]);
			r = m*r;
			i++;
			
			
		}
		
		if(c >4 && r == 1){
			fprintf(out,"Case #%d: YES\n",x-t);//YES
		}
		else{
			fprintf(out,"Case #%d: NO\n",x-t);//NO
		}
		
		
	}
}
