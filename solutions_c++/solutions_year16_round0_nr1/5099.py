
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
			for(int iter = 0 ; iter < lSize ; iter ++)
			{

				if(pFile[iter] == '\r' || pFile[iter] == '\n' 
					|| pFile[iter] == ' ')
				{
					vtProblem.push_back(_ttoi(strText));
					strText = _T("");
				}else
				{
					strText.AppendFormat(_T("%c"),pFile[iter]);
				}
				
			}
			vtProblem.push_back(_ttoi(strText));
		}
	}

	CFile f;
	f.Open(_T("d:\\codejam\\SheepCount.txt"),CFile::modeCreate | CFile::modeWrite);
	for(int iter = 1 ;iter <= vtProblem[0] ; iter ++)
	{
		CString strResult = CountingSheep(vtProblem[iter]);
		CString strText;
		strText.Format(_T("Case #%d: %s"),iter ,strResult);
		f.Write(CT2A(strText ),strText .GetLength());
		f.Write("\r\n",2);

	}
	f.Close();
	
}

