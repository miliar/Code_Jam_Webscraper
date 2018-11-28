#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

int main() {
	int T, tc;

	cin >> T;

	for(tc=1;tc<=T;tc++) {
		int N, M;

		cin >> N >> M;

		int lawn[N][M];

		fi(N) {
			fj(M) {
				cin >> lawn[i][j];
			}
		}

		bool ok = true;

		fi(N) {
			fj(M) {
				int h = lawn[i][j];
				bool col = true;
				bool row = true;

				fk(N) {
					if(lawn[k][j] > h) {
						row = false;
						break;
					}
				}

				fk(M) {
					if(lawn[i][k] > h) {
						col = false;
						break;
					}
				}

				if(!col && !row) {
					ok = false;
					break;
				}
			}

			if(!ok) {
				break;
			}
		}

		if(ok) {
			cout << "Case #" << tc << ": YES" << endl;
		} else {
			cout << "Case #" << tc << ": NO" << endl;
		}
	}
}
