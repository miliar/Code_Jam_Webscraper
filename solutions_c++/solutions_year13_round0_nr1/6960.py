#include "StdAfx.h"
#include "GoogleCodeJamSolver.h"


CGoogleCodeJamSolver::CGoogleCodeJamSolver(void)
{
}


CGoogleCodeJamSolver::~CGoogleCodeJamSolver(void)
{
}

void CGoogleCodeJamSolver::Run()
{
	CStdioFile oFile("c:\\temp.txt", CFile::modeReadWrite|CFile::shareDenyNone);
	CStdioFile oFileOut("c:\\temp_out.txt", CFile::modeCreate|CFile::modeReadWrite|CFile::shareDenyNone);
	CString sLine;
	oFile.ReadString(sLine);
	int iNumCases = atoi(sLine);
	for(int iCase=1;iCase<=iNumCases;iCase++)
	{
		char a[4][4];
		for(int i=0;i<4;i++)
		{
			oFile.ReadString(sLine);
			a[i][0] = sLine.Mid(0,1).GetBuffer(0)[0];
			a[i][1] = sLine.Mid(1,1).GetBuffer(0)[0];
			a[i][2] = sLine.Mid(2,1).GetBuffer(0)[0];
			a[i][3] = sLine.Mid(3,1).GetBuffer(0)[0];
		}

		// verifico se algum usuario ganhou
		bool bGanhou = true;
		for(int i=0;i<4;i++)
		{
			char primeiro = a[i][0];
			if(primeiro == 'T') primeiro=a[i][1];

			bGanhou = false;
			if(primeiro=='X' || primeiro =='O')
			{
				bGanhou = true;
				for(int j=1;j<4;j++)
				{
					if(a[i][j] != primeiro && a[i][j] != 'T')
					{
						bGanhou = false;
						break;
					}
				}
			}

			if(bGanhou)
			{
				CString sTemp;
				sTemp.Format("Case #%d: %c won\n", iCase, primeiro);
				oFileOut.WriteString(sTemp);
				break;
			}
		}

		if(bGanhou)
		{
			oFile.ReadString(sLine);
			continue;
		}

		for(int j=0;j<4;j++)
		{
			char primeiro = a[0][j];
			if(primeiro == 'T') primeiro=a[1][j];
			
			bGanhou = false;
			if(primeiro =='X' || primeiro =='O')
			{
				bGanhou = true;
				for(int i=1;i<4;i++)
				{
					if(a[i][j] != primeiro && a[i][j] != 'T')
					{
						bGanhou = false;
						break;
					}
				}
			}

			if(bGanhou)
			{
				CString sTemp;
				sTemp.Format("Case #%d: %c won\n", iCase, primeiro);
				oFileOut.WriteString(sTemp);
				break;
			}
		}

		if(bGanhou)
		{
			oFile.ReadString(sLine);
			continue;
		}

		// verifico as diagonais
		bGanhou = false;
		char primeiro = a[0][0];
		if(primeiro == 'T') primeiro = a[1][1];
		if(primeiro != '.')
		{
			bGanhou = true;
			for(int i=1;i<4;i++)
			{
				if(a[i][i] != primeiro && a[i][i] != 'T')
				{
					bGanhou = false;
					break;
				}
			}
		}

		if(bGanhou)
		{
			CString sTemp;
			sTemp.Format("Case #%d: %c won\n", iCase, primeiro);
			oFileOut.WriteString(sTemp);
			oFile.ReadString(sLine);
			continue;
		}

		bGanhou = false;
		primeiro = a[0][3];
		if(primeiro == 'T') primeiro = a[1][2];
		if(primeiro != '.')
		{
			bGanhou = true;
			for(int i=1;i<4;i++)
			{
				if(a[i][3-i] != primeiro && a[i][3-i] != 'T')
				{
					bGanhou = false;
					break;
				}
			}
		}

		if(bGanhou)
		{
			CString sTemp;
			sTemp.Format("Case #%d: %c won\n", iCase, primeiro);
			oFileOut.WriteString(sTemp);
			oFile.ReadString(sLine);
			continue;
		}

		// ninguem ganhou
		bool bNotCompleted = false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='.')
				{
					bNotCompleted = true;
					CString sTemp;
					sTemp.Format("Case #%d: Game has not completed\n", iCase);
					oFileOut.WriteString(sTemp);
					break;
				}
			}

			if(bNotCompleted) 
			{
				break;
			}
		}

		if(!bNotCompleted)
		{
			CString sTemp;
			sTemp.Format("Case #%d: Draw\n", iCase);
			oFileOut.WriteString(sTemp);
		}
		
		oFile.ReadString(sLine);
	}
}