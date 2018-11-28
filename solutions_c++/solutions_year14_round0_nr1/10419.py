
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)

#define MAXN 100005


using namespace std;

int T1[4][4], frec[17];

void process(int f){
	
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)scanf("%d", &T1[i][j]);
		
	for(int j = 0; j < 4; j++)frec[T1[f][j]]++;
	
}

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int fil;
		memset(frec, 0, sizeof frec);
		
		scanf("%d", &fil);
		fil--;
		process(fil);
			
		
		scanf("%d", &fil);
		fil--;
		process(fil);

		int ct = 0, ans;
		for(int i = 1; i <= 16; i++)if(frec[i] > 1)ct++, ans = i;
		
		printf("Case #%d: ", caso++);
		
		if(ct == 0)printf("Volunteer cheated!\n");
		else{
			
			if(ct > 1)printf("Bad magician!\n");
			else printf("%d\n", ans);
		}
		
	}


}

