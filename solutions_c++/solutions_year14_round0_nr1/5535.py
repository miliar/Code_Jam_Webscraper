#include <iostream>
#include <cstdio>
using namespace std;
int ar[5][5],bar[5][5],n;
int main()
{
	scanf(" %d",&n);
	for(int i=1,a,b,cnt=0,tut;i<=n;i++,cnt=0){
		scanf(" %d",&a);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) scanf(" %d",&ar[i][j]);
		scanf(" %d",&b);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++) scanf(" %d",&bar[i][j]);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				if(ar[a][i]==bar[b][j]) {cnt++;tut=ar[a][i];}
		printf("Case #%d: ",i);
		if(!cnt) printf("Volunteer cheated!\n");
		else if(cnt==1) printf("%d\n",tut);
		else printf("Bad magician!\n");
	}
	return 0;
}
