#include <cstdio>
#include <set>

using namespace std;

multiset <int> mzb;
set <int> zb;
int ile,x,w1,w2;

void powt(){
	int poprz=-1;
	for(multiset <int> :: iterator it=mzb.begin(); it!=mzb.end(); ++it){
		if(*it==poprz){
			printf("%d\n",poprz);
			break;
		}
		poprz=*it;
	}
}

int main(){
	scanf("%d",&ile);
	for(int i=0; i<ile; i++){
		
		if(!zb.empty()){
			zb.clear();
			mzb.clear();
		}
			
		scanf("%d", &w1);
		
		for(int a=1; a<=4; a++)
			for(int b=1; b<=4; b++){
				scanf("%d",&x);
				if(a==w1){
					zb.insert(x);
					mzb.insert(x);
				}
			}

		scanf("%d", &w2);
		
		for(int a=1; a<=4; a++)
			for(int b=1; b<=4; b++){
				scanf("%d",&x);
				if(a==w2){
					zb.insert(x);
					mzb.insert(x);
				}
			}

		printf("Case #%d: ",i+1);
		
		if(zb.size()==8)
			printf("Volunteer cheated!\n");
		else if(zb.size()==7)
			powt();
		else
			printf("Bad magician!\n");
		
	}
}
