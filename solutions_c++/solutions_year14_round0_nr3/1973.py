#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>

using std::cout;
using std::cin;
using std::string;
using std::stringstream;

typedef unsigned long long line_t;
struct PointT {
	int x;
	int y;
	PointT(int _x, int _y) : x(_x), y(_y) {}
};

class CanvasT {
public:
	CanvasT(int row, int col)
		: mRow(row),
		mCol(col)
	{
		mCells.resize(row);
		for ( int i=0; i<row; i++ ) mCells[i] = 0;
	}
	
	int open3x3(const PointT& pos, std::vector<PointT>& new_area) {
		if ( open1x1(pos.x-1, pos.y-1) )
			new_area.push_back(PointT(pos.x-1, pos.y-1));
		if ( open1x1(pos.x, pos.y-1) )
			new_area.push_back(PointT(pos.x, pos.y-1));
		if ( open1x1(pos.x+1, pos.y-1) )
			new_area.push_back(PointT(pos.x+1, pos.y-1));
		
		if ( open1x1(pos.x-1, pos.y) )
			new_area.push_back(PointT(pos.x-1, pos.y));
		if ( open1x1(pos.x+1, pos.y) )
			new_area.push_back(PointT(pos.x+1, pos.y));
		
		if ( open1x1(pos.x-1, pos.y+1) )
			new_area.push_back(PointT(pos.x-1, pos.y+1));
		if ( open1x1(pos.x, pos.y+1) )
			new_area.push_back(PointT(pos.x, pos.y+1));
		if ( open1x1(pos.x+1, pos.y+1) )
			new_area.push_back(PointT(pos.x+1, pos.y+1));
		return remain();
	}
	
	bool open1x1(int x, int y) {
		line_t mask;
		if ( x>=0 && x<mCol && y>=0 && y<mRow ) {
			mask = (line_t)1 << x;
			if ( 0==(mCells[y] & mask) ) {
				mCells[y] |= mask;
				return true;
			}
		}
		return false;
	}
	
	int remain() const {
		int remain = 0;
		for ( int k=0; k<mRow; k++ ) {
			line_t temp = mCells[k];
			for ( int j=0; j<mCol; j++ ) {
				if ( !(temp & 0x01) ) remain++;
				temp >>= 1;
			}
		}
		return remain;
	}
	
	void click(std::vector<PointT>& click, int mine) {
		std::vector<PointT> new_area;
		open1x1(click[0].x, click[0].y);
		if ( remain()==mine ) return;
		
		for ( int i=0; i<click.size(); i++ ) {
			open3x3(click[i], new_area);
		}
	}
	
	void show(std::ostream& os, int x, int y) const {
		for ( int k=0; k<mRow; k++ ) {
			line_t temp = mCells[k];
			for ( int j=0; j<mCol; j++ ) {
				if ( k==y && j==x ) {
					os << "c";
				}
				else if ( temp & 0x01 ) {
					os << ".";
				}
				else {
					os << "*";
				}
				temp >>= 1;
			}
			os << "\n";
		}
	}
	
private:
	int mRow;
	int mCol;
	std::vector<line_t> mCells;
};

bool solve(int row, int col, int mine, std::vector<PointT>& click) {
	CanvasT canvas(row, col);
	std::vector<PointT> new_area;
	canvas.open1x1(click[0].x, click[0].y);
	int remain = canvas.remain();
	if ( remain==mine ) return true;
	
	for ( int i=0; i<click.size()-1; i++ ) {
		new_area.clear();
		canvas.open3x3(click[i], new_area);
	}
	
	new_area.clear();
	remain = canvas.open3x3(click.back(), new_area);
	if ( remain==mine ) {
		return true;
	}
	else if ( remain<mine ) {
		return false;
	}
	else {
		for ( int k=0; k<new_area.size(); k++ ) {
			click.push_back(new_area[k]);
			if ( solve(row, col, mine, click) ) return true;
			click.pop_back();
		}
		return false;
	}
}

// エントリポイント
int main(int argc, char* argv[])
{
	std::ofstream ofs("mine.txt");
	
	string buf;
	int time(0), row(0), col(0), mine(0), k, j;
	bool solved;
	cin >> time;
	cin.ignore(1024, '\n');
	
	for ( int t=1; t<=time; t++ ) {
		
		// 1ライン入力
		std::getline(cin, buf);
		stringstream ss(buf);
		ss >> row >> col >> mine;
		if ( ss.fail() ) return 0;
		
		std::vector<PointT> click;
		solved = false;
		for ( k=0; k<row; k++ ) {
			for ( j=0; j<col; j++ ) {
				click.clear();
				click.push_back(PointT(j, k));
				if ( solve(row, col, mine, click) ) {
					solved = true;
					break;
				}
			}
			if ( solved ) break;
		}
		
		ofs << "Case #" << t << ":\n";
		if ( solved ) {
			CanvasT canvas(row, col);
			canvas.click(click, mine);
			canvas.show(ofs, click[0].x, click[0].y);
		}
		else {
			ofs << "Impossible\n";
		}
	}
	
	return 0;
}



