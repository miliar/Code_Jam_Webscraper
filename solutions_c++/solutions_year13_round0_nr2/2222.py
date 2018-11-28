#include <stdio.h>
#include <vector>
#include <algorithm>

#define MAX_N 100
#define MAX_M 100
#define MIN_V (-1)
#define MAX_V 100

//#define debugf fprintf
#define debugf __noop

#define MIN(x,y) ((x<y)?(x):(y))

FILE *Fin, *Fout;

int FindMin( int* arr, int len )
{
    int min = MAX_V;
    for( int i=0; i<len; i++ )
        if( min > arr[i] )
            min = arr[i];
    return min;
}

int FindMax( int* arr, int len )
{
    int max = MIN_V;
    for( int i=0; i<len; i++ )
        if( max < arr[i] )
            max = arr[i];
    return max;
}

template<int M, int N> int FindMin( int (&arr)[M][N], int m, int n )
{
    int min = MAX_V;
    for( int i=0; i<m; i++ )
    for( int j=0; i<n; j++ )
        if( min > arr[i][j] )
            min = arr[i][j];
    return min;
}

void Test(int testNo)
{
    static int A[MAX_N][MAX_M];
    static int Rmin[MAX_N], Rmax[MAX_N];
    static int Cmin[MAX_M], Cmax[MAX_M];
	int cmin0 = 0, rmin0 = 0;

    int N = 0, M = 0;
    bool result = false;

#if _DEBUG
	memset( A, 0, sizeof(A) );
	memset( Rmin, 0, sizeof(Rmin) );
	memset( Rmax, 0, sizeof(Rmax) );
	memset( Cmin, 0, sizeof(Cmin) );
	memset( Cmax, 0, sizeof(Cmax) );
#endif

    // read input
    fscanf( Fin, "%d %d\n", &N, &M );

    for( int i=0; i<N; i++ )
        for( int j=0; j<M; j++ )
            fscanf( Fin, "%d", &A[i][j] );

    // restore
    for(;;)
    {
        // build mins
        for( int i=0; i<N; i++ ) Rmin[i] = FindMin( A[i], M );
        for( int i=0; i<N; i++ ) Rmax[i] = FindMax( A[i], M );
        for( int i=0; i<M; i++ ) Cmin[i] = MAX_V;
        for( int i=0; i<M; i++ ) Cmax[i] = MIN_V;

        for( int i=0; i<N; i++ )
            for( int j=0; j<M; j++ )
            {
                int v = A[i][j];
                if( Cmin[j] > v ) Cmin[j] = v;
                if( Cmax[j] < v ) Cmax[j] = v;
            }


        // unwind min
        int rmin = FindMin(Rmin, N);
        int cmin = FindMin(Cmin, M);

		if( rmin == cmin )
		{
			int rmax = FindMax(Rmax, N);
			int cmax = FindMax(Cmax, M);
			if( rmin == rmax && cmin == cmax )
			{
				result = true;
				break;
			}
		}

		bool rfound = false;
        if( rmin <= cmin )
        {
			//if( rmin0 == rmin )
			//{
			//	result = false;
			//	break;
			//}
            for( int i=0; i<N; i++ )
                if( Rmin[i] == rmin && Rmax[i] == rmin )
				{
                    for( int j=0; j<M; j++ )
                        A[i][j] = Cmax[j];
					rfound = true;
				}
			//rmin0 = rmin;
        }
		if( rfound )
			continue;

		bool cfound = false;
        if( cmin <= rmin )
        {
			//if( cmin0 == cmin )
			//{
			//	result = false;
			//	break;
			//}
            for( int j=0; j<M; j++ )
                if( Cmin[j] == cmin && Cmax[j] == cmin )
				{
                    for( int i=0; i<N; i++ )
                        A[i][j] = Rmax[i];
					cfound = true;
				}
			//cmin0 = cmin;
        }
		if( cfound )
			continue;

		break;
    }

    fprintf( Fout, "Case #%d: %s\n", testNo+1, result ? "YES" : "NO" );
}

void Run()
{
    int T = 0;

    fscanf( Fin, "%d\n", &T );
    for( int t=0; t<T; t++ )
    {
        Test(t);
    }
}

int main(int argc, char* argv[])
{
    /*Fin  = fopen(argc >= 2 ? argv[1] : DEFAULT_INPUT , "rt" ); if( Fin  == NULL )*/ Fin  = stdin;
    /*Fout = fopen(argc >= 3 ? argv[2] : DEFAULT_OUTPUT, "w+t"); if( Fout == NULL )*/ Fout = stdout;

    Run();

    fflush(Fout);
    if( Fout != stdout) fclose(Fout);
    if( Fin  != stdin ) fclose(Fin );
    return 0;
}