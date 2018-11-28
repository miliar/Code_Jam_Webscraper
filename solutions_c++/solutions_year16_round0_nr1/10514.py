#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main(int argc,char **argv){
	if(argc<3){
		cout << "lack para" << endl;
		return 1; 
	}
    freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int cnt;
	cin >> cnt;
	for(int i=1;i<=cnt;i++){
		int now_num,flag[20]={0},ncnt=0;
		scanf("%d",&now_num);//cout << now_num << endl;
		long long lnow_num=(long long)now_num,res_num=-1;
		for(int j=1;j<=100;j++){
			long long tnum=lnow_num*j;
			long long fnum=lnow_num*j;
			while(fnum!=0){
				int x=fnum%10;	
				fnum=fnum/10;	
				if(flag[x]==0){
					flag[x]=1;
					ncnt+=1;
				}
			}
			if(ncnt==10){
				res_num=tnum;
				break;
			}
		}
		if(res_num==-1){
			printf("Case #%d: INSOMNIA\n", i);
		}
		else{
			printf("Case #%d: %lld\n", i,res_num);
		}
	}
} 
