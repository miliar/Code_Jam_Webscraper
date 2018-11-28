
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout<<x<<" "<<y<<endl
#define MAXN 100005


using namespace std;

int T[4][4], F[17];

void read(int fil){
	
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)scanf("%d", &T[i][j]);
		
	for(int j = 0; j < 4; j++)F[T[fil][j]]++;
	
}

int main(){

	int T = 0, caso = 1;
	scanf("%d", &T);
	
	while(T--){
		
		int fil;
		memset(F, 0, sizeof F);
		
		scanf("%d", &fil);
		fil--;
		read(fil);
			
		
		scanf("%d", &fil);
		fil--;
		read(fil);

		int ct = 0, ans;
		for(int i = 1; i <= 16; i++)if(F[i] > 1)ct++, ans = i;
		
		printf("Case #%d: ", caso++);
		
		if(ct == 0)printf("Volunteer cheated!\n");
		else{
			
			if(ct > 1)printf("Bad magician!\n");
			else printf("%d\n", ans);
		}
		
	}


}

