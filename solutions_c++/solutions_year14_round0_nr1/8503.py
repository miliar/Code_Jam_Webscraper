#include <iostream>
#include<cstdio>
#include<cstdlib>
#define REP(i,n) for(int i=0;i<n;i++)
using namespace std;
/*void fastread(int *a)
{    char c=0;
      while(c<33)
      {c=getchar_unlocked();
	  }
      *a=0;
      while(c>33)
      {
       *a=*a*10+c-'0';
       c=getchar_unlocked();
      }
}*/
int main(){
int test,m,i,j,n,X;
int rank[100];
int BOT[100][100];
int Arr[100][100];
cin>>test;
int Y=1;
while(test--){
int count=0;
cin>>m;
	REP(i,4)
	{
		REP(j,4){
			cin>>BOT[i][j];
			
		}
	}
	cin>>n;
	REP(i,4){
		REP(j,4){
			cin>>Arr[i][j];
			}}
X=0;
REP(i,4){
REP(j,4){ 
				if(BOT[m-1][i]==Arr[n-1][j]){
		
			count++;
			rank[X]=BOT[m-1][i];
        X++;			
			}
			
		}
	}
	
	if(count==1)
	{
	printf("Case #%d: %d\n",Y,rank[0]);
	}
	else if(count>1)
	{
	printf("Case #%d: Bad magician!\n",Y);
	}
	else{
	printf("Case #%d: Volunteer cheated!\n",Y);
	}
	Y++;
	}
	}