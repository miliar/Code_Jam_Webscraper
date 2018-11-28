#include <iostream>

using namespace std;

int T;
char f[4][4];

bool check(int x, int y, int dx, int dy, char c) {
    int cnt = 0;
	
    while ((x >= 0) && (x < 4) &&
           (y >= 0) && (y < 4)) {

        cnt++;
		//cout << f[y][x] << " " << x << " " << y<< endl;;
        if ((f[y][x] !='T') && (f[y][x] != c))
            return 0;
		x += dx;
        y += dy;
    }
	
    if (cnt == 4)
        return 1;
    return 0;
}

signed int d[4][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};

int main() {
    cin >> T;
    char temp = 0;
    for (int i = 1; i <= T; i++) {
            int used = 0;
        for (int y = 0; y < 4; y++) {
                cin >> f[y];
        }
        for (int y = 0; y < 4; y++) {
            for (int x = 0; x < 4; x++) {
                //cout << f[y][x];
                if (f[y][x] != '.')
                    used++;
            }
           // cout << endl;
        }
		
		//cout << "ba: " << check(0, 3, d[3][0], d[3][1], 'O')<< endl;
		//return 0;
		
        for (int y = 0; y < 4; y++) {
            for (int x = 0; x < 4; x++)
                for (int z = 0; z < 4; z++) {
                    if (check(x, y, d[z][0], d[z][1], 'X')) {
                        cout << "Case #" << i << ": " << "X won";
                        goto blub;
                    }
					//cout << x << " " << y << " " << z << endl;
                    if (check(x, y, d[z][0], d[z][1], 'O')) {
                        cout << "Case #" << i << ": " << "O won";
                        goto blub;
                    }
                }
		}
		if (used == 16) {
            cout << "Case #" << i << ": " << "Draw";
            goto blub;
        }
        else {      
            cout << "Case #" << i << ": " << "Game has not completed";
            goto blub;
		}
    blub:;
	
		
    cout << endl ;
    }
}
