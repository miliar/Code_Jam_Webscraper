#include<bits/stdc++.h>
using namespace std;

int T,L,X;
int w[500][500] = {0};

int main(){
    scanf("%d", &T);
    w[1][1] = 1; w['i']['i'] = w['j']['j'] = w['k']['k'] = -1;
    w[1]['i'] = 'i'; w[1]['j'] = 'j'; w[1]['k'] = 'k';
    w['i'][1] = 'i'; w['i']['j'] = 'k'; w['i']['k'] = -'j';
    w['j'][1] = 'j'; w['j']['i'] = -'k'; w['j']['k'] = 'i';
    w['k'][1] = 'k'; w['k']['i'] = 'j'; w['k']['j'] = -'i';

    for(int qwe=1; qwe<=T;qwe++){
	scanf("%d%d", &L, &X);
	string s = "",t = "";
	cin >> t;
	for(int i=0; i<X;i++)  s+=t;
	int C = 1, signC = 0;
	for(int i=0, j=s.length(); i<j;i++){
	    C = w[C][s[i]];
	    if(C < 0) { C=-C; signC=!signC;}
	}	    
	C = w['i'][C];
	if(C < 0) { C=-C; signC=!signC;}
	C = w[C]['k'];
	if(C < 0) { C=-C; signC=!signC;}
	//if has prefix i && postfix k, no j	
	if(C != 'j' || signC) printf("Case #%d: NO\n", qwe);
	else{
	    int fi = 1, signI = 0, pi = -1, fk = 1, signK = 0;
	    bool ok = 0;
	    for(int i=0, j=s.length(); i<j;i++){
		fi = w[fi][s[i]];
		if(fi < 0) {fi=-fi; signI=!signI;}
		if(fi == 'i' && !signI){ pi=i; break;}
	    }
	    if(pi!= -1){
		for(int i=s.length()-1; i>pi; i--){
		    fk = w[s[i]][fk];
		    if(fk < 0) {fk=-fk; signK=!signK;}
		    if(fk == 'k' && !signK){ ok = 1; break;}
		}
	    }
	    if(ok) printf("Case #%d: YES\n",qwe);
	    else printf("Case #%d: NO\n", qwe);
	}
    }
    return 0;
}
