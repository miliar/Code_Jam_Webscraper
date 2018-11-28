#include<iostream>


using namespace std;
char str[100000];

int a[4][4] = {
				{1, 2, 3, 4},
				{2,-1, 4,-3},
				{3,-4,-1, 2},
				{4, 3,-2,-1}
				};
int product(int x,int y){
	return a[x-1][y-1];
}
int absolute(int a){
	if(a<0)
		return -a;
	return a;
}
			
int main(){
	
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,x,l,n,j,cases;
	int i,m,c,r,cur;
	scanf("%d",&t);
	
	cases = 1;
	while(cases <=t){
		m=1;
		scanf("%d%d",&n,&l);
		scanf(" %s",str);
		c=2;
		r=1;
		
		
		
		for(j=0;j<l;j++)
		{
			for(i=0;i<n;i++){
				if((r)==c){
					c++;
					r=1;
				}
				cur = str[i] - 'i' + 2;
				
				m = r/absolute(r);
				r = m*product(absolute(r),cur);
				
			}
				
		} 
		  
		if((r)==c){
			c++;
			r=1;
		}
		if(c >4 && r == 1){
			printf("Case #%d: YES\n",cases);//YES
		}
		else{
			printf("Case #%d: NO\n",cases);//NO
		}
		
		cases++;
	}
}
