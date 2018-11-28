#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

using namespace std;

ifstream	inFile;
axFile		outFile;


axStatus	output( int c, int result ) {
	axStringA_<256>	tmp;
	
	tmp.format("Case #{?}: {?}", c, result );
	
	
	tmp.append("\n");
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

axStatus	doCase( int caseNo ) {
//	ax_log("=== doCase {?} ===", caseNo );
	int	A;
	int	N;
	
	inFile >> A;
	inFile >> N;
	
	axArray<int>	n;
	n.resize(N);
	
	for( int i=0; i<N; i++ ) {
		inFile >> n[i];
	}
	n.bubbleSort( true );

//	ax_log_var( n );
	
	int	op = 0;
	int a = A;
	
	for( int i=0; i<N ; i++ ) {
		bool done = false;
		
		int v = n[i];
		int add_op = 0;
		
		for(;;) {
//			ax_log_var2( a, v );
			if( a > v ) {
				a += v;
				break;
			}
		
			if( a == 1 ) {
				op += N-i;
				done = true;
				break; // cannot add any more, sub from the end
			}
		
//			ax_log("+{?}", a-1);
			a += a-1;
			add_op++;
		}
		
		if( done ) break;
	
//		ax_log_var( add_op );
		if( add_op >= N-i ) {
			op += N-i;
			break; // sub from the end is better
		}
		op += add_op;
	}

	output( caseNo, op );
	
	return 0;
}

axStatus	run() {
	axStatus	st;
		
	inFile.open("A-small-attempt3.in");
//	inFile.open("test.txt");
	if( ! inFile.is_open() ) return -1;
	
	st = outFile.openWrite("out.txt", true, true);		if( !st ) return st;

	axStringA	buf;
	int C;
	inFile >> C;
	for( int c=0; c<C; c++ ) {
		st = doCase( c+1 );			if( !st ) return st;
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

