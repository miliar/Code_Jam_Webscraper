#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

std::ifstream	inFile;
axFile			outFile;

typedef	axArray< axArray<int, 100>, 100 >	Lawn;

axStatus	output( int c, bool result ) {
	axStringA_<256>	tmp;
	tmp.format("Case #{?}: {?}\n", c+1, result ? "YES":"NO" );
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

axStatus	doCase( int c ) {
	axStringA	buf;
	int	N, M;
	
	inFile >> N >> M;

	Lawn	a;
	Lawn	b;
	
	axArray< int, 100 >		nMax;
	axArray< int, 100 >		mMax;
	
	a.resize( N );
	
	nMax.resize( N );	nMax.setAll(0);
	mMax.resize( M );	mMax.setAll(0);
	
	for( int n=0; n<N; n++ ) {
		a[n].resize( M );
		for( int m=0; m<M; m++ ) {
			int v;
			inFile >> v;
			
			ax_max_it( nMax[n], v );
			ax_max_it( mMax[m], v );
			
			a[n][m] = v;
		}
	}
//--------------
	for( int n=0; n<N; n++ ) {
		for( int m=0; m<M; m++ ) {
			int v = a[n][m];
			if( v == nMax[n] ) continue;
			if( v == mMax[m] ) continue;
			output( c, false );
			return 0;
		}
	}

	output( c, true );
	return 0;
}

axStatus	run() {
	axStatus	st;
		
	inFile.open("B-large.in");
	if( ! inFile.is_open() ) return -1;
	
	st = outFile.openWrite("out.txt", true, true);		if( !st ) return st;

	axStringA	buf;
	int C;
	inFile >> C;
	for( int c=0; c<C; c++ ) {
		st = doCase( c );			if( !st ) return st;
	}



	return 0;
}


axStatus	changeDir() {
	axStatus st;
	axStringA path;
	st = axFilePath::getDirName(path, __FILE__ );		if( !st ) return st;
	st = axFileSystem::setCurrentDir(path);				if( !st ) return st;
	return 0;
}


int main(int argc, const char * argv[]) {
	axScope_NSAutoreleasePool	pool;

	changeDir();

	axStatus st = run();
	ax_log("===== end of program - return {?} =====", st );

    return 0;
}

