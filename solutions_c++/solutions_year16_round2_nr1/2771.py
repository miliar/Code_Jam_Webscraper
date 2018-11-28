#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	FILE *f1, *f2;
	int i, j, k;
	char s[2001];
	int t;
	int cn = 1;
	int cnt[11];
	int mark[200];
	f1 = fopen("A-large.in","r");
	f2 = fopen("output.txt","w");
	fscanf(f1,"%d", &t);
	while(t--) {
		for(i = 64; i <= 91; i++) {
			mark[i] = 0;
		}
		for(i = 0; i < 11; i++) cnt[i] = 0;
		fscanf(f1, "%s", s);
		i = 0;
		while(s[i]) {
			mark[s[i]]++;
			i++;
		}
			if(mark['Z'] > 0) {
				cnt[0] = mark['Z'];
				mark['E']-= mark['Z'] , mark['R']-= mark['Z'], mark['O']-= mark['Z'];
			}  
			if(mark['W'] > 0) {
				cnt[2] = mark['W'];
				mark['T']-= mark['W'];
				 mark['O']-= mark['W'];
			} 
			 if(mark['U'] > 0) {
				cnt[4] = mark['U'];
				mark['F']-= mark['U'];
				 mark['O']-= mark['U'];
				 mark['R']-= mark['U'];
				 
			}
			 if(mark['X'] > 0) {
				cnt[6] = mark['X'];
				mark['S']-= mark['X'];
				 mark['I']-= mark['X'];
			}
			 if(mark['G'] > 0) {
				cnt[8] = mark['G'];
				mark['E']-= mark['G'];
				 mark['I']-= mark['G'];
				 mark['H']-= mark['G'];
				 mark['T']-= mark['G'];
				 
			}
			if(mark['O'] > 0) {
				cnt[1] = mark['O'];
				mark['E']-= mark['O'];
				 mark['N']-= mark['O'];
			}
			if(mark['S'] > 0) {
				cnt[7] = mark['S'];
				mark['N']-= mark['S'];
				 mark['V']-= mark['S'];
				 mark['E']-= mark['S'];
				 mark['E']-= mark['S'];
				 
			}
			if(mark['R'] > 0) {
				cnt[3] = mark['R'];
				mark['T']-= mark['R'];
				 mark['H']-= mark['R'];
				 mark['E']-= mark['R'];
				 mark['E']-= mark['R'];
				 
			}
			if(mark['F'] > 0) {
				cnt[5] = mark['F'];
				mark['I']-= mark['F'];
				 mark['V']-= mark['F'];
				 mark['E']-= mark['F'];
				 
			}
			if(mark['E'] > 0) {
				cnt[9] = mark['E'];
				mark['N']-= mark['E'];
				 mark['N']-= mark['E'];
				 mark['I']-= mark['E'];
				 
			}
			fprintf(f2, "Case #%d: ",cn++);
			for(i = 0; i < 10; i++) {
				for(j = 0; j < cnt[i]; j++) {
					fprintf(f2,"%d",i);
				}
			}
			fprintf(f2,"\n");
			//cout<<endl;
		
	}
	
	return 0;
}
