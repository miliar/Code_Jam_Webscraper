// b.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include "math.h"

__int64 Yama(int sumXY)
{
    int n = sumXY / 2 + 1;
    return 2 * n * n - n;
}

__int64 LineCount(int sumXY)
{
    int n = sumXY / 2 + 1;
    return 4 * n - 3;
}

double sum_nCm(int in, int y)
{
    int n = in - y;
    __int64 sum = 0;
    __int64 a = 1;
    for (int i = 0; i < n; ++i) {
        sum += a;
        a = a * (in - i) / (i + 1);
    }
    return sum / pow((double)2, (double)in);
}

int main(int argc, char* argv[])
{
    FILE* fpIn = NULL;
    fopen_s(&fpIn, argv[1], "r");
    if (!fpIn) {
        return 2;
    }
    FILE* fpOut = NULL;
    fopen_s(&fpOut, argv[2], "w");
    if (!fpOut) {
        return 3;
    }

    int nTest;
    fscanf_s(fpIn, "%d", &nTest);
    for (int iTest = 0; iTest < nTest; ++iTest) {
        __int64 N;
        int x, y;
        fscanf_s(fpIn, "%I64d %d %d\n", &N, &x, &y);

        int sumXY;
        if (x >= 0) {
            sumXY = x + y;
        } else {
            sumXY = -x + y;
        }
        double result = 0.0;
        __int64 smallYama = Yama(sumXY - 2);
        __int64 largeYama = Yama(sumXY);
        if (N <= smallYama) {
            result = 0.0;
        } else if (largeYama <= N) {
            result = 1.0;
        } else if (x == 0) {
            result = 0.0;
        } else {
            __int64 lineCount = LineCount(sumXY);
            int in = (int)(N - smallYama);
            if (in <= y) {
                result = 0.0;
            } else if (in > sumXY + y) {
                result = 1.0;
            } else {
                result = sum_nCm(in, y);
            }
        }

        fprintf_s(fpOut, "Case #%d: %f\n", iTest+1, result);
    }


    fclose(fpIn);
    fclose(fpOut);

	return 0;
}
