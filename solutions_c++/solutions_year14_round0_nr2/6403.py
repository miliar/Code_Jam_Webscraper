#include <iostream>
#include <vector>
#include <cstdio>

int main()
{
	freopen("B-large.in","r",stdin) ;
	freopen("output_large.out","w",stdout) ;


	int get ;		// データ総数

	double cost ;		// クッキーファーム一個あたりのコスト
						// 問題文中の C にあたる

	double power ;		// クッキーファーム一個あたりの生産量
						// 問題文中の F にあたる

	double target ;		// 目指すクッキーの数
						// 問題文中の X にあたる

	scanf("%d",&get) ;

	for( int i = 0 ; i < get ; i ++ )
	{
		scanf("%lf",&cost) ;
		scanf("%lf",&power) ;
		scanf("%lf",&target) ;

		double nowper ;
		double nowtime ;

		nowper = 2.0 ;
		nowtime = 0.0 ;
		double lastper = nowper ;
		double lasttime = nowtime ;

		double total ;				// 現在の最短の時間
		total = target / nowper ;

		// このnumっつーのが一つずつ増やしていくファーム数
		for( int num = 1 ; ; num ++ )
		{
			double tmptime ;		// ファーム数numに至るまでの時間を格納する
			tmptime = cost / lastper ;
	//		time.push_back( tmptime ) ;
			nowtime = tmptime + lasttime ;

			// これでファーム数numに至るまでの時間は格納された

			double tmppow ;			// ファーム数numの総生産力
			tmppow = lastper + power ;
	//		per.push_back( tmppow ) ;
			nowper = tmppow ;

			// これでファーム数numの総生産力は格納された

			// 次はファーム数numの状態から target 枚のクッキーを生産するのにかかる時間を求める
			double tmp_totime ;
			tmp_totime = target / nowper ;

			if( total <= nowtime + tmp_totime )
			{
				break ;
			}
			else
			{
				total = nowtime + tmp_totime ;
			}

			lastper = nowper ;
			lasttime = nowtime ;
		}

		printf("Case #%d: %.7lf\n", i+1, total ) ;
	}

	return 0 ;
}