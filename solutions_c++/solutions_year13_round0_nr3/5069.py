// codeJamC.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <stdio.h>
#include <stdlib.h>

#include <vector>
using namespace std;

struct BigInt {
    BigInt() {}
    BigInt(const char* p)
    {
        std::vector<char> temp;
        while (p) {
            if (*p < '0' || '9' < *p) {
                _ASSERTE(*p == 0 || *p == ' ' || *p == '\n');
                break;
            }
            temp.push_back(*p - '0');
            ++p;
        }
        arrayNumber.resize(temp.size());
        for (size_t i = 0; i < temp.size(); ++i) {
            arrayNumber[i] = temp[temp.size() - 1 - i];
        }
    }
    BigInt Square() const
    {
        _ASSERTE(!arrayNumber.empty());

        BigInt result;
        size_t nCount = arrayNumber.size();
        size_t nCount2 = 2 * nCount - 1;
        int iKuriagari = 0;
        for (size_t i = 0; i < nCount2; ++i) {
            int iSum = iKuriagari;
            for (size_t j = 0; j <= i && j < nCount; ++j) {
                if (i-j < nCount) {
                    iSum += arrayNumber[j] * arrayNumber[i-j];
                }
            }
            result.arrayNumber.push_back(iSum % 10);
            iKuriagari = iSum / 10;
        }
        while (iKuriagari) {
            result.arrayNumber.push_back(iKuriagari % 10);
            iKuriagari = iKuriagari / 10;
        }
        return result;
    }

    bool IsKaibun() const
    {
        size_t nSize = arrayNumber.size();
        for (size_t i = 0; i < nSize / 2; ++i) {
            if (arrayNumber[i] != arrayNumber[nSize - i - 1]) {
                return false;
            }
        }
        return true;
    }

    void Increment(bool& bCheckKetaAgari)
    {
        bCheckKetaAgari = false;
        for (size_t i = 0; i < arrayNumber.size(); ++i) {
            if (arrayNumber[i] != 9) {
                ++arrayNumber[i];
                return;
            }
            arrayNumber[i] = 0;
        }
        bCheckKetaAgari = true;
        arrayNumber.push_back(1);
    }
    void IncrementTane(bool& bCheckKetaAgari)
    {
        Increment(bCheckKetaAgari);
        if (arrayNumber[0] == 0) {
            bool bTemp;
            Increment(bTemp);
        }
    }

    std::vector<char> arrayNumber;  //0-9までの値しか使用しない
};

bool operator<(const BigInt& a, const BigInt& b)
{
    if (a.arrayNumber.size() != b.arrayNumber.size()) {
        return a.arrayNumber.size() < b.arrayNumber.size();
    }

    for (size_t i = 0; i < a.arrayNumber.size(); ++i) {
        int iCheck = (int)a.arrayNumber.size() - 1 - (int)i;
        if (a.arrayNumber[iCheck] != b.arrayNumber[iCheck]) {
            return a.arrayNumber[iCheck] < b.arrayNumber[iCheck];
        }
    }
    return false;
}

int Calc(const BigInt& bigIntFront, const BigInt& bigIntBack)
{
    int i = 0;
    return 0;
}

BigInt CreateKaibun1(const BigInt& tane)
{
    BigInt result = tane;
    for (size_t i = 0; i < tane.arrayNumber.size() - 1; ++i) {
        result.arrayNumber.push_back(tane.arrayNumber[tane.arrayNumber.size() - 2 - i]);
    }
    return result;
}

BigInt CreateKaibun2(const BigInt& tane)
{
    BigInt result = tane;
    for (size_t i = 0; i < tane.arrayNumber.size(); ++i) {
        result.arrayNumber.push_back(tane.arrayNumber[tane.arrayNumber.size() - 1 - i]);
    }
    return result;
}

std::vector<BigInt> GetSquareKaibunArray(size_t iMaxSquareKeta)
{
    BigInt tane1;   //奇数桁用
    tane1.arrayNumber.push_back(1);
    BigInt tane2;   //偶数桁用
    tane2.arrayNumber.push_back(1);

    std::vector<BigInt> result;
    while (true) {
        //先に奇数桁用の処理
        while (true) {
            BigInt kaibun = CreateKaibun1(tane1);
            BigInt kaibun2 = kaibun.Square();
            if (kaibun2.arrayNumber.size() > iMaxSquareKeta) {
                return result;
            }
            if (kaibun2.IsKaibun()) {
                result.push_back(kaibun2);
            }

            bool bCheckKetaAgari = false;
            tane1.IncrementTane(bCheckKetaAgari);
            if (bCheckKetaAgari) {
                break;
            }
        }

        //後に偶数桁用の処理
        while (true) {
            BigInt kaibun = CreateKaibun2(tane2);
            BigInt kaibun2 = kaibun.Square();
            if (kaibun2.arrayNumber.size() > iMaxSquareKeta) {
                return result;
            }
            if (kaibun2.IsKaibun()) {
                result.push_back(kaibun2);
            }

            bool bCheckKetaAgari = false;
            tane2.IncrementTane(bCheckKetaAgari);
            if (bCheckKetaAgari) {
                break;
            }
        }
    }

    return result;
}

int main(int argc, char* argv[])
{
#if 0
    BigInt bigIntTest;
    bigIntTest.arrayNumber.push_back(1);
    bigIntTest.arrayNumber.push_back(2);
    bigIntTest.arrayNumber.push_back(3);

    BigInt bigIntTest2 = bigIntTest.Square();
#endif
#if 0
    BigInt bigIntTest;
    bigIntTest.arrayNumber.push_back(1);
    bigIntTest.arrayNumber.push_back(2);
    bigIntTest.arrayNumber.push_back(3);
    bigIntTest.arrayNumber.push_back(2);
    bigIntTest.arrayNumber.push_back(1);

    bool bIsKaibun = bigIntTest.IsKaibun();
#endif
#if 0
    BigInt test1, test2;
    test1.arrayNumber.push_back(1);
    test1.arrayNumber.push_back(2);

    test2.arrayNumber.push_back(1);
    test2.arrayNumber.push_back(2);
    bool bTest;

    bTest = test1 < test2;
    bTest = test2 < test1;

    test1.arrayNumber.push_back(1);
    test2.arrayNumber.push_back(2);

    bTest = test2 < test1;

    test1.arrayNumber.push_back(1);
    test2.arrayNumber.push_back(1);

    bTest = test2 < test1;

#endif

    std::vector<BigInt> arraySquareKaibun = GetSquareKaibunArray(4);

    if (argc != 3) {
        return 1;
    }

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

    char sz[1024];
    fgets(sz, 1024, fpIn);
    int nTestCount = atoi(sz);
    for (int i = 0; i < nTestCount; ++i) {
        fgets(sz, 1024, fpIn);
        BigInt front(sz);

        char* pc = sz;
        while('0' <= *pc && *pc <= '9'){++pc;}
        while(*pc < '0' || '9' < *pc){++pc;}
        BigInt back(pc);

        int iCount = 0;
        for (size_t j = 0; j < arraySquareKaibun.size(); ++j) {
            if (arraySquareKaibun[j] < front) {
                continue;
            }
            if (back < arraySquareKaibun[j]) {
                break;
            }
            ++iCount;
        }

        fprintf_s(fpOut, "Case #%d: %d\n", i+1, iCount);
    }


    fclose(fpIn);
    fclose(fpOut);

	return 0;
}

