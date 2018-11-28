#include<iostream>
#include<stdio.h>
using namespace std;
char s[4][4];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("o.txt","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	bool flag1,flag2;
	bool flag;
	while(t--){
		flag1=flag2=flag=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>s[i][j];
				if(s[i][j]=='.')
					flag=1;
			}
		}
		int num,num2;
		int n1,n2;
		for(int i=0;i<4;i++){
			num=num2=0;
			n1=n2=0;
			for(int j=0;j<4;j++){
				if(s[i][j]=='X'||s[i][j]=='T')
					num++;
				if(s[i][j]=='O'||s[i][j]=='T')
					num2++;
				if(s[j][i]=='X'||s[j][i]=='T')
					n1++;
				if(s[j][i]=='O'||s[j][i]=='T')
					n2++;
			}
			if(num==4 || n1==4){
				flag1=1;
				break;
			}
			if(num2==4||n2==4){
				flag2=1;
				break;
			}
		}
		num=num2=0;
		n1=n2=0;
		for(int i=0;i<4;i++){
			if(s[i][i]=='X'||s[i][i]=='T')
					num++;
			if(s[i][i]=='O'||s[i][i]=='T')
					num2++;
			if(s[i][3-i]=='X'||s[i][3-i]=='T')
					n1++;
			if(s[i][3-i]=='O'||s[i][3-i]=='T')
					n2++;
		}
		if(num==4||n1==4){
			flag1=1;
		}
		if(num2==4||n2==4){
			flag2=1;
		}
		if(flag1)
			printf("Case #%d: X won\n",++cas);
		else if(flag2)
			printf("Case #%d: O won\n",++cas);
		else if(flag)
			printf("Case #%d: Game has not completed\n",++cas);
		else
			printf("Case #%d: Draw\n",++cas);
	}
	return 0;
}
	
			

