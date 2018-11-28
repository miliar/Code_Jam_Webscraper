// codeJamB.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"

#include<vector>
using namespace std;

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
        int n, m;
        fscanf_s(fpIn, "%d %d\n", &n, &m);

        std::vector<int> arrayMaxTate;
        arrayMaxTate.resize(m, 0);
        std::vector<int> arrayMaxYoko;
        arrayMaxYoko.resize(n, 0);
        std::vector<std::vector<int> > arrayA;
        arrayA.resize(n);
        for (int iN = 0; iN < n; ++iN) {
            arrayA[iN].resize(m);
            for (int iM = 0; iM < m; ++iM) {
                int d;
                fscanf_s(fpIn, "%d", &d);
                arrayA[iN][iM] = d;
                //fscanf_s(fpIn, " ");

                arrayMaxTate[iM] = std::max(arrayMaxTate[iM], arrayA[iN][iM]);
                arrayMaxYoko[iN] = std::max(arrayMaxYoko[iN], arrayA[iN][iM]);
            }
            //fscanf(fpIn, "%n");
        }


        bool result = true;

        for (int iN = 0; iN < n; ++iN) {
            for (int iM = 0; iM < m; ++iM) {
                if (arrayA[iN][iM] < arrayMaxTate[iM]
                    && arrayA[iN][iM] < arrayMaxYoko[iN]) {
                    result = false;
                    break;
                }
            }
            if (!result) {
                break;
            }
        }

        //FIX_ME
        if (result) {
            fprintf_s(fpOut, "Case #%d: YES\n", iTest+1);
        } else {
            fprintf_s(fpOut, "Case #%d: NO\n", iTest+1);
        }
    }


    fclose(fpIn);
    fclose(fpOut);

	return 0;
}

