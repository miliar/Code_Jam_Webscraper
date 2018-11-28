#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <math.h>

using namespace std;

void main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int k, n, m, count = 0;
	
	cin >> k;

	int arr[5] = {1, 4, 9, 121, 484};

	for(int i = 0; i < k; i++)
	{
		cin >> n >> m;
		count = 0;
		
		for(int i = 0; i < 5; i++)
		{
			if(arr[i] >= n && arr[i] <= m)
				count++;
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}


	//int K, N, M;
	//bool IsVer, IsHor, IsNot;

	//IsNot = IsVer = IsHor = false;

	//cin >> K;

	//int** arr;

	//for(int k = 0; k < K; k++)
	//{
	//	IsNot = IsVer = IsHor = false;

	//	cin >> N >> M;

	//	arr = new int*[N];
	//
	//for(int i = 0; i < N; i++)
	//{
	//	arr[i] = new int[M];
	//}

	//	for(int i = 0; i < N; i++)
	//	{
	//		for(int j = 0; j < M; j++)
	//		{
	//			cin >> arr[i][j];
	//		}
	//	}
	//	for(int i = 0; i < N; i++)
	//	{
	//		for(int j = 0; j < M; j++)
	//		{
	//			IsVer = IsHor = false;

	//			if(arr[i][j] == 1)
	//			{
	//				for(int y = 0; y < N; y++)
	//				{
	//					if(arr[y][j] != 1)
	//					{
	//						IsVer = true;
	//					}
	//				}
	//				for(int y = 0; y < M; y++)
	//				{
	//					if(arr[i][y] != 1)
	//					{
	//						IsHor = true;
	//					}
	//				}
	//				if(IsVer && IsHor)
	//				{
	//					IsNot = true;
	//				}
	//			}
	//		}
	//	}
	//	if(IsNot)
	//		cout << "Case #" << k + 1 << ": No" << endl;
	//	else
	//		cout << "Case #" << k + 1 << ": Yes" << endl;

	//}
}