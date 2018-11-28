#include <stdio.h>

#define SIZE 10

#if 0
#define IN	stdin
#define OUT	stdout
#else
#define IN	in
#define OUT	out
#endif
int main(int argc, char *argv[])
{
	int T,c=-1;

	FILE *in = fopen(argv[1], "r");
	FILE *out = fopen(argv[2], "w" );

	fscanf(IN, "%d", &T );

	while(++c<T) {

		int r,t,count=0;;
		fscanf(IN, "%d %d", &r, &t);
		r++;
		while(t>0 && t>=((r*r)-((r-1)*(r-1)))) {
			t -= (r*r)-((r-1)*(r-1));
			r +=2;
			count++;
		}
		fprintf(OUT,"Case #%d: %d\n", c+1, count);
	}

	if(in) fclose(in);
	if(out) fclose(out);
	return 0;
}

