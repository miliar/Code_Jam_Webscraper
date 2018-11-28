
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



void CQualifi_ADlg::OnBnClickedSolve()
{
	// TODO: Add your control notification handler code here
	int iTestCase;
	FILE* f;
	FILE* fw;

//	fopen_s(&f, "C:\CodeJam\2015\input\A-small-attempt0.in", "r");
	fopen_s(&f, "a.txt", "r");
	fopen_s(&fw, "result.txt", "w");

	fscanf_s(f, "%d", &iTestCase);

	for(int i = 0; i < iTestCase; i++)
	{
		int iLevelCnt;
		fscanf_s(f, "%d", &iLevelCnt);
		
		char acLevels[10000];
		 


		fgets( acLevels, iLevelCnt + 3,  f);

		int iNeededMen  = 0;
		int iStandMen = 0;
		int iLevel =0;

		for(int j = 1; j < iLevelCnt+2; j++)
		{
			CString str;
			int iMen;
			char cMen;
			cMen = acLevels[j];

			iMen = atoi(&cMen);	

			int iNeeded = iLevel - iStandMen;

			iStandMen += iMen;
			
			if(iNeeded > 0)
			{
				iNeededMen += iNeeded;
				iStandMen += iNeeded;
			}
			iLevel++;
		}
		fprintf(fw, "Case #%d: %d",i+1,iNeededMen);  
		
		if(i <iTestCase -1)
			fprintf(fw, "\n");
	}
	fclose(f);
	fclose(fw);

}
