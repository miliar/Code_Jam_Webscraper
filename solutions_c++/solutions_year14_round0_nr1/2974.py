#include <iostream>
#include <cstdio>
using namespace std;

#define forn(i,n) for(int i=0; i<(int)(n); i++)

int cards[32];

int main(){
	int t; cin>>t;
	forn(tc,t){
		forn(i,32)cards[i]=0;
		int a; cin>>a;
		forn(i,4)forn(j,4){
			int c; cin>>c;
			if(i+1==a)cards[c]=1;	
		}
		cin>>a;
		int num_answers = 0;
		int y = -1;
		forn(i,4)forn(j,4){
			int c; cin>>c;
			if (i+1==a){
				if(cards[c]==1){
					num_answers++;
					y=c;
				}
			}
		}
		if(num_answers==0)printf("Case #%d: Volunteer cheated!\n", tc+1);
		if(num_answers==1)printf("Case #%d: %d\n", tc+1, y);
		if(num_answers >1)printf("Case #%d: Bad magician!\n", tc+1);
	}
}
