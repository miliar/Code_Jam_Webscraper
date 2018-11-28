
// MFCApplication1Dlg.cpp : 구현 파일
//

#include "stdafx.h"
#include "MFCApplication1.h"
#include "MFCApplication1Dlg.h"
#include "afxdialogex.h"
#include <iostream>
#include <cstdlib>
#include <string>
#include <regex>
#include "md5.h"

#pragma warning(disable:4996)
using namespace std;

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialogEx
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

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CMFCApplication1Dlg 대화 상자



CMFCApplication1Dlg::CMFCApplication1Dlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CMFCApplication1Dlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CMFCApplication1Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CMFCApplication1Dlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDOK, &CMFCApplication1Dlg::OnBnClickedOk)
	ON_BN_CLICKED(IDC_BUTTON2, &CMFCApplication1Dlg::OnBnClickedButton2)
	ON_BN_CLICKED(IDC_BUTTON1, &CMFCApplication1Dlg::OnBnClickedButton1)
	ON_BN_CLICKED(IDC_BUTTON3, &CMFCApplication1Dlg::OnBnClickedButton3)
END_MESSAGE_MAP()


// CMFCApplication1Dlg 메시지 처리기

BOOL CMFCApplication1Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

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

void CMFCApplication1Dlg::OnSysCommand(UINT nID, LPARAM lParam)
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

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다. 문서/뷰 모델을 사용하는 MFC 응용 프로그램의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CMFCApplication1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트입니다.

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
		CDialogEx::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
HCURSOR CMFCApplication1Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CMFCApplication1Dlg::OnBnClickedOk()
{
	CDialogEx::OnOK();
}

//////////////////////////////////////////////////////////////////////////
// Running Code
int card[16];
int result_count = 0;
CString _first_cards[4];
CString _second_cards[4];
CStringArray _srData;
CList<CString,CString&> _saved;
CList<CString,CString&> _saved_copy;
CList<CString,CString&> _re;


void CMFCApplication1Dlg::OnBnClickedButton2()
{
	int T=0;
	int answer=0;
	int N=0;

	FILE *fp_out=fopen("output.txt","w");
	FILE *fp_in=fopen("A-small-attempt0.in","r");

	_ftscanf(fp_in, _T("%d"), &T);
	TCHAR data[9999];
	// save
	for (int i=1; i <= T; ++i)
	{
		// set data
		int first_answer = 0;
		_ftscanf(fp_in, _T("%d\n"), &first_answer);
		for (int j=0; j < 4; ++j)
		{
			_fgetts(data, 99, fp_in);
			_first_cards[j] = data;
			_first_cards[j].Trim();
			//D0(L"AAA %s", _first_cards[j]);
		}
		
		int second_answer = 0;
		_ftscanf(fp_in, _T("%d\n"), &second_answer);
		for (int j=0; j < 4; ++j)
		{
			_fgetts(data, 99, fp_in);
			_second_cards[j] = data;
			_second_cards[j].Trim();
			//D0(L"BBB %s", _second_cards[j]);
		}
		
		// compute
		CString strAnswer;
		CString strToken;
		int cnt = 0;
		CString strFound;
		while (AfxExtractSubString(strToken, _first_cards[first_answer-1], cnt++, L' '))
		{
			CString strToken2;
			int cnt2 = 0;
			while (AfxExtractSubString(strToken2, _second_cards[second_answer-1], cnt2++, L' '))
			{
				if (strToken == strToken2)
				{
					if (strFound.IsEmpty())
						strFound = strToken;
					else
						strFound = _T("Bad magician!");
				}
			}
		}

		if (strFound.IsEmpty())
			strFound = _T("Volunteer cheated!");

		// result
		//D0(_T("Case #%d: %s"), i, strFound);
		_ftprintf(fp_out, _T("Case #%d: %s\n"), i, strFound);
	}
	
	fclose(fp_out);
	fclose(fp_in);
}


void CMFCApplication1Dlg::OnBnClickedButton1()
{
	::ShellExecute(NULL, _T("open"), _T("notepad"), _T("output.txt"), NULL, SW_SHOW);
}


void CMFCApplication1Dlg::OnBnClickedButton3()
{
	CString strAnswer;
	CString strToken;
	int cnt = 0;
	while (AfxExtractSubString(strToken, L"5 6 7 8", cnt++, ' '))
	{
		D0(L"AAA %s", strToken);
	}
}
