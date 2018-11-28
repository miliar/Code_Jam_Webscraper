# include <stdio.h>
# include <vector>
# include <algorithm>

# define sz(c) (int)(c).size()

using namespace std;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t;
	
	scanf("%d",&t);
	
	for(int _i=0; _i<t; _i++){
		int a1, a2;
		int m1[5][5], m2[5][5];
		
		scanf("%d",&a1);
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&m1[i][j]);
		
		scanf("%d",&a2);
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&m2[i][j]);
		
		a1--, a2--;
		
		vector<int> A;
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(m1[a1][i] == m2[a2][j])
					A.push_back(m1[a1][i]);
		
		printf("Case #%d: ",_i+1);
		
		if(sz(A) == 1)
			printf("%d\n",A[0]);
		
		else if(!sz(A))
			printf("Volunteer cheated!\n");
		
		else
			printf("Bad magician!\n");
	}
}
