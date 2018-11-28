#include <string.h>
#include <iostream>
#include <vector>
#define MAX_LENGTH 9999
using namespace std;

vector<__int64> vector_p;
vector<__int64> vector_fs;

__int64 find_next_p(__int64 in_num)
{
	char num_string[150];
	sprintf(num_string, "%I64d\0", in_num);
	int num_length = strlen(num_string);
	sprintf(num_string, "%I64d\0", in_num/__int64(pow(10, num_length/2)));
	int o_half_strlen = strlen(num_string);
	sprintf(num_string, "%I64d\0", in_num/__int64(pow(10, num_length/2)) + 1);
	if ( o_half_strlen < strlen(num_string) ) num_length++;
	for (int loop=0; loop<num_length/2; loop++) num_string[num_length-loop-1] = num_string[loop];
	return _atoi64(num_string);
}

bool is_p(__int64 in_num)
{
	char num_string[150];
	sprintf(num_string, "%I64d\0", in_num);
	int num_length = strlen(num_string);
	for (int loop=0; loop<num_length/2; loop++) 
		if (num_string[num_length-loop-1] != num_string[loop]) return false;
	return true;
}

void find_fs()
{
	__int64 p = 0, max = 100000000000000000, p2 = 0;
	while ( p2 < max )
	{
		p = find_next_p(p);
		vector_p.push_back(p);
		p2 = p*p;
		if ( p2 <= max && is_p(p2) ) vector_fs.push_back(p2);
	}
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
	
	find_fs(); 
	cout << "p  count : " << vector_p.size() << endl;
	cout << "fs count : " << vector_fs.size() << endl;
	//for ( int loop = 0; loop<vector_fs.size(); loop++ ) cout << loop+1 << ": " << vector_fs[loop] << endl;
	for ( int tloop=0; tloop<T; tloop++ )
	{
		__int64 a, b;
		fscanf(in_file, "%I64d %I64d\n", &a, &b);
		cout << "T:" << tloop+1 << " : " << a << " " << b << endl;
		__int64 count = 0;
		for ( int loop = 0; loop<vector_fs.size(); loop++ )
		{
			if ( vector_fs[loop] >= a && vector_fs[loop] <= b ) count++;
		}

		sprintf(out_string, "Case #%d: %I64d\n", tloop+1, count);
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}