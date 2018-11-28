#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

std::ifstream	inFile;
axFile			outFile;

axStatus	output( int caseNo, int answer ) {
	axStringA_<256>	tmp;
	
	tmp.format("Case #{?}: ", caseNo );
	
	if( answer == 0 ) {
		tmp.appendFormat("Volunteer cheated!" );
	}else if( answer == -1 ) {
		tmp.appendFormat("Bad magician!");
	}else{
		tmp.appendFormat("{?}", answer);
	}
	
	tmp.append("\n");
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

axStatus	doCase( int caseNo ) {
//	inFile >> xxxx;
	int a0;
	int a1;

	int	c0[4][4];
	int	c1[4][4];
	
	inFile	>> a0;
	for( int i=0; i<4; i++ ) {
		for( int j=0; j<4; j++ ) {
			inFile >> c0[i][j];
		}
	}

	inFile >> a1;
	for( int i=0; i<4; i++ ) {
		for( int j=0; j<4; j++ ) {
			inFile >> c1[i][j];
		}
	}
	
	auto row0 = c0[a0-1];
	auto row1 = c1[a1-1];

	int ans = 0;
	
	for( int i=0; i<4; i++ ) {
		auto s = row0[i];
		
		for( int j=0; j<4; j++ ) {
			if( row1[j] == s ) {
				if( ans != 0 ) {
					ans = -1;	break;
				}
				ans = s;
			}
		}
	}
	
	output( caseNo, ans );
	
	return 0;
}

axStatus	run() {
	axStatus	st;
		
	inFile.open("A-small-attempt0.in");
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

