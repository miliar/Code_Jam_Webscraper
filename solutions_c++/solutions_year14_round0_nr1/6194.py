#include <iostream>


using namespace std;

typedef long long int int64;


//jamA
int main(void)
{
	int nTestCase, repeat;
	int i, j;

	int board1[4][4], board2[4][4];
	int compdata[17];
	int ch, line1, line2, ansnum, ans;

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){

		// テストケース番号出力
		cout << "Case #" << repeat << ": ";

		// 1回めの指定行読み込み
		cin >> line1;

		// ボード読み込み
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> ch;
				board1[i][j] = ch;
			}
		}

		// 2回めの指定行読み込み
		cin >> line2;

		// ボード読み込み
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> ch;
				board2[i][j] = ch;
			}
		}

		// 調査データを初期化する
		for(i = 0; i < 17; i++){
			compdata[i] = 0;
		}

		// 1回目の指定行に含まれる数をcompdataに登録する
		for(i = 0; i < 4; i++){
			compdata[ board1[line1 - 1][i] ] = 1;
		}

		// 2回目の指定行に含まれる数をcompdataから検索する
		// 含まれている数が1つであれば正解。
		ansnum = 0;
		ans = 0;
		for(i = 0; i < 4; i++){
			if(compdata[ board2[line2 - 1][i] ] == 1){
				ansnum++;
				ans = board2[line2 - 1][i];
			}
		}

		// 当たり判定
		if(ansnum == 0){
			cout << "Volunteer cheated!" << endl;
		}else if(ansnum == 1){
			cout << ans << endl;
		}else{
			cout << "Bad magician!" << endl;
		}

	}

	return 0;
}

