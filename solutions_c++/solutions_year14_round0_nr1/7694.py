#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
typedef long long INT;



int main(){
	int i,j,tst,cas=1,n1,n2;
	int arr[3][20];
	vector <int> myv;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&tst);

	while(tst--){
		scanf("%d",&n1);
		for(i=0;i<16;i++){
			scanf("%d",&arr[0][i]);
		}
		scanf("%d",&n2);
		for(i=0;i<16;i++){
			scanf("%d",&arr[1][i]);
		}

		myv.clear();
		for(i=(n1-1)*4;i<n1*4;i++){
			for(j=(n2-1)*4;j<n2*4;j++){
				if(arr[0][i]==arr[1][j]){
					myv.push_back(arr[0][i]);
				}
			}
		}
		printf("Case #%d: ",cas++);
		if(myv.size()==1){printf("%d\n",myv[0]);}
		else if(myv.size()>1){puts("Bad magician!");}
		else if(myv.size()==0){puts("Volunteer cheated!");}
	}
	
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);