#include<stdio.h>
#include<stack>

using namespace std;

int main(){
	int casos, resp1, resp2, arr1[5][5], arr2[5][5];
	scanf("%d",&casos);
	for(int c=1; c<=casos; c++){
		stack<int> Bateria;
		scanf("%d",&resp1);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&arr1[i][j]);
		scanf("%d",&resp2);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&arr2[i][j]);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++)
			if(arr1[resp1-1][i]==arr2[resp2-1][j])
				Bateria.push(arr1[resp1-1][i]);
		} 
		if(Bateria.size()==0)
			printf("Case #%d: Volunteer cheated!\n",c);
		else if(Bateria.size()>1)
			printf("Case #%d: Bad magician!\n",c);
		else if(Bateria.size()==1)
			printf("Case #%d: %d\n",c, Bateria.top());
	}
	return 0;
}
