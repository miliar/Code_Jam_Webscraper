#include <iostream>


using namespace std;

typedef long long int int64;


//jamB
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	int field[100][100]; // 最大で100x100
	int N, M;
	int arNmax[100], arMmax[100];
	bool result;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){
		// テストケース番号出力
		cout << "Case #" << repeat << ": ";

		// 行と列の数を取得する
		cin >> N;
		cin >> M;

		// それぞれの行列の値を取得する
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				cin >> field[i][j];
			}
		}

		// 行と列のそれぞれの最大値を取得する
		// まずは初期化
		for(i = 0; i < 100; i++){
			arNmax[i] = 0;
			arMmax[i] = 0;
		}

		// すべての値を比較して、行ごと、列ごとの最大値を求める
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				if(field[i][j] > arNmax[i]){
					arNmax[i] = field[i][j];
				}
				if(field[i][j] > arMmax[j]){
					arMmax[j] = field[i][j];
				}
			}
		}

		// すべてのフィールドの値に対して、行方向か列方向のいずれかの最大値よりも、値が高いか同じならばOK.
		// その場合、ちゃんと芝刈り機で刈れます。
		// いずれかの最大値よりも低い場合、行方向に刈っても列方向に刈っても、その高さまでは刈り取れません。
		result = true;
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				if(field[i][j] < arNmax[i] && field[i][j] < arMmax[j]){
					result = false;
				}
			}
		}

		// 答えを出力
		if(result){
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}

	return 0;
}

