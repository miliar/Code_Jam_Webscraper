#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#define MAX_LENGTH 9999
using namespace std;

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
	fscanf(in_file, "%d\n", &T); //%I64d 
	cout << "T:" << T << endl;
	
	__int64 n;
	#define max_l 1000001
	char *str = (char *)malloc(max_l);
	for ( int tloop=0; tloop<T; tloop++ )
	{
		memset(str, 0, max_l);
		fscanf(in_file, "%s %I64d\n", str, &n);
		cout << "T:" << tloop+1 << " : " << str << " " << n << endl;

		__int64 ans = 0;
		int from_idx = 0;
		int tmp_strlen = strlen(str);

		for ( int start_loop=0; start_loop<tmp_strlen; start_loop++ )
		{
			int c_count = 0;
			for ( int loop=start_loop; loop<tmp_strlen; loop++ )
			{
				if ( str[loop] == 'a'	|| str[loop] == 'e'	|| str[loop] == 'i' 
				  || str[loop] == 'o'	|| str[loop] == 'u' ) 
				{
					 c_count = 0; 
					 continue;
				}
				
				c_count++;

				if ( c_count >= n ) 
				{
					ans += (tmp_strlen - loop);
					break;
				}
			}
		}
		sprintf(out_string, "Case #%d: %I64d\n", tloop+1, ans);
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}