// 1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k,T,R, C, W;
	cin >> T;
	int index = 1;
	while (T--)
	{
		cin >> R >> C >> W;
		cout << "Case #" << index << ": ";
		int **arr = new int*[R];
		for (i = 0; i < R; i++)

		{
			arr[i] = new int[C];
		}
		
		//small R= 1;
		
		if (W == C)
		{
			cout << R-1+W << endl;
		}
		else
		{
			if (W == 1) {
				cout << C*R << endl;
			}
			else
			{
				int result = 0;
				
				while (C / W >=1){
					if (C == W)
						break;
					result++;
					C -= W;
				}


				result *= R;
				result += W;
				cout << result << endl;
			}
		}
		index++;
	}
	return 0;
}

