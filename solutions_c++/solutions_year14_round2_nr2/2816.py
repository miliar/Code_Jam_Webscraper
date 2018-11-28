#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<string>

#define MAX(a,b) ((a) > (b) ? a : b)
#define MIN(a,b) ((a) < (b) ? a : b)
#define IT(a,it) for(auto it=a.begin(); it != a.end(); it++)
#define REV_IT(a,it) for(auto it=a.rbegin(); it != a.rend(); it++)
#define MAXX 1000

using namespace std;
int a,b,k,ans = 0,temp,cou;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T, casee = 1, i, j;
	scanf("%d",&T);
	for(casee=1;casee<=T;casee++){
		ans = 0;cou = 0;temp = 0;
		printf("Case #%d: ",casee);
		cin>>a>>b>>k;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				temp = i bitand j;
				if(temp<k){
					//if(i==j) cou++;
					ans++;
					//cout<<i<<" "<<j<<" "<<temp<<endl;
				}
			}
		}
		cout<<ans-cou<<endl;
	}
	fclose(stdin);
	fclose(stdin);
return 0;
}

