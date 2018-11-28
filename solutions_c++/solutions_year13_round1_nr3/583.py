//

#include "stdafx.h"
#include "a0.h"
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// Ψһ��Ӧ�ó������

CWinApp theApp;

using namespace std;


vector<CString> string2Arr(CString str, char cSplit)
{
	vector<CString> strArr;
	int nStart = 0;
	while (true)
	{
		int nPos = str.Find(cSplit, nStart);
		if (nPos < 0)
		{
			strArr.push_back(str.Mid(nStart));
			break;
		}
		strArr.push_back(str.Mid(nStart, nPos-nStart));
		nStart = nPos+1;
	}
	return strArr; 
}

//����nΪ��������, mΪ�������ֵ, strArrTΪ���ֳ˻���Ϣ,�������ֽ���ϲ�ΪsRet;
void GoodLuck(CString& sRet, const vector<CString>& strArrT, int N, int M)
{
	vector<int> nRets; //Ӧ����n��
	int n2Max = 0;
	int n3Max = 0;
	int n5Max = 0;
	int n7Max = 0;
	for (int i=0; i<strArrT.size(); i++)
	{
		long nSub = atoi(strArrT[i]);
		if (nSub == 1)
		{
			continue;
		}
		int n2 = 0;
		int n3 = 0;
		int n5 = 0;
		int n7 = 0;
		//Ҫ��nRet�ֽ�Ϊ�˻�����ʽ
		//������������
		//m���Ϊ8��5
		//����3��5��7Ҫ����
		while (nSub%3==0)
		{
			nSub = nSub/3;
			++n3;
		}

		while (nSub%5==0)
		{
			nSub = nSub/5;
			++n5;
		}

		while (nSub%7==0)
		{
			nSub = nSub/7;
			++n7;
		}

		while (nSub%2==0)
		{
			nSub = nSub/2;
			++n2;
		}

		if (n2>n2Max)
		{
			n2Max = n2;
		}
		if (n3>n3Max)
		{
			n3Max = n3;
		}
		if (n5>n5Max)
		{
			n5Max = n5;
		}
		if (n7>n7Max)
		{
			n7Max = n7;
		}
	}
	for (int i=0; i<n7Max; i++)
	{
		sRet+="7";
	}

	for (int i=0; i<n5Max; i++)
	{
		sRet+="5";
	}

	for (int i=0; i<n3Max; i++)
	{
		sRet+="3";
	}

	int nLeft = N - sRet.GetLength(); //ʣ��2��λ��

	while (true)
	{
		if (nLeft<=0)
		{
			break;
		}
		int nt1 = n2Max/nLeft;
		int nt2 = n2Max%nLeft;
		if (nt1>2 || (nt1==2 && nt2>0))
		{
			sRet+="8";
			n2Max -= 3;
			nLeft--;
			continue;
		}
		else if (nt1>1 || (nt1==1 && nt2>0))
		{
			sRet+="4";
			n2Max -= 2;
			nLeft--;
			continue;
		}
		else
		{
			sRet+="2";
			n2Max--;
			nLeft--;
		}
	} 
}


int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	HMODULE hModule = ::GetModuleHandle(NULL);

	if (hModule != NULL)
	{
		// ��ʼ�� MFC ����ʧ��ʱ��ʾ����
		if (!AfxWinInit(hModule, NULL, ::GetCommandLine(), 0))
		{
			// TODO: ���Ĵ�������Է���������Ҫ
			_tprintf(_T("����: MFC ��ʼ��ʧ��\n"));
			nRetCode = 1;
		}
		else
		{
			// TODO: �ڴ˴�ΪӦ�ó������Ϊ��д���롣

			CStdioFile file;
			BOOL bOpen = file.Open("C:\\input", CFile::modeRead);
			vector<CString> strArr;
			if (bOpen)
			{
				CString strT;
				while (file.ReadString(strT))
				{
					strArr.push_back(strT);
				}
				file.Close();
			}

			if (bOpen)
			{
				int nSize = atoi(strArr[0]);

				//������Ϣ
				int R = 0;
				int N = 0;
				int M = 0;
				int K = 0;
				vector<CString> strArrT = string2Arr(strArr[1], ' ');
				if (strArrT.size() == 4)
				{
					R = atoi(strArrT[0]);
					N = atoi(strArrT[1]);
					M = atoi(strArrT[2]);
					K = atoi(strArrT[3]);
				}
				//����ֵ
				vector<CString> strRArr;
				strRArr.push_back("Case #1:");
				//��ÿ�ε���Ϣ
				for (size_t i=2; i<R+2; ++i)
				{
					//�������K��������
					vector<CString> strArrT = string2Arr(strArr[i], ' ');

					CString sRet;
					GoodLuck(sRet, strArrT, N, M);
					strRArr.push_back(sRet);
				}

				CStdioFile fileT;
				bOpen = fileT.Open("C:\\output", CFile::modeWrite|CFile::modeCreate);
				if (bOpen)
				{
					for (int i = 0; i < strRArr.size(); i++)
					{
						fileT.WriteString(strRArr[i]+"\n");
					}
					fileT.Close();
				}
			}

		}
	}
	else
	{
		// TODO: ���Ĵ�������Է���������Ҫ
		_tprintf(_T("����: GetModuleHandle ʧ��\n"));
		nRetCode = 1;
	}

	return nRetCode;
}

