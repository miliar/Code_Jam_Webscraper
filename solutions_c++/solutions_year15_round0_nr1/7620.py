//HARE KRISHNA

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define ll long long
#define I64 ll
#define pb push_back
const ll mod=1000000007;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out12.txt","w",stdout);
	int tcase,t;
	int s,already_stood,taken,i,j;
	scanf("%d",&t);
	char str[1005];
	//int minn=2000;
	for(tcase=1;tcase<=t;tcase++){
        scanf("%d %s",&s,str);
        for(j=0;j<=s;j++){
        bool flag=0;
		already_stood=j+str[0]-'0';

		for(i=1;i<=s;i++){
			if(str[i]>'0'){
				if(already_stood>=i){
					already_stood+=(str[i]-'0');
				}
				else{
					flag=1;
                    break;
				}
			}
		}
		if(!flag)break;
        }
		printf("Case #%d: %d\n",tcase,j);
        }
    return 0;
	}


