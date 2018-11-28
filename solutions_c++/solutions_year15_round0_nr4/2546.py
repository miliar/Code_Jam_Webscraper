
// Qualifi_ADlg.cpp : implementation file
//

#include "stdafx.h"
#include "Qualifi_A.h"
#include "Qualifi_ADlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CAboutDlg dialog used for App About

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// Dialog Data
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CQualifi_ADlg dialog



CQualifi_ADlg::CQualifi_ADlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CQualifi_ADlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CQualifi_ADlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CQualifi_ADlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(ID_SOLVE, &CQualifi_ADlg::OnBnClickedSolve)
END_MESSAGE_MAP()


// CQualifi_ADlg message handlers

BOOL CQualifi_ADlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
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

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CQualifi_ADlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CQualifi_ADlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CQualifi_ADlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

int ReturnBig(int R, int C)
{
	if(R > C)
	{
		return R;
	}
	else return C;

}

int ReturnLittle(int R, int C)
{
	if(R > C)
	{
		return C;
	}
	else return R;

}


void CQualifi_ADlg::OnBnClickedSolve()
{
	// TODO: Add your control notification handler code here
	int iTestCase;
	FILE* f;
	FILE* fw;

//	fopen_s(&f, "C:\CodeJam\2015\input\A-small-attempt0.in", "r");
	fopen_s(&f, "d.txt", "r");
	fopen_s(&fw, "result.txt", "w");

	fscanf_s(f, "%d", &iTestCase);

	for(int i = 0; i < iTestCase; i++)
	{
		bool bPossible = true;
		int X,R,C;
		fscanf_s(f, "%d", &X);
		fscanf_s(f, "%d", &R);
		fscanf_s(f, "%d", &C);

		int gop = R*C;

		if(X >= 7)
		{
										bPossible = false;
		}
		else
		{
			if(X == 4)
			{ 
				int iLittle = ReturnLittle(R,C);
				if(iLittle <= 2)
				{
										bPossible = false;
				}
			}
			else if(X == 5)
			{ 
				int iLittle = ReturnLittle(R,C);
				if(iLittle <= 3)
				{
										bPossible = false;
				}
			}
			else if(X == 6)
			{ 
				int iLittle = ReturnLittle(R,C);
				if(iLittle <= 4)
				{
										bPossible = false;
				}
			}


		if(gop >= X)
		{
			if(gop % X == 0)
			{ 
				int iLittle = ReturnLittle(R,C);
				int iBig = ReturnBig(R,C);

				if(X > iLittle)
				{
					if(((X + 1) - (iLittle+1)) > iLittle)
					{ 
							bPossible = false;
					}else
					{
						if( ((X + 1)  - iLittle) > iBig)
						{
										bPossible = false;
						}
					}
				}
			}
			else
			{
				bPossible = false;
			}
		}
		else
		{
			bPossible = false;
		
		}
		}
		if(bPossible)
			fprintf(fw, "Case #%d: GABRIEL", i + 1);
		else
			fprintf(fw, "Case #%d: RICHARD", i + 1);

		if(i <iTestCase - 1)
		{
			fprintf(fw,"\n");
		}
	
	}
	fclose(f);
	fclose(fw);

}
