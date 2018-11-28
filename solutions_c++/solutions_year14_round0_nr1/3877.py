
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)


void preprocess()
{
}

void solve()
{
}


int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);;
#endif

int n=1,t;
int answer1,answer2;
int grid1[4];
int grid2[4];
int tmp;
cin>>t;

while(n<=t){
cin>>answer1;
for(int i=0;i<4;i++){
	for(int j=0;j<4;j++){
		if(i==answer1-1)
			cin>>grid1[j];
		else
			cin>>tmp;
	}
}
cin>>answer2;
for(int i=0;i<4;i++){
	for(int j=0;j<4;j++){
		if(i==answer2-1)
			cin>>grid2[j];
		else
			cin>>tmp;
	}
}

int card=-1,foundOnce=0,moreThanOnce=0;
for(int i=0;i<4;i++){
	for(int j=0;j<4;j++){
		if(grid1[i]==grid2[j]){
			if(foundOnce){
				moreThanOnce=1;			
			}
			else{
				foundOnce=true;
				card=grid1[i];
			}
			break;
		}
	}
	if(moreThanOnce)
		break;
}

cout<<"Case #"<<n<<": ";
if(moreThanOnce)
   cout<<"Bad magician!";
else if(foundOnce)
	cout<<card;
else
	cout<<"Volunteer cheated!";
cout<<endl;
n++;
}



#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

