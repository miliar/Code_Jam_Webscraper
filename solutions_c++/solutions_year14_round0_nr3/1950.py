#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Mines{
	int w, h, mines, trueMines;
	int right=0, bottom=0;
	vector<vector<bool>> map;
	vector<vector<bool>> temp;
	
	Mines(){
		cin >> h >> w >> mines;
		trueMines = mines;
		for( int ix=0; ix<w; ix++ )
			map.push_back( vector<bool>( h, false ) );
	}
	
	bool reset(){
		for( int ix=0; ix<w; ix++ )
			for( int iy=0; iy<h; iy++ )
				map[ix][iy] = false;
		mines = trueMines;
		right = 0;
		bottom = 0;
	}
	
	bool fill2x2(){
		int free_h = h - bottom;
		int free_w = w - right;
		
		if( free_h == 1 && free_w == 2 && mines == 1 ){
			map[1][0] = true;
			mines = 0;
			return true;
		}
		if( free_h == 2 && free_w == 1 && mines == 1 ){
			map[0][1] = true;
			mines = 0;
			return true;
		}
		if( free_h == 2 && free_w == 2 && mines == 3 ){
			map[0][1] = map[1][0] = map[1][1] = true;
			mines = 0;
			return true;
		}
		
		return false;
	}
	bool fillRight(){
		int free = h - bottom;
		int free_w = w - right;
		if( free == mines+1 || free_w < 3 )
			return false;
		
		right++;
		for( int i=free-1; i >=0 && mines > 0; i-- ){
			map[w-right][i] = true;
			mines--;
		}
		return true;
	}
	bool fillBottom(){
		int free_h = h - bottom;
		int free = w - right;
		if( free == mines+1 || free_h < 3 )
			return false;
		
		bottom++;
		for( int i=free-1; i >=0 && mines > 0; i-- ){
			map[i][h-bottom] = true;
			mines--;
		}
		return true;
	}
	
	bool fillBoth(){
		int free_h = h - bottom;
		int free_w = w - right;
		if( free_w + free_h <= mines+4 || free_h <= 2 || free_w <= 2 )
			return false;
		
		bottom++; right++;
		int x=0, y=1;
		while( mines > 0 ){
			if( x < free_w-2 ){
				map[w-right-x][h-bottom] = true;
				x++;
				mines--;
			}
			if( y < free_h-2 ){
				map[w-right][h-bottom-y] = true;
				y++;
				mines--;
			}
		}
		return true;
	}
	
	bool reduceSwitching(){
		reset();
		while( mines > 0 ){
			if( right > bottom ){
				if( !fillBottom() )
					if( !fillRight() )
						if( !fillBoth() )
							if( !fill2x2() )
								return false;
			}
			else{
				if( !fillRight() )
					if( !fillBottom() )
						if( !fillBoth() )
							if( !fill2x2() )
								return false;
			}
		}
		
		//All mines placed
		return true;
	}
	bool reduceBottom(){
		reset();
		while( mines > 0 ){
			if( !fillBottom() )
				if( !fillRight() )
					if( !fillBoth() )
						if( !fill2x2() )
							return false;
		}
		
		//All mines placed
		return true;
	}
	bool reduceRight(){
		reset();
		while( mines > 0 ){
			if( !fillRight() )
				if( !fillBottom() )
					if( !fillBoth() )
						if( !fill2x2() )
							return false;
		}
		
		//All mines placed
		return true;
	}
	bool reduce(){
		if( !reduceSwitching() )
			if( !reduceBottom() )
				if( !reduceRight() )
					return false;
		return true;
	}
	
	bool allMines(){
		for( int iy=0; iy<h; iy++ )
			for( int ix=0; ix<w; ix++ )
				if( !temp[ix][iy] )
					return false;
		return true;
	}
	void fill( int ix, int iy ){
		if( ix >= w || iy >= h )
			return;
		temp[ix][iy] = true;
		if( iy+1 < h && map[ix][iy+1] )
			return;
		if( ix+1 < w && map[ix+1][iy] )
			return;
		if( iy+1 < h && ix+1 < w && map[ix+1][iy+1] )
			return;
		
		fill( ix+1, iy );
		fill( ix, iy+1 );
		fill( ix+1, iy+1 );
	}
	bool validate(){
		temp = map;
		temp[0][0] = true;
		fill( 0, 0 );
		return allMines();
	}
	
	void result(){
		if( reduce() ){
			if( !validate() )
				cout << "NOOOOOOOOOOOOOOOOOOOOOO" << endl;
			for( int iy=0; iy<h; iy++ ){
				for( int ix=0; ix<w; ix++ )
					if( ix==0 && iy==0 )
						cout << 'c';
					else
						cout << (map[ix][iy] ? "*" : ".");
				cout << endl;
			}
		}
		else{
		//	cout << w << " " << h << " " << trueMines << endl;
			cout << "Impossible" << endl;
		}
	}
};

int main( int, char** ){
	int amount;
	cin >> amount;
	for( int i=1; i<=amount; i++ ){
		cout << "Case #" << i << ":" << endl;
		Mines().result();
	}
	
	return 0;
}