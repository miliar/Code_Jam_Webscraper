
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

