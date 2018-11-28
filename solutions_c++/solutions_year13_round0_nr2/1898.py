#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <string>

using namespace std;
char *checkGame( int map[100][100], const int mapSizeX, const int mapSizeY ){
	const int maxSize = 100;
	char *ret = NULL;

	vector<int> hList;
	vector<int> numList;
	while(1){
		int hListMax = 0;
		if( hList.size() ){
			hListMax = hList[ hList.size() - 1 ];
		}
		int next = -1;
		for( int v = 0; v < mapSizeY; v++ ){
			for( int u = 0; u < mapSizeX; u++ ){
				int m = map[v][u];
				if( m > hListMax && (next < 0 || m < next) ){
					next = m;
				}
			}
		}
		if( next > 0 ){
			hList.push_back( next );
		}
		else{
			break;
		}
	}
	//for( int i = 0; i < hList.size(); i++ ){
	//	const int level = hList[i];
	//	int count = 0;
	//	for( int v = 0; v < mapSizeY; v++ ){
	//		for( int u = 0; u < mapSizeX; u++ ){
	//			if( map[v][u] == level ) count++;
	//		}
	//	}
	//	numList.push_back( count );
	//}

	//for( int i = 0; i < hList.size(); i++ ){
	//	printf( "%d ", hList[i] );
	//}
	//printf("\n");

	bool check = true;
	for( int i = 0; i < hList.size() && check; i++ ){
		const int level = hList[i];
		int subMap[maxSize][maxSize] = {0};
		for( int v = 0; v < mapSizeY; v++ ){
			bool flag = false;
			for( int u = 0; u < mapSizeX && !flag; u++ ){
				if( map[v][u] == level ) flag = true;
			}
			for( int u = 0; u < mapSizeX && flag; u++ ){
				if( map[v][u] >  level ) flag = false;
			}
			for( int u = 0; u < mapSizeX && flag; u++ ){
				if( map[v][u] == level ) subMap[v][u] = level;
			}
		}
		for( int u = 0; u < mapSizeX; u++ ){
			bool flag = false;
			for( int v = 0; v < mapSizeY && !flag; v++ ){
				if( map[v][u] == level ) flag = true;
			}
			for( int v = 0; v < mapSizeY && flag; v++ ){
				if( map[v][u] >  level ) flag = false;
			}
			for( int v = 0; v < mapSizeY && flag; v++ ){
				if( map[v][u] == level ) subMap[v][u] = level;
			}
		}

		for( int v = 0; v < mapSizeY && check; v++ ){
			for( int u = 0; u < mapSizeX && check; u++ ){
				if( map[v][u] == level && subMap[v][u] != level ) check = false;
			}
		}
	}
	if( check == true ){
		ret = "YES";
	}
	else{
		ret = "NO";
	}


	return ret;
}


int main( int argc, char *argv[] )
{
	char input[512];
#if 1
	strcpy( input, argv[1] );
#else if
	strcpy( input, "B-large.in" );
#endif
	printf( "input = %s\n", input );
	FILE *fp = fopen( input, "r" );

	if( fp != NULL ){
		char buff[512] = {0};
		int dataNum = 0;

		fgets( buff, 512-1, fp );
		sscanf( buff, "%d", &dataNum );
		printf( "dataNum = %d\n", dataNum );
		char (*out)[256] = new char[dataNum][256];
		for( int i = 0; i < dataNum; i++ ){

			int map[100][100] = {0};
			int mapSizeX, mapSizeY;
			fscanf( fp, "%d",  &mapSizeY );
			fscanf( fp, "%d",  &mapSizeX );
			printf( "%d %d\n", mapSizeY, mapSizeX );
			for( int v = 0; v < mapSizeY; v++ ){
				for( int u = 0; u < mapSizeX; u++ ){
					fscanf( fp, "%d", &map[v][u] );
				}
			}
			for( int v = 0; v < mapSizeY; v++ ){
				for( int u = 0; u < mapSizeX; u++ ){
					printf("%d", map[v][u] );
				}
				printf("\n");
			}
			char *ret = checkGame( map, mapSizeX, mapSizeY );
			sprintf( out[i], "Case #%d: %s", i+1, ret );
			printf( "%s\n", out[i] );
		}
		fclose(fp);

		fp = fopen( "Lawnmower.out", "w" );
		for( int i = 0; i < dataNum; i++ ){
			fprintf( fp, "%s\n", out[i] );
		}
		fclose(fp);
		delete []out;
	}
	return 0;
}