// Qualification Round
// Problem A Small

#include <stdio.h>
#include <vector>
using namespace std;

#define pb push_back

int main(){
	bool f;
	int T,A,B, ti,i,j,k;
	vector<int> c,r;
	FILE *fi = fopen("a_small.in","r"),
		*fo = fopen("a_small.out","w");
	fscanf(fi,"%d\n",&T);
	for(ti = 1; ti <= T; ti++){
		c.clear(); r.clear();
		fscanf(fi,"%d\n",&A);
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++){
				fscanf(fi,"%d",&B);
				if(i == A-1)
					c.pb(B);
			}
		fscanf(fi,"%d\n",&A);
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++){
				fscanf(fi,"%d",&B);
				if(i == A-1){
					f = false;
					for(k = 0; k < c.size(); k++)
						if(B == c[k]){
							f = true;
							break;
						}
					if(f)
						r.pb(B);
				}
			}
		if(r.size() == 1)
			fprintf(fo,"Case #%d: %d\n",ti,r[0]);
		else if(r.size() > 1)
			fprintf(fo,"Case #%d: Bad magician!\n",ti);
		else
			fprintf(fo,"Case #%d: Volunteer cheated!\n",ti);
	}
	fclose(fi); fclose(fo);
	return 0;
}

