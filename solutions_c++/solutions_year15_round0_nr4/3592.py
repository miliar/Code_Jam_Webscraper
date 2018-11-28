#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, x, r, c, k;
	int area=0;
	char ch;
	cin>>t;
	for(k=1; k<=t; k++){
		cin>>x>>r>>c;
		
		area = r*c;
		
		if(x==1){
			ch = 'G';
		}
		else if(x==2){
			if(area%x)
			    ch = 'R';
			else
			    ch = 'G';
		}
		else if(x==3){
			if(area%x)
			    ch = 'R';
			else
			    ch = 'G';
			
		}
		else if(x==4){
			if((r==3 && c==4)||(r==4 && c==3)||(r==4 && c==4))
			    ch = 'G';
			else
			    ch = 'R';
		}
		
		if(ch == 'G')
		    printf("Case #%d: GABRIEL\n", k);
		else if(ch == 'R')
		    printf("Case #%d: RICHARD\n", k);
	}
	return 0;
}