#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
char a[5][5];
bool calc(char x){
	int i,j;
	for (i=0;i<4;i++){
		int t=0,k=0,l=0,m=0;
	 for (j=0;j<4;j++){
		if (a[i][j]==x) t++;
		if (a[j][i]==x) k++;
		if (a[j][j]==x) l++;
		if (a[j][3-j]==x) m++; 
		}
	 if (t==4 || k==4) return true;
	 if (l==4|| m==4) return true;
	}

	for(i=0;i<4;i++){
		int t[2]={0},k[2]={0},l[2]={0},m[2]={0};
 	 for(j=0;j<4;j++){
		if (a[i][j]==x) t[1]++;else if(a[i][j]=='T') t[0]++;
		if (a[j][i]==x) k[1]++;else if (a[j][i]=='T') k[0]++;
		if (a[j][j]==x) l[1]++;else if (a[j][j]=='T') l[0]++;
		if (a[j][3-j]==x)m[1]++;else if (a[j][3-j]=='T')m[0]++;	
 	 }
	  if ((t[1]==3 && t[0]==1) || (k[1]==3 && k[0]==1 ))return true;	
	  if ((l[1]==3 && l[0]==1) || (m[1]==3 && m[0]==1 ))return true;
	}
	
	


}
bool cantain(char x){
	for (int i=0;i<4;i++) 
    for(int j=0;j<4;j++)
		if (a[i][j]==x) return true;
}
char check(){
	
	if (calc('X')) return 'X';
    if (calc('O')) return 'O';
	if (cantain('.')==false) return  'D';
	return 'W';
}
int main(){
	int t,i,j,k,n;
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	getchar();
	int test=0;
	while(test<t){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				scanf("%c",&a[i][j]);
	 	getchar();
		}
		char c=check();
		test++;
		if (c=='X') printf("Case #%d: X won\n",test);
		else if (c=='O') printf("Case #%d: O won\n",test);
		else if (c=='D') printf("Case #%d: Draw\n",test);
		else printf("Case #%d: Game has not completed\n",test);
		getchar();

	}



	return 0;
}
