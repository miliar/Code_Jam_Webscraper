
// SP_CodeJam2016Dlg.cpp : ���� ����
//

#include "stdafx.h"
#include "SP_CodeJam2016.h"
#include "SP_CodeJam2016Dlg.h"
#include <math.h>
#include <vector>
using namespace std;





#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// ���� ���α׷� ������ ���Ǵ� CAboutDlg ��ȭ �����Դϴ�.

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// ��ȭ ���� �������Դϴ�.
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV �����Դϴ�.

// �����Դϴ�.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
END_MESSAGE_MAP()


// CSP_CodeJam2016Dlg ��ȭ ����




CSP_CodeJam2016Dlg::CSP_CodeJam2016Dlg(CWnd* pParent /*=NULL*/)
	: CDialog(CSP_CodeJam2016Dlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CSP_CodeJam2016Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CSP_CodeJam2016Dlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(COUNT_SHEEP, &CSP_CodeJam2016Dlg::OnBnClickedSheep)
	ON_BN_CLICKED(IDOK, &CSP_CodeJam2016Dlg::OnBnClickedOk)
	ON_BN_CLICKED(ID_FRACTILES, &CSP_CodeJam2016Dlg::OnBnClickedFractiles)
	ON_BN_CLICKED(ID_REVENGE, &CSP_CodeJam2016Dlg::OnBnClickedRevenge)
	ON_BN_CLICKED(ID_COIN_JAM, &CSP_CodeJam2016Dlg::OnBnClickedCoinJam)
	ON_BN_CLICKED(ID_MAKE_PRIME, &CSP_CodeJam2016Dlg::OnBnClickedMakePrime)
END_MESSAGE_MAP()


// CSP_CodeJam2016Dlg �޽��� ó����

BOOL CSP_CodeJam2016Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// �ý��� �޴��� "����..." �޴� �׸��� �߰��մϴ�.

	// IDM_ABOUTBOX�� �ý��� ��� ������ �־�� �մϴ�.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// �� ��ȭ ������ �������� �����մϴ�. ���� ���α׷��� �� â�� ��ȭ ���ڰ� �ƴ� ��쿡��
	//  �����ӿ�ũ�� �� �۾��� �ڵ����� �����մϴ�.
	SetIcon(m_hIcon, TRUE);			// ū �������� �����մϴ�.
	SetIcon(m_hIcon, FALSE);		// ���� �������� �����մϴ�.

	// TODO: ���⿡ �߰� �ʱ�ȭ �۾��� �߰��մϴ�.

	return TRUE;  // ��Ŀ���� ��Ʈ�ѿ� �������� ������ TRUE�� ��ȯ�մϴ�.
}

void CSP_CodeJam2016Dlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// ��ȭ ���ڿ� �ּ�ȭ ���߸� �߰��� ��� �������� �׸�����
//  �Ʒ� �ڵ尡 �ʿ��մϴ�. ����/�� ���� ����ϴ� MFC ���� ���α׷��� ��쿡��
//  �����ӿ�ũ���� �� �۾��� �ڵ����� �����մϴ�.

void CSP_CodeJam2016Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // �׸��⸦ ���� ����̽� ���ؽ�Ʈ

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Ŭ���̾�Ʈ �簢������ �������� ����� ����ϴ�.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// �������� �׸��ϴ�.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// ����ڰ� �ּ�ȭ�� â�� ���� ���ȿ� Ŀ���� ǥ�õǵ��� �ý��ۿ���
//  �� �Լ��� ȣ���մϴ�.
HCURSOR CSP_CodeJam2016Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

CString CountingSheep(int nStartNumber)
{
	long lSheep = 0;
	int nIndex = 1;

	if(nStartNumber == 0)
	{
		return _T("INSOMNIA");
	}
	while(1)
	{
		
		int nCurrentNumber = nStartNumber * nIndex;
		int nResultNumber = nCurrentNumber;
		nIndex++; ;
		while(1)
		{
			lSheep = lSheep| 1<< ( nCurrentNumber %10);
			nCurrentNumber/=10;
			if(nCurrentNumber == 0 )
			{
				break;
			}	
		}
		if(lSheep == 1023)
		{
			CString strResult;
			strResult.Format(_T("%d"),nResultNumber);
			return strResult;
		}

	}
}
void CSP_CodeJam2016Dlg::OnBnClickedSheep()
{
	CFileDialog dlg(TRUE);
	vector<int> vtProblem;
	int nCount = 0;
	int* pProblem = NULL;
	if(dlg.DoModal() == IDOK)
	{
		CFile f;
		if(f.Open(dlg.GetPathName(),CFile::modeNoTruncate | CFile::modeRead))
		{
			long lSize = f.GetLength();
			char* pFile = new char[lSize+1];
			f.Read(pFile,lSize);
			f.Close();
			CString strText;
			int nIndex = 0;
			for(int iter = 0 ; iter < lSize ; iter ++)
			{

				
				if(pFile[iter] == '\r' || pFile[iter] == '\n' 
					|| pFile[iter] == ' ')
				{
					if(pProblem ==0)
					{
						nCount = _ttoi(strText);
						pProblem = new int[nCount];
					}else
					{
						pProblem[nIndex] = _ttoi(strText);
						nIndex++;
					}
					
					strText = _T("");
				}else
				{
					strText.AppendFormat(_T("%c"),pFile[iter]);
				}
				
			}
		}
	}

	CFile f;
	f.Open(_T("d:\\codejam\\SheepCount.txt"),CFile::modeCreate | CFile::modeWrite);
	for(int iter = 0 ;iter < nCount ; iter ++)
	{
		CString strResult = CountingSheep(pProblem[iter]);
		CString strText;
		strText.Format(_T("Case #%d: %s"),iter +1,strResult);
		f.Write(CT2A(strText ),strText .GetLength());
		f.Write("\r\n",2);

	}
	f.Close();
	
}

CString MakeTile(CString strPatern,CString strText,int nCount)
{
	CString strResult;
	CString strGold;
	

	for(int iter = 0  ; iter < nCount ; iter ++)
	{
		strGold.Append(_T("G"));
	}

	for(int nIndex = 0 ; nIndex <strText.GetLength() ; nIndex ++)
	{
		BOOL bGolde = strText.Mid(nIndex,1) == _T("G");
		if(bGolde )
		{
			strResult.Append(strGold);
		}else
		{
			strResult.Append(strPatern);
		}
		
	}
	return strResult;
}
void CSP_CodeJam2016Dlg::OnBnClickedOk()
{
	
	int K =31 , C = 7;
	CFile f;
	CString strFileName;
	for(int K = 2; K < 31 ; K++)
	{
		for(int C = 2 ; C < 8 ;C++)
		{
			strFileName.Format(_T("d:\\codejam\\MakeTile_%d_%d.txt"),K,C);
			f.Open(strFileName,CFile::modeCreate | CFile::modeWrite);
			for(int iter = 0 ; iter < pow((double)2,(double)K) ; iter ++)
			{
				CString strText;
				for(int j= 0 ; j < K ; j++)
				{
					if(iter & (1<<j))
					{
						strText.Append(_T("G"));
					}else
					{
						strText.Append(_T("L"));
					}

				}
				CString strResult = strText;
				for(int j= 1 ; j < C ; j++)
				{
					strResult = MakeTile(strText,strResult,K);
				}

				f.Write(CT2A(strText),strText.GetLength());
				f.Write("  ",2);
				f.Write(CT2A(strResult),strResult.GetLength());
				f.Write("\r\n",2);
			}
			f.Close();
			
		}
	}
	
}

