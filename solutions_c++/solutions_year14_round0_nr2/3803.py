#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

std::ifstream	inFile;
axFile			outFile;

axStatus	output( int c, double ans ) {
	axStringA_<256>	tmp;
	
	tmp.format("Case #{?}: ", c );

	tmp.appendFormat("{?:0.7lf}", ans);
	
	tmp.append("\n");
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

axStatus	doCase( int caseNo ) {

	double C, F, X;

	inFile >> C >> F >> X;

	double R = 2;

	double ans = X / R;
	double sum = C / R;
	
	for(;;) {
		R += F;
		double s = X / R + sum;
		
		if( s > ans ) break;
		ans = s;
		sum += C / R;
	}
	
	
	output( caseNo, ans );
	
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
		st = doCase( c+1 );			if( !st ) return st;
	}
	return 0;
}


axStatus	changeDir() {
	axStatus st;
	axStringA path;
	st = axFilePath::dirName(path, __FILE__ );		if( !st ) return st;
	st = axFileSystem::setCurrentDir(path);				if( !st ) return st;
	return 0;
}


int main(int argc, const char * argv[]) {
	@autoreleasepool {
		changeDir();

		axStatus st = run();
		ax_log("===== end of program - return {?} =====", st );
	}
    return 0;
}

