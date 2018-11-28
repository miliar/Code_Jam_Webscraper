#include <stdio.h>
#include <atlstr.h>
#include <string.h>

CString Maneuver(CString strSrc)
{
	CString strDst;
	strDst = strSrc.MakeReverse();
	strDst.Replace(_T('+'), _T('T'));
	strDst.Replace(_T('-'), _T('+'));
	strDst.Replace(_T('T'), _T('-'));
	return strDst;
}

int GetCount(CString strPancakes, BOOL bAllHappy)
{
	int nCnt1 = 99999;
	int nCnt2 = 99999;

	BOOL bFlag = FALSE;

	if (strPancakes.GetLength()==1)
	{
		if (bAllHappy)
		{
			if (strPancakes == _T("+"))
				return 0;
			else
				return 1;
		}
		else
		{
			if (strPancakes == _T("-"))
				return 0;
			else
				return 1;
		}
	}
	
	if (bAllHappy)
	{
		if (strPancakes.Right(1)==_T("+"))
		{
			nCnt1 = GetCount(strPancakes.Left(strPancakes.GetLength()-1), TRUE);
			nCnt2 = GetCount(Maneuver(strPancakes.Left(strPancakes.GetLength()-1)), TRUE) + 1;
		}
		else
		{
			nCnt1 = GetCount(strPancakes.Left(strPancakes.GetLength()-1), FALSE) + 1;
			nCnt2 = GetCount(Maneuver(strPancakes.Left(strPancakes.GetLength()-1)), FALSE) + 2;
		}
	}
	else
	{
		if (strPancakes.Right(1)==_T("-"))
		{
			nCnt1 = GetCount(strPancakes.Left(strPancakes.GetLength()-1), FALSE);
			nCnt2 = GetCount(Maneuver(strPancakes.Left(strPancakes.GetLength()-1)), FALSE) + 1;
		}
		else
		{
			nCnt1 = GetCount(strPancakes.Left(strPancakes.GetLength()-1), TRUE) + 1;
			nCnt2 = GetCount(Maneuver(strPancakes.Left(strPancakes.GetLength()-1)), TRUE) + 2;
		}
	}

	/*
	if (bAllHappy)
	{
		if (strPancakes.Right(1)==_T("+"))
		{
			for (int i=strPancakes.GetLength()-2; i>=0; i--)
			{
				if (strPancakes.GetAt(i)==_T('-'))
				{
					nCnt1 = GetCount(Maneuver(strPancakes.Left(i+1)), TRUE) + 1;
					nCnt2 = GetCount(strPancakes.Left(i+1), FALSE) + 1;
					bFlag = TRUE;
					break;
				}
			}
		}
		else
		{
			for (int i=strPancakes.GetLength()-2; i>=0; i--)
			{
				if (strPancakes.GetAt(i)==_T('+'))
				{
					nCnt1 = GetCount(Maneuver(strPancakes.Left(i+1)), FALSE) + 2;
					nCnt2 = GetCount(strPancakes.Left(i+1), TRUE) + 1;
					bFlag = TRUE;
					break;
				}
			}
		}
	}
	else
	{
		if (strPancakes.Right(1)==_T("-"))
		{
			for (int i=strPancakes.GetLength()-2; i>=0; i--)
			{
				if (strPancakes.GetAt(i)==_T('+'))
				{
					nCnt1 = GetCount(Maneuver(strPancakes.Left(i+1)), FALSE) + 1;
					bFlag = TRUE;
					break;
				}
			}
		}
		else
		{
			for (int i=strPancakes.GetLength()-2; i>=0; i--)
			{
				if (strPancakes.GetAt(i)==_T('-'))
				{
					nCnt1 = GetCount(Maneuver(strPancakes.Left(i+1)), TRUE) + 2;
					bFlag = TRUE;
					break;
				}
			}
		}
	}
	*/
	if (nCnt1 < nCnt2)
		return nCnt1;
	else
		return nCnt2;
}

int main()
{
	FILE * in = fopen("B-small-attempt0.in", "r");
	FILE * out = fopen("B-small-attempt0.out", "w");
	char szInp[200] = {0, };
	int T;

	fscanf(in, "%d", &T);

	for (int i=1; i<=T; i++)
	{
		fscanf(in, "%s", szInp);
		CString strPancakes = szInp;

		int nCnt1 = GetCount(strPancakes, TRUE);
		int nCnt2 = GetCount(Maneuver(strPancakes), TRUE) + 1;

		if (nCnt1<nCnt2)
			fprintf(out, "Case #%d: %d\n", i, nCnt1);
		else
			fprintf(out, "Case #%d: %d\n", i, nCnt2);
	}

	return 0;
}