#include <stdio.h>
#include <string.h>


int main () {

	FILE *in;
	FILE *out;
	in = fopen ("A-large.in","r");
	out = fopen ("Al.out","w");

	char s[2001];

	int t,n0=0,n2=0,n4=0,n6=0,n8=0,n9=0,n7=0,n5=0,n3=0,ln=0,n1=0;
	fscanf(in,"%d",&t);


	for (int i=0;i<t;i++) {
		fscanf(in,"%s",s);
		for (int j=0;j<strlen(s);j++){
			/// 2 resolvido
			if (s[j]=='W') {
				n2++;
				n1--;
			}

			/// 1 resolvido
			if (s[j]=='O') { 		/// n1 me devolve o numero de 1s
				n1++;
			}

			/// 0 resolvido
			if (s[j]=='Z') {
				n0++;
				n3--;
				n1--;
			}

			/// 4 resolvido
			if (s[j]=='U') {
				n3--;
				n4++;
				n5--;
				n1--;
			}

			/// 3 reosolvido
			if (s[j]=='R') n3++;

			/// 6 resolvido
			if (s[j]=='X') {
				n6++;
				n7--;
			}

			/// 5 resolvido
			if (s[j]=='F') n5++;   

			/// 7 resolvido
			if (s[j]=='S') n7++; 	///n7 vai me devolver o numero de 7s

			/// 8 resolvido
			if (s[j]=='G') n8++;

			/// 9 resolvido fora.
			if (s[j]=='N') ln++;

		}

		n9=(ln-n7-n1);
		n9=n9/2;

		fprintf(out,"Case #%d: ",i+1);
		for (int j=0;j<n0;j++) fprintf(out,"0",s);
		for (int j=0;j<n1;j++) fprintf(out,"1",s);
		for (int j=0;j<n2;j++) fprintf(out,"2",s);
		for (int j=0;j<n3;j++) fprintf(out,"3",s);
		for (int j=0;j<n4;j++) fprintf(out,"4",s);
		for (int j=0;j<n5;j++) fprintf(out,"5",s);
		for (int j=0;j<n6;j++) fprintf(out,"6",s);
		for (int j=0;j<n7;j++) fprintf(out,"7",s);
		for (int j=0;j<n8;j++) fprintf(out,"8",s);
		for (int j=0;j<n9;j++) fprintf(out,"9",s);

		if (i!=(t-1)) fprintf (out,"\n");

		n0=0; n1=0; n2=0; n3=0; n4=0;
		n5=0; n6=0; n7=0; n8=0; n9=0;
		ln=0;

		
	}


	fclose(in);
	fclose (out);
	return 0;
}