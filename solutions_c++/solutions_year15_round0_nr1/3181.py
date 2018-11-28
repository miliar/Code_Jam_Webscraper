#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char** argv) {
	int t,maxlevel,cas=1;
	freopen("zzz.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d",&maxlevel); 
		string audlevel;
		cin>>audlevel;
		int nowstand=0,add=0;
		for(int q=0;q<=maxlevel;q++){
			int z=audlevel[q]-'0';
			
			if( q > nowstand ){
				add += q -nowstand;
				nowstand = q + z;
			}
			else nowstand += z;
		}
		printf("Case #%d: %d\n",cas,add);
		cas++;
	}
	
}
