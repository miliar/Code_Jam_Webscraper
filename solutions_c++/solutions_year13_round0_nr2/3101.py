#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

struct min_heights_t {
    int height;
    int x;
    int y;
    min_heights_t(int _h, int _x, int _y) : height(_h),x(_x),y(_y) {}
    bool operator<(const min_heights_t & other ) const {
        return height < other.height;
    }
};

class test_t {
    vector<min_heights_t> heights;
    vector<int> rows_max;
    vector<int> cols_max;
    vector<int> rows;
    vector<int> cols;

    bool allocate(vector<min_heights_t>::const_iterator start, const vector<min_heights_t>::const_iterator end, vector<int> & rows, vector<int> & cols ) {
        if( start == end )
            return true;
        else {
            const min_heights_t one = *start;

            // printf( "\nlooking at %d, %d -> %d\n",one.x,one.y,one.height);

            // already mowed to the right level
            if( rows[one.y] == one.height  && cols[one.x]>=one.height) {
                // printf("  row %d has wanted height %d\n",one.y,one.height);
                return allocate(start+1,end,rows,cols);
            }

            if( rows[one.y] >= one.height && cols[one.x] == one.height) {
                // printf("  col %d has wanted height %d\n",one.x,one.height);
                return allocate(start+1,end,rows,cols);
            }

            // try to mow first row and then col
            if( rows_max[one.y] == one.height ) {
                rows[one.y] = one.height;
                // printf(" Allocating row %d to %d\n",one.y,one.height);
                return(allocate(start+1,end,rows,cols));
            }
            if( cols_max[one.x] == one.height ) {
                // printf(" Allocating col %d to %d\n",one.x,one.height);
                cols[one.x] = one.height;
                return allocate(start+1,end,rows,cols);
            }
            return false;
        }
    }

    public:
    test_t(int height, int width) {
        rows_max.assign(height,0);
        cols_max.assign(width,0);
        rows.assign(height,100);
        cols.assign(height,100);
    }

    void add(int x, int y, int height) {
        rows_max[y] = max(rows_max[y],height);
        cols_max[x] = max(cols_max[x],height);
        heights.push_back(min_heights_t(height,x,y));
    }

    bool process() {
        sort(heights.begin(),heights.end());
        return allocate(heights.begin(),heights.end(),rows,cols);
    }
};

int main(int argc, const char* argv[]) {
  ifstream infile("/Users/mseritan/Downloads/one.in");
  ofstream outfile("/Users/mseritan/Downloads/one.out");
  int tests=0;
  string line;
  getline(infile,line);
  stringstream(line) >> tests;
  printf("tests %d\n",tests);
  for( int t=1;t<=tests;t++) {
    int width, height;
    getline(infile,line);

    stringstream(line) >> height >> width;
    // printf("height %d, width %d\n", height, width);
    test_t test(height,width);
    for( int j=0;j<height;j++) {
        getline(infile,line);
        stringstream ss(line);
        for( int i=0; i<width; i++) {
            string item;
            getline(ss,item,' ');
            int height;
            stringstream(item) >> height;
            test.add(i,j,height);
        }
    }
    outfile << "Case #" << t << ": "<<  (test.process() ? "YES" : "NO") << endl;
  }
  return 0;
}