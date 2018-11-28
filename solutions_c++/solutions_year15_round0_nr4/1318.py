#include<cstdio>

using namespace std;


int main(void)
{
	int cases;
	int cas;
	int x,r,c;
	int ans;

	scanf("%d",&cases);
	for(cas=1;cas<=cases;cas++){
		ans=0;
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",cas);

		if(x==1){
			ans=1;
		}
		else if(x==2){
			if(r%2==0 || c%2==0)
				ans=1;
			else 
				ans=2;
		}
		else if(x==3){
			if(r%3==0 && c>=2)
				ans=1;
			else if(r>=2 && c%3==0)
				ans=1;
			else
				ans=2;
		}
		else{//x==4
			if(r<4 && c<4)
				ans=2;
			else if(r==4 && c>2)
				ans=1;
			else if(r>2 && c==4)
				ans=1;
			else 
				ans=2;
		}

		if(ans==1)
			printf("GABRIEL\n");
		else 
			printf("RICHARD\n");
	}
}
