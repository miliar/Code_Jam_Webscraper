#include <string.h>
#include <iostream>
#include <vector>
#define MAX_LENGTH 9999
using namespace std;

int lawn[100][100]; // N, M
int max_n[100];
int max_m[100];

void get_max_mn (int n, int m)
{
	memset(max_m, 0, sizeof(int)*100);
	memset(max_n, 0, sizeof(int)*100);
	for ( int nloop=0; nloop<n; nloop++ )
	for ( int mloop=0; mloop<m; mloop++ )
	{
		if ( max_m[nloop] < lawn[nloop][mloop] ) max_m[nloop] = lawn[nloop][mloop];
		if ( max_n[mloop] < lawn[nloop][mloop] ) max_n[mloop] = lawn[nloop][mloop];
	}

	cout << "max_m : "; for ( int nloop=0; nloop<n; nloop++ ) cout << max_m[nloop] << " "; cout << endl;
	cout << "max_n : "; for ( int mloop=0; mloop<m; mloop++ ) cout << max_n[mloop] << " "; cout << endl;
	cout << endl;
}

bool check_yes(int n, int m)
{
	for ( int nloop=0; nloop<n; nloop++ )
	for ( int mloop=0; mloop<m; mloop++ )
	{
		if ( lawn[nloop][mloop] < max_n[mloop] && lawn[nloop][mloop] < max_m[nloop] ) return false;
	}
	return true;
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
		int n, m;
		fscanf(in_file, "%d %d\n", &n, &m);
		cout << "T:" << tloop+1 << " : " << n << " " << m << endl;
		for ( int nloop=0; nloop<n; nloop++ )
		for ( int mloop=0; mloop<m; mloop++ )
		{
			fscanf(in_file, "%d", &lawn[nloop][mloop]);
		}

		get_max_mn (n, m);

		for ( int nloop=0; nloop<n; nloop++, cout << endl )
		for ( int mloop=0; mloop<m; mloop++ )
		{
			cout << lawn[nloop][mloop] << " ";
		}
		cout << endl;

		if( check_yes(n, m) ) sprintf(out_string, "Case #%d: YES\n", tloop+1);
		else                  sprintf(out_string, "Case #%d: NO\n" , tloop+1);
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}