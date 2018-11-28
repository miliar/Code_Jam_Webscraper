#include <iostream>
#include <iomanip>

using namespace std;

typedef long long int int64;


//jamA
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	double C, F, X;
	int N, M;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){

		// テストケース番号出力
		cout << "Case #" << repeat << ": ";

		// データ読み込み
		cin >> C >> F >> X;

		// もしX<=Cなら、一回も建てないで継続
		if(X <= C){
			cout << fixed << setprecision(8) << (X / 2) << endl;
			continue;
		}

		// ここなら、1回以上Farmを建てることが前提となる
		// N回Farmを建てたときと、N+1回Farmを建てた時の、どちらが早いかを比較する。
		// N = 0からスタート
		N = 0;
		double total_time = 0;
		double next_farm_time = 0, s = 0, p0, p1;
		double t0 = 0, t1 = 0, a0 = 0, a1 = 0, X0 = 0, X1 = 0;
		while(1){
			M = N + 1;
			a0 = 2 + N * F;
			a1 = 2 + M * F;

			next_farm_time = C / a0;
			s = C / F;
			p1 = a1 * s;

			if(p1 >= X){ // 交点の高さがXを超えたので、a0のときが最短時間となる
				total_time += X / a0;
				cout << fixed << setprecision(8) ; // 小数部の精度指定とする。
				cout << total_time << endl;
				break;
			}
			// 交点の高さがXを超えないので、a1をa0として再検証する
			a1 = a0;
			total_time += C / a0;
			N++;
		}

	}

	return 0;
}

