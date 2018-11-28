#define _AFXDLL
#define _WIN32_WINNT _WIN32_WINNT_MAXVER
#include <afxwin.h>		// MFC core and standard components

#include <iostream>
using namespace std;

void open_file(CString esFile, CStringList& lOut);
void process_case(CString esCase, CStdioFile& erFileOut, int case_num);

int main()
{
	CStringList lOut;
	open_file("c:\\input.txt", lOut);
	CStdioFile oFileOut("c:\\output.txt", CFile::modeReadWrite|CFile::shareDenyNone|CFile::modeCreate);
	int i=0;
	POSITION pos = lOut.GetHeadPosition();
	while(pos)
	{
		i++;
		process_case(lOut.GetNext(pos), oFileOut, i);
	}
	oFileOut.Close();
	return 0;
}

void open_file(CString esFile, CStringList& lOut)
{
	CStdioFile oInputFile(esFile, CFile::modeRead|CFile::shareDenyNone);
	CString sLine;
	oInputFile.ReadString(sLine);
	int iNumCases = atoi(sLine);
	while(oInputFile.ReadString(sLine))
	{
		lOut.AddTail(sLine);
	}
	oInputFile.Close();
}

void process_case(CString esCase, CStdioFile& erFileOut, int case_num)
{
	int iPos = esCase.Find(" ");
	double r = atof(esCase.Left(iPos));
	double t = atof(esCase.Right(esCase.GetLength()-iPos-1));

	double a = 2.0;
	double b = 2.0 * r - 1.0;
	double c = -t;
	double delta = b*b-4*a*c;
	double n1 = (-b-sqrt(delta))/(2.0*a);
	double n2 = (-b+sqrt(delta))/(2.0*a);
	double max_n = n1 > n2 ? n1 : n2;
	int n = (int) max_n;
	
	do
	{
		double a1 = 2.0 * r + 1;
		double an = a1 + (n - 1.0) * 4.0;
		double sn = (a1 + an) * n / 2.0;
		if(sn>t) n--;
		else break;
	}
	while(true);
	
	CString sOut;
	sOut.Format("Case #%d: %d\n", case_num, n);
	erFileOut.WriteString(sOut);
}
