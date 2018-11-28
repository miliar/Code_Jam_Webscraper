#include<cstdio>
#include<bits/stdc++.h>

int pairs[400];

char solv[20];

struct pos {
	int x, y;
	pos operator+(pos& other) {
		pos r = *this;
		r.x += other.x;
		r.y += other.y;
		return r;
	}
	bool operator==(pos& other) {
		return x == other.x && y == other.y;
	}
};

pos kier[4];

void get_sol(int x, int n) {
	for (int i = 0; i < n; ++i) {
		solv[i] = (x&(1<<i))?'\\':'/';
	}
}

pos numtopos(int num, int R, int C) {
	pos x;
	if(num <= C) {
		x.x = num-1;
		x.y = -1;
	} else if (num <= C+R) {
		x.x = C;
		x.y = num-C-1;
	} else if (num <= C+R+C) {
		x.x = C-(num-C-R);
		x.y = R;
	} else {
		x.x = -1;
		x.y = R-(num-C-R-C);
	}
	return x;
}

bool check_p(int a, int b, int R, int C) {
	pos x = numtopos(a,R,C), t = numtopos(b,R,C);
	pos dir;
	if (x.x < 0) dir = kier[1];
	if (x.x >= C) dir = kier[0];
	if (x.y < 0) dir = kier[3];
	if (x.y >= R) dir = kier[2];
	pos next = x + dir;
	do {
		x = next;
		if (solv[x.x+x.y*C] == '/') {
			if (dir == kier[0]) {
				dir = kier[3];
			} else if (dir == kier[1]) {
				dir = kier[2];
			} else if (dir == kier[2]) {
				dir = kier[1];
			} else if (dir == kier[3]) {
				dir = kier[0];
			}
		} else {
			if (dir == kier[0]) {
				dir = kier[2];
			} else if (dir == kier[1]) {
				dir = kier[3];
			} else if (dir == kier[2]) {
				dir = kier[0];
			} else if (dir == kier[3]) {
				dir = kier[1];
			}
		}
		next = x + dir;
	} while (next.x >= 0 && next.x < C && next.y >= 0 && next.y < R);
	return next == t;
}

char str[100];

int main() {
	kier[0].x = -1;
	kier[1].x = 1;
	kier[2].y = -1;
	kier[3].y = 1;
	int T; scanf("%d", &T);
	for (int _ = 0; _ < T; ++_) {
		int R, C; scanf("%d%d", &R, &C);
		for (int i = 0; i < R*2 + C*2; ++i) {
			scanf("%d", pairs+i);
		}
		bool found = 0;
		for (int x = 0; x < (1<<(R*C)); ++x) {
			get_sol(x,R*C);
			bool good = 1;
			for (int i = 0; i < R*2+C*2 && good; i += 2) {
				good &= check_p(pairs[i], pairs[i+1], R, C);
			}
			if (good) {
				printf("Case #%d:\n", _+1);				
				for (int i = 0; i < R; ++i) {
					memcpy(str, solv+i*C, C);
					str[C] = 0;
					printf("%s\n", str);
				}
				found = 1; break;
			}
		}
		if (!found)
			printf("Case #%d: \nIMPOSSIBLE\n", _+1);
	}
	return 0;
}
