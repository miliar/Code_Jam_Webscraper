#include <iostream>
#include <fstream>
#include <memory.h>
using namespace std;
// use: ./A input.txt >> output.txt

ifstream in;
int n;
char map[100][100];
int check[100][100];
int r,c;

#define VALIDPOS(x,y) ((x)>=0 && (x)<c && (y)>=0 && (y)<r)
#define UP '^'
#define DOWN 'v'
#define LEFT '<'
#define RIGHT '>'
#define NONE '.'

struct point {
	int x,y;
};

char getmap(int x, int y) {
	return map[y][x];
}

point getgoodpoint(int px, int py, int dx, int dy) {
	px +=dx;
	py += dy;
	while (VALIDPOS(px, py)) {
		if (getmap(px, py) != NONE)
			break;

		px += dx;
		py += dy;
	}

	point p;
	p.x = px;
	p.y = py;
	return p;
}

bool scan(int px, int py, int dx, int dy) {
	px +=dx;
	py += dy;
	while (VALIDPOS(px, py)) {
		if (getmap(px, py) != NONE)
			break;

		px += dx;
		py += dy;
	}

	return (VALIDPOS(px, py));
}

void process(int idx) {
	cout << "Case #" << idx << ": ";

	// clear
	memset(map, 0, sizeof(map));
	memset(check, 0, sizeof(check));

	// load
	//int r,c;	<- global
	int x,y;
	in >> r >> c;
	for (y=0; y<r; y++) {
		for (x=0; x<c; x++) {
			in >> map[y][x];
		}
	}

	// check impossible & calculate
	int res=0;
	for (y=0; y<r; y++) {
		for (x=0; x<c; x++) {
			if (getmap(x, y) != NONE && 
				!scan(x, y, 1, 0) &&
				!scan(x, y, -1, 0) &&
				!scan(x, y, 0, 1) &&
				!scan(x, y, 0, -1)) {
				cout << "IMPOSSIBLE" << endl;
				return;
			} else if (getmap(x, y) != NONE) {
				// check current 
				// if that goes wrong & unchecked then plus 1
				// and just check it
				point p;
				if (getmap(x, y) == LEFT)
					p = getgoodpoint(x, y, -1, 0);
				else if (getmap(x, y) == RIGHT)
					p = getgoodpoint(x, y, 1, 0);
				else if (getmap(x, y) == UP)
					p = getgoodpoint(x, y, 0, -1);
				else if (getmap(x, y) == DOWN)
					p = getgoodpoint(x, y, 0, 1);

				//cout << p.x << "," << p.y << endl;

				if (!VALIDPOS(p.x, p.y) && !check[p.y][p.x])
					res++;
				check[y][x] = 1;
			}
		}
	}
	

	cout << res << endl;
}

int main(int argc, char **argv) {
	if (argc == 1) {
		cout << "please enter input.txt argv\n";
		return -1;
	}

	in.open(argv[1]);

	in >> n;

	for (int i=0; i<n; i++) {
		process(i+1);
	}

	in.close();

	return 0;
}
