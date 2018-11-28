#include <iostream>
#include <cstdio>
using namespace std;

char mp[6][6];

bool test(char a,char b){
	if (a=='.') return false;
	if (b=='.') return false;
	if (a=='T') return true;
	if (a==b) return true;
	return false;
}
int main(){
	long cases;
	char flag;
	cin>>cases;
	for (int tt=1;tt<=cases;tt++){
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				cin>>mp[i][j];
		flag='N';
		for (int i=1;i<=4;i++){
			flag=mp[i][1];
			if (flag=='T') flag=mp[i][2];
			if (flag=='.'){
				flag='N';
				continue;
			}
			for (int j=2;j<=4;j++){
				if (!test(mp[i][j],flag)){
					flag='N';
					break;
				}
			}
			if (flag!='N') break;
		}
		if (flag=='N')
			for (int j=1;j<=4;j++){
				flag=mp[1][j];
				if (flag=='T') flag=mp[2][j];
				if (flag=='.'){
					flag='N';
					continue;
				}
				for (int i=2;i<=4;i++){
					if (!test(mp[i][j],flag)){
						flag='N';
						break;
					}
				}
				if (flag!='N') break;
			}
		if (flag=='N'){
			flag=mp[1][1];
			if (flag=='T') flag=mp[2][2];
			if (flag!='.'){
				for (int i=2;i<=4;i++){
					if (!test(mp[i][i],flag)){
						flag='N';
						break;
					}
				}
			}else{
				flag='N';
			}
			if (flag=='N'){
				flag=mp[1][4];
				if (flag=='T') flag=mp[1][4];
				if (flag!='.'){
					for (int i=2;i<=4;i++){
						if (!test(mp[i][5-i],flag)){
							flag='N';
							break;
						}
					}
				}else{
					flag = 'N';
				}
			}
		}
		if (flag!='N') printf("Case #%d: %c won\n",tt,flag);
		else{
			for (int i=1;i<=4;i++)
				for (int j=1;j<=4;j++)
					if (mp[i][j]=='.'){
						flag='.';
						break;
					}
			if (flag=='.') printf("Case #%d: Game has not completed\n",tt);
			else printf("Case #%d: Draw\n",tt);
		}
	}
}
