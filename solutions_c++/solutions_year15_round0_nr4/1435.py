#include<bits/stdc++.h>
using namespace std;

int main(){
	int N,NN;
	cin >> N;
	NN=N;
	while(N--){
		int x,r,c;
		cin >> x >> r >> c;
		if( ((r*c)%x!=0) || (x==3 && r*c==3) || (x==4 && r*c==4) || (x==4 && r*c==8) )
			printf("Case #%d: RICHARD\n",NN-N);
		else	
			printf("Case #%d: GABRIEL\n",NN-N);	
	}
}
