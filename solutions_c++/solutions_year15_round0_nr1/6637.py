#include<iostream>


using namespace std;


int main(){
	int t,n,i,a,x;
	int sum,in;
	FILE *inp,*out;
	inp = fopen("a.txt","r");
	out = fopen("b.txt","w");
	fscanf(inp,"%d",&t);
	x=t;
	while(t--){
		fscanf(inp,"%d",&n);
		sum=0;
		in=0;
		for(i=0;i<=n;i++){
			
			fscanf(inp,"%1d",&a);
			if(sum<i && a!=0){
				in = in + i-sum;
				sum+=in;
			}
			sum+=a;
		}
		fprintf(out,"Case #%d: %d\n",x-t,in);
	}
}
