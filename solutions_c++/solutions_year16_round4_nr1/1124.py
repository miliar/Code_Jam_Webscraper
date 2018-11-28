#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;
int ans[3][20][3];
char dir[10][3]={"P","R","S"};
string gao(int type,int level){
	if (level==1){
		string res=dir[type];
		return res;
	}
	string a=gao(type,level-1);
	string b=gao((type+1)%3,level-1);
	if (a<b) return a+b;
	else return b+a;
}
int main(int argc, char const *argv[])
{
	memset(ans,0,sizeof(ans));
	ans[0][0][0]=1;
    ans[1][0][1]=1;
    ans[2][0][2]=1;
    for (int i=1;i<=12;i++){
    	ans[0][i][0]=ans[0][i-1][0]+ans[0][i-1][2];
    	ans[0][i][1]=ans[0][i-1][1]+ans[0][i-1][0];
    	ans[0][i][2]=ans[0][i-1][2]+ans[0][i-1][1];
        ans[1][i][0]=ans[1][i-1][0]+ans[1][i-1][2];
    	ans[1][i][1]=ans[1][i-1][1]+ans[1][i-1][0];
    	ans[1][i][2]=ans[1][i-1][2]+ans[1][i-1][1];
    	ans[2][i][0]=ans[2][i-1][0]+ans[2][i-1][2];
    	ans[2][i][1]=ans[2][i-1][1]+ans[2][i-1][0];
    	ans[2][i][2]=ans[2][i-1][2]+ans[2][i-1][1];
    }
    int n,t,a,b,c;
    scanf("%d",&t);
    for (int i=0;i<t;i++){
    	scanf("%d%d%d%d",&n,&b,&a,&c);
    	int sum=a+b+c,cnt=0;
    	while(sum){
    		cnt++;
    		sum/=2;
    	}

    	int flag=-1;
    	for (int j=0;j<3;j++){
    		if (a==ans[j][cnt-1][0] && b==ans[j][cnt-1][1] && c==ans[j][cnt-1][2])
    			flag=j;
    	}
    	printf("Case #%d: ", i+1);
        if (flag==-1)
        	printf("IMPOSSIBLE\n");
        else{
        	string str=gao(flag,cnt);
        	cout<<str<<endl;
        }
    }
	return 0;
}