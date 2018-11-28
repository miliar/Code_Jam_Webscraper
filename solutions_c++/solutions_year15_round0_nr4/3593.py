#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main()
{
	int T,X,R,C;
	bool flag=false;
	bool output[100]={0};
	scanf("%d",&T);
	for(int i=0; i<T; ++i){
		flag=false;
		scanf("%d %d %d",&X, &R, &C);
		if(R<C)
			swap(R,C);
		if(X==1)
			flag=true;
		else if(X==2){
			if(R*C%2)
				flag=false;
			else
				flag=true;
		}
		else if(X==3){
			if((R%3==0 && C>=2) || (R==4 && C==3))
				flag = true;
			else
				flag = false;
		}
		else{
			if(R%4==0 && C>=3)
				flag=true;
			else
				flag = false;
		}
		output[i] = flag;
	}
	for(int i=0; i<T; ++i){
		printf("Case #%d: ",i+1);
		if(output[i])
			printf("GABRIEL\n");
		else
			printf("RICHARD\n");
	}
	return 0;
}
