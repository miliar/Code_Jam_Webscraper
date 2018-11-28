#include <fstream>

int get_front_diff( int * line, int len );

int main()
{
	//open files.
	std::ifstream in;
	std::ofstream out;

	in.open("B-large.in");
	out.open("B-large.out");

	//global variables.
	int T, N, M;
	int * lawn;
	bool is_end;

	//in and out.
	in >> T;
	for( int t = 0; t < T; t ++ )
	{
		in >> N >> M;

		//get lawn.
		lawn = new int[ N * M ];
		is_end = true;

		for( int n = 0; n < N; n ++ )
		{
			for( int m = 0; m < M; m ++ )
			{
				in >> lawn[ m + n * M ];
			}
		}

		out << "Case #" << t + 1 << ": ";

		//search on rows.
		for( int n = 0; n < N; n ++ )
		{
			for( int m = 0; m < M; m ++ )
			{
				for( int i = 0; i < M; i ++ )
				{
					if( lawn[ m + n * M ] < lawn[ i + n * M ] )
					{
						for( int j = 0; j < N; j ++ )
						{
							if( lawn[ m + n * M ] < lawn[ m + j * M ] )
							{
								is_end = false;
								break;
								break;
								break;
								break;
							}
						}
					}
				}
			}

			//int index = get_front_diff( lawn + n * M, M );

			//if( index != 0 )
			//{
			//	//copy column to a array.
			//	int *arr = new int [ N ];
			//	for( int i = 0; i < N; i ++ )
			//	{
			//		arr[i] = lawn[ index + i * M ];
			//	}

			//	if( 0 != get_front_diff( arr, N ) )
			//	{
			//		is_end = false;
			//		break;
			//	}
			//}
		}

		

		//if all search done, there will be no problem.
		if( is_end )
		{
			out << "YES" << std::endl;
		}else
		{
			out << "NO" << std::endl;
		}
	}

	//close files.
	in.close();
	out.close();

	return 0;
}

int get_front_diff( int * line, int len )
{
	for( int i = 1; i < len ; i ++ )
	{
		if( line[ 0 ] > line[ i ] )
		{
			return i;
		}
	}

	return 0;
}