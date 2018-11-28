
// SP_CodeJam2016Dlg.cpp : 구현 파일
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


// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// 대화 상자 데이터입니다.
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

// 구현입니다.
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


// CSP_CodeJam2016Dlg 대화 상자




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


// CSP_CodeJam2016Dlg 메시지 처리기

BOOL CSP_CodeJam2016Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
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

	// 이 대화 상자의 아이콘을 설정합니다. 응용 프로그램의 주 창이 대화 상자가 아닐 경우에는
	//  프레임워크가 이 작업을 자동으로 수행합니다.
	SetIcon(m_hIcon, TRUE);			// 큰 아이콘을 설정합니다.
	SetIcon(m_hIcon, FALSE);		// 작은 아이콘을 설정합니다.

	// TODO: 여기에 추가 초기화 작업을 추가합니다.

	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
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

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다. 문서/뷰 모델을 사용하는 MFC 응용 프로그램의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CSP_CodeJam2016Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 클라이언트 사각형에서 아이콘을 가운데에 맞춥니다.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 아이콘을 그립니다.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
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
