#include <conio.h>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

void main () {
	int T, n;

	FILE *f_in, *f_out;
	f_in = fopen("data.txt","r");	
	f_out = fopen("output.txt","w");	
	fscanf(f_in,"%d",&T);

	char buff[1002];
	
	
	for (int t = 0; t < T; ++t) {
		//fscanf(f_in, "%d", &n);
		
		fscanf(f_in, "%s", buff);
		string s(buff), so;

		so += s[0];
		for (int i = 1; i < s.length(); i++) {
			char c =  s[i];
			
			if (so[0] <= c) {
				so = c + so;
			} else {
				so += c;
			}
		}

		fprintf(f_out, "Case #%d: ", t+1 );

		fprintf(f_out, "%s\n", so.c_str());
	}
	 

}