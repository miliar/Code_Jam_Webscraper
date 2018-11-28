#include <string.h>
#include <iostream>
#include <vector>
#define MAX_LENGTH 9999
using namespace std;

__int64 a, b, ans;
__int64 a0;

__int64 find_value(__int64 start, __int64 end)
{
	a0 = 2*a+1;
	__int64 n = start + (end - start) / 2;
	__int64 sum = (a0 + a0+4*(n-1))*n / 2;
	if ( n > b || sum < 0 ) sum = b+1;

	if ( sum == b ) return n;
	else if ( sum >  b ) {  if ( start == end ) find_value(start-1, n-1);
							else return find_value(start, n); }
	else if ( sum <  b ) {	if ( start == end ) return start;
							else return find_value(n+1, end); }
}

int main()
{
	FILE *in_file, *out_file;
	char in_string [MAX_LENGTH];
	char out_string[MAX_LENGTH];

	in_file  = fopen("in.txt",  "r");
	out_file = fopen("out.txt", "w");
	if ( in_file  == NULL ) { cout << "in.txt open error" <<  endl; exit(0); }
	if ( out_file == NULL ) { cout << "out.txt open error" << endl; exit(0); }

	int T = 0;
	fscanf(in_file, "%d\n", &T);
	cout << "T:" << T << endl;
	
	for ( int tloop=0; tloop<T; tloop++ )
	{
		fscanf(in_file, "%I64d %I64d\n", &a, &b);
		cout << "T:" << tloop+1 << " : " << a << " " << b << endl;

		ans = find_value(1, 10000000000);
		sprintf(out_string, "Case #%d: %I64d\n", tloop+1, ans);
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}