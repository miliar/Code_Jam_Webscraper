#include <stdio.h>
#include <string.h>
#include <vector>

#define MIN(a,b) ( (a)>(b)?(b):(a) )
#define MAX(a,b) ( (a)<(b)?(b):(a) )

struct sizepair {
	int x;
	int y;
};

std::vector<sizepair> solution;

int R, C, M, empty;

bool solve(int xmin, int ymin, int xmax, int ymax, int ie=0) {
	for(int x=xmin; x<xmax; ++x) {
		for(int y=ymin; y<ymax; ++y) {
			if(x*y+ie > empty) {
				continue;
			} else if(x*y+ie == empty) {
				sizepair sp = { x, y };
				solution.push_back(sp);
				return true;
			} else if(x>xmin) {
				if(solve(2, 1, x, ymax-y, ie+x*y)) {
					sizepair sp = { x, y };
					solution.push_back(sp);
					return true;
				}
			}
		}
	}
	return false;
}

char minefield[50*50];

/*
void test() {
	R = C = 4;
	M = 3;
	empty = R*C - M;
	solve(2, 2, MIN(R,C)+1, MAX(R,C)+1);
	for(int i=0; i<solution.size(); ++i)
		printf("X %d  Y %d\n", solution[i].x, solution[i].y);
}
*/


int main(int argc, char** argv) {
	//test();
	int T;
	scanf("%d%*c", &T);
	for(int i=0; i<T; ++i) {
		printf("Case #%d:\n", i+1);
		scanf("%d %d %d", &R, &C, &M);
		//printf("%d %d %d\n", R, C, M);
		empty = R*C - M;
		if (empty == 1 || R == 1 || C == 1) {
			for(int row=0; row<R; ++row) {
				for(int col=0; col<C; ++col) {
					if(!row && !col)
						putchar('c');
					else if(empty > 0)
						putchar('.');
					else
						putchar('*');
					if(empty > 0)
						--empty;
				}
				printf("\n");
			}
			goto possible;
		}
		/*for(int x=2; x<=MIN(R,C); ++x) {
			for(int y=2; y<=x; ++y) {
				for(int ax=2; ax<=x; ++ax) {
					for(int ay=0; ay<=MAX(R,C)-y; ++ay) {
						if(x*y + ax*ay > empty)
							break;
						if(x*y + ax*ay == empty) {
							bool rotate = C>R;
							int ox = rotate?y:x;
							int oy = rotate?x:y;
							int oax = rotate?ay:ax;
							int oay = rotate?ax:ay;
							for(int row=0; row<R; ++row) {
								for(int col=0; col<C; ++col) {
									if(!row && !col)
										putchar('c');
									else if(row<oy && col<ox)
										putchar('.');
									else if(!rotate && row<oy+oay && col<oax)
										putchar('.');
									else if(rotate && row<oay && col<ox+oax)
										putchar('.');
									else
										putchar('*');
								}
								putchar('\n');
							}
							goto possible;
						}
					}
				}
			}
		}*/
		if(solve(2, 2, MIN(R,C)+1, MAX(R,C)+1)) {
			memset(minefield, '*', 50*50);
			bool rotate = C>R;
			int offset = 0;
			while(!solution.empty()) {
				sizepair sp = solution.back();
				solution.pop_back();
				for(int row=(rotate?0:offset); row<(rotate?sp.x:sp.y+offset); ++row) {
					for(int col=(rotate?offset:0); col<(rotate?sp.y+offset:sp.x); ++col) {
						minefield[row*50+col] = '.';
					}
				}
				offset += sp.y;
			}
			minefield[0] = 'c';
			for(int row=0; row<R; ++row) {
				for(int col=0; col<C; ++col) {
					putchar(minefield[row*50+col]);
				}
				putchar('\n');
			}
		} else {
			printf("Impossible\n");
		}
possible:
		continue;
	}
	return 0;
}