#include<cstdio>
#include<set>

int cards[17];

int main(){
	int testcase,tc;
	int row;
	int i,j;

	int a,b,c,d,count;

	int ans;

	scanf("%d",&testcase);
	for(tc=1;tc<=testcase;tc++){
		for(i=1;i<=16;i++) cards[i] = 0;
		count = 0;

		scanf("%d",&row);
		for(i=1;i<=4;i++){
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if(i == row){
				cards[a] = 1;
				cards[b] = 1;
				cards[c] = 1;
				cards[d] = 1;
			}
		}
		scanf("%d",&row);
		for(i=1;i<=4;i++){
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if(i == row){
				if(cards[a] == 1){ count++; ans = a; }
				if(cards[b] == 1){ count++; ans = b; }
				if(cards[c] == 1){ count++; ans = c; }
				if(cards[d] == 1){ count++; ans = d; }
			}
		}

		if(count == 0) printf("Case #%d: Volunteer cheated!\n",tc);
		else if(count > 1) printf("Case #%d: Bad magician!\n",tc);
		else printf("Case #%d: %d\n",tc,ans);
	}

	return 0;
}
