#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>
#include<queue>

using namespace std;

int N;
char Parties[27]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
priority_queue <pair<int,int> > P;

int main(){
	int t;
	scanf("%d",&t);
	for(int time=1;time<=t;time++){
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			int tmp;
			scanf("%d",&tmp);
			P.push(make_pair(tmp,i));
		}
		printf("Case #%d: ",time);
		while(true){
			for(int i=0;i<2;i++){
				int num = P.top().first;
				int party = P.top().second;
				P.pop();
				printf("%c",Parties[party]);
				num--;
				if(num==0&&P.size()==2)break;
				else if(num!=0)P.push(make_pair(num,party));
			}
			if(P.empty())break;
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}
				
