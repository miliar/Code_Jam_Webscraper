#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
	int t,x,y,p;
	
	int a[4][4],b[4][4];
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int count=0;
		scanf("%d",&x);
		for(int m=0;m<4;m++){
		for(int j=0;j<4;j++){
			cin >> a[m][j] ;
		}
	}
		scanf("%d",&y);
		for(int m=0;m<4;m++){
		for(int j=0;j<4;j++){
			cin >> b[m][j] ;
		}
	}

	for(int j=0;j<4;j++){
		for(int k=0;k<4;k++){
			if(a[x-1][j]==b[y-1][k]){
				count++;
				p=a[x-1][j];
		}
	}
}
	if (count==0) printf("Case #%d: Volunteer cheated! \n",i+1);
	else if(count==1)printf("Case #%d: %d \n",i+1,p);
	else printf("Case #%d: Bad Magician! \n",i+1);

}
	return 0;
}