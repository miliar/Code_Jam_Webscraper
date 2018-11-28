#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
typedef long long INT;


int main(){
	int len,i,j,tst,cas=1,n;
	int cnt[15];
	int word[3000];
	char str[2050];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tst);
	while(tst--){
		scanf("%s",&str);
		len=strlen(str);
		clr(word);
		clr(cnt);
		for(i=0;i<len;i++){
			word[str[i]]++;
		}

		//0
		if(word['Z']!=0){
			cnt[0]=word['Z'];
			word['E']-=word['Z'];
			word['R']-=word['Z'];
			word['O']-=word['Z'];
			word['Z']=0;
		}
		//2
		if(word['W']!=0){
			cnt[2]=word['W'];
			word['T']-=word['W'];
			word['O']-=word['W'];
			word['W']=0;
		}

		//4
		if(word['U']!=0){
			cnt[4]=word['U'];
			word['F']-=word['U'];
			word['O']-=word['U'];
			word['R']-=word['U'];
			word['U']=0;
		}
		//3
		if(word['R']!=0){
			cnt[3]=word['R'];
			word['T']-=word['R'];
			word['H']-=word['R'];
			word['E']-=2*word['R'];
			word['R']=0;
		}
		//6
		if(word['X']!=0){
			cnt[6]=word['X'];
			word['S']-=word['X'];
			word['I']-=word['X'];
			
			word['X']=0;
		}
		//7
		if(word['S']!=0){
			cnt[7]=word['S'];
			word['V']-=word['S'];
			word['E']-=2*word['S'];
			word['N']-=word['S'];
			word['S']=0;
		}
		//8
		if(word['G']!=0){
			cnt[8]=word['G'];
			word['E']-=word['G'];
			word['I']-=word['G'];
			word['H']-=word['G'];
			word['T']-=word['G'];
			word['G']=0;
		}
		//1
		if(word['O']!=0){
			cnt[1]=word['O'];
			word['N']-=word['O'];
			word['E']-=word['O'];
			word['O']=0;
		}
		//3
		if(word['R']!=0){
			cnt[3]=word['R'];
			word['T']-=word['R'];
			word['E']-=2*word['R'];
			word['H']-=word['R'];
			word['R']=0;
		}
		//5
		if(word['V']!=0){
			cnt[5]=word['V'];
			word['F']-=word['V'];
			word['I']-=word['V'];
			word['E']-=word['V'];
			word['V']=0;
		}
		//9
		if(word['I']!=0){
			cnt[9]=word['I'];
			
		}
		printf("Case #%d: ",cas++);
		for(i=0;i<10;i++){
			for(j=0;j<cnt[i];j++){
				printf("%d",i);
			}
		}
		printf("\n");
	}
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);