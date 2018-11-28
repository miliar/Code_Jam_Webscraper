#include <fstream>
#include <ax/ax_core.h> //libax.googlecode.com

std::ifstream	inFile;
axFile			outFile;

typedef	axArray< axArray<int, 100>, 100 >	Lawn;

axStatus	output( int c, int a,  int b ) {
	axStringA_<256>	tmp;
	
	tmp.format("Case #{?}: {?} {?}", c, a,b );
	
	
	tmp.append("\n");
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

class Node : public axDListNode<Node,true> {
public:
	double	v;
	
	axStatus	toStringFormat( axStringFormat & f ) const {
		f.out( v );
		return 0;
	}
	
	bool largerThan( const Node & a ) {
		return v > a.v;
	}
};

axStatus	doCase( int caseNo ) {
	int n;
	inFile >> n;

	axArray<int,1000>	nao;
	axArray<int,1000>	ken;
	
	
	for( int i=0; i<n; i++ ) {
		double v;
		inFile >> v;
		nao.append(v*100000);
	}
	for( int i=0; i<n; i++ ) {
		double v;
		inFile >> v;
		ken.append(v*100000);
	}
	
	nao.bubbleSort( true );
	ken.bubbleSort( true );
	
	int i=0;
	int j=0;
	for(;;) {
		if( i >= n || j >=n ) break;
	
		if( nao[i] > ken[j] ) {
			j++;
			continue;
		}
		
		i++;
		j++;
	}
	
	int b = n-i;
			

//	ax_log_var( ken );
//	ax_log_var( nao );
	
	i=0;
	j=0;
	for(;;) {
		if( i >= n || j >=n ) break;
	
		if( ken[i] > nao[j] ) {
			j++;
			continue;
		}
		
		i++;
		j++;
	}

	int a = i;

		
	output( caseNo, a, b );
	
	return 0;
}

axStatus	run() {
	axStatus	st;
		
	inFile.open("D-large.in");
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

