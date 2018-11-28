#include<cstdio>
#include<set>

using namespace std;

main(){
	set<int> s;
	int N,resp1,resp2,num,caso = 1;
	scanf("%d",&N);
	while(N--){
		s.clear();
		scanf("%d",&resp1);
		int a = 4*(resp1-1); for(int i=0;i<a;++i) scanf("%*d");
		for(int i=0;i<4;++i) {scanf("%d",&num); s.insert(num);}
		a = 4*(4-resp1); for(int i=0;i<a;++i) scanf("%*d");
	
		/*set<int>::iterator it = s.begin();
		for(;it!= s.end();it++){
			printf("%d ",*it);
		}
		printf("\n");*/

		int achou = 0,carta;
		scanf("%d",&resp2);
		a = 4*(resp2-1); for(int i=0;i<a;++i) scanf("%*d");
		for(int i=0;i<4;++i) {
			scanf("%d",&num);
			if(s.find(num) != s.end()){
				achou++;
				carta = num;
			}// da pra podar aqui quando acho > 1
		}
		a = 4*(4-resp2); for(int i=0;i<a;++i) scanf("%*d");

		printf("Case #%d: ",caso++);
		if(achou > 1){
			printf("Bad magician!\n");
		}else if(achou == 0){
			printf("Volunteer cheated!\n");
		}else{
			printf("%d\n",carta);
		}

		


	
	}

}