CString Fractiles(int nK,int nC,int nS)
{

	CString strResult;
	int nJump = nK;
	if(nK>nC)
	{
		nJump = nC;
	}
	if((int)(nK*1.0/nC+0.5) > nS)
	{
		return _T("IMPOSSIBLE");
	}
	if(nC >= 2)
	{
		
		for(int iter = nJump ; iter<= nK; iter+=nJump)
		{

			strResult.AppendFormat(_T("%d "),(iter-2)*nK + iter);
		}
		if(nK % nJump)
		{
			strResult.AppendFormat(_T("%d "),(nK-1)*nK);
		}

	}else
	{
		for(int iter = 1 ; iter<= nK; iter+=nJump)
		{
			strResult.AppendFormat(_T("%d "),iter);
		}
	}



	return strResult;
}
void CSP_CodeJam2016Dlg::OnBnClickedFractiles()
{
	CFileDialog dlg(TRUE);
	vector<int> vtProblem;
	int nCount = 0;
	int* pProblem = NULL;
	if(dlg.DoModal() == IDOK)
	{
		CFile f;
		if(f.Open(dlg.GetPathName(),CFile::modeNoTruncate | CFile::modeRead))
		{
			long lSize = f.GetLength();
			char* pFile = new char[lSize+1];
			f.Read(pFile,lSize);
			f.Close();
			CString strText;
			int nIndex = 0;
			for(int iter = 0 ; iter < lSize ; iter ++)
			{

				
				if(pFile[iter] == '\r' || pFile[iter] == '\n' 
					|| pFile[iter] == ' ')
				{
					if(pProblem ==0)
					{
						nCount = _ttoi(strText);
						pProblem = new int[nCount * 3*5];
					}else
					{
						strText.Trim();
						if(!strText.IsEmpty())
						{
							pProblem[nIndex] = _ttoi(strText);
							nIndex++;
						}
						
					}
					
					strText = _T("");
				}else
				{
					strText.AppendFormat(_T("%c"),pFile[iter]);
				}
				
			}
		}
	}

	CFile f;
	f.Open(_T("d:\\codejam\\SheepCount.txt"),CFile::modeCreate | CFile::modeWrite);
	for(int iter = 0 ;iter < nCount ; iter ++)
	{
		CString strResult = Fractiles(pProblem[iter*3],pProblem[iter*3+1],pProblem[iter*3+2]);
		CString strText;
		strText.Format(_T("Case #%d: %s"),iter +1,strResult);
		f.Write(CT2A(strText ),strText .GetLength());
		f.Write("\r\n",2);

	}
	f.Close();
	
	
}
CString Revenge(CString strStack)
{
	int nCount = 0;
	CString strCurrent = strStack.Left(1);
	for(int iter = 1 ; iter< strStack.GetLength() ; iter ++)
	{
		if(strStack.Mid(iter,1).Compare(strCurrent))
		{
			strCurrent = strStack.Mid(iter,1);
			nCount ++;
		}
	}
	if(strCurrent== _T("-"))
	{
		nCount ++;
	}
	CString strResult;
	strResult.Format(_T("%d"),nCount);
	return strResult;
	
}
void CSP_CodeJam2016Dlg::OnBnClickedRevenge()
{
	CFileDialog dlg(TRUE);
	vector<int> vtProblem;
	int nCount = 0;
	int* pProblem = NULL;
	vector<CString> vtPancake;
	if(dlg.DoModal() == IDOK)
	{
		CFile f;
		if(f.Open(dlg.GetPathName(),CFile::modeNoTruncate | CFile::modeRead))
		{ 
			long lSize = f.GetLength();
			char* pFile = new char[lSize+1];
			f.Read(pFile,lSize);
			f.Close();
			CString strText;
			int nIndex = 0;
			for(int iter = 0 ; iter < lSize ; iter ++)
			{

				
				if(pFile[iter] == '\r' || pFile[iter] == '\n' )
				{
					if(nCount ==0)
					{
						nCount = _ttoi(strText);
						
					}else
					{
						if(!strText.IsEmpty())
						{
							vtPancake.push_back(strText);
						}
						
						
					}
					
					strText = _T("");
				}else
				{
					strText.AppendFormat(_T("%c"),pFile[iter]);
				}
				
			}
			if(!strText.IsEmpty())
			{
				vtPancake.push_back(strText);
			}
		}
	}

	CFile f;
	f.Open(_T("d:\\codejam\\Pancake.txt"),CFile::modeCreate | CFile::modeWrite);
	for(int iter = 0 ;iter < nCount ; iter ++)
	{
		CString strResult = Revenge(vtPancake[iter]);
		CString strText;
		strText.Format(_T("Case #%d: %s"),iter +1,strResult);
		f.Write(CT2A(strText ),strText .GetLength());
		f.Write("\r\n",2);

	}
	f.Close();
}
BOOL IsPrime(LONGLONG lValue)
{
	for(LONGLONG iter = 3;  iter < lValue/3;iter ++)
	{
		if(((lValue /iter) *iter) == lValue)
		{
			return FALSE;
		}
	}
	return TRUE;
}
CString CoinJam(int N,int J)
{
	LONGLONG l;
	int nCount = pow((double)2,(double)N-2);
	int nLoop = N-2;
	CString strResult = _T("\r\n");
	LONGLONG lDefault[11];
	int nJCount = 0;
	for(int a=2; a<10; a++)
	{
		lDefault[a] = pow((double)a,(double)N)+1;
	}


	/*while(1)
	{

	}*/
	
	return strResult;
	
}
void CSP_CodeJam2016Dlg::OnBnClickedCoinJam()
{
	CFile f;
	f.Open(_T("d:\\codejam\\coinjam.txt"),CFile::modeCreate | CFile::modeWrite);

		CString strResult = CoinJam(16,50);
		CString strText;
		strText.Format(_T("Case #%d: %s"),1,strResult);
		f.Write(CT2A(strText ),strText .GetLength());
		f.Write("\r\n",2);


	f.Close();
}
vector<LONGLONG> vtPrime;

void CSP_CodeJam2016Dlg::OnBnClickedMakePrime()
{
	LONGLONG l = pow(10.0,5);

	for(LONGLONG iter = 2 ; iter < l ; iter ++)
	{
		BOOL bIsPrime = TRUE;
		for(int nIndex = 0 ; nIndex < vtPrime.size() ; nIndex++)
		{
			if(iter % vtPrime[nIndex] == 0)
			{		
				bIsPrime = FALSE;
				break;
			}

		}
		if(bIsPrime)
		{
			vtPrime.push_back(iter);
		}

	}
}
