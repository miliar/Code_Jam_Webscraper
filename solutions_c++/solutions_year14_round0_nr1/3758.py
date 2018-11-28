
// MFCApplication1Dlg.cpp : ���� ����
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


// ���� ���α׷� ������ ���Ǵ� CAboutDlg ��ȭ �����Դϴ�.

class CAboutDlg : public CDialogEx
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

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CMFCApplication1Dlg ��ȭ ����



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


// CMFCApplication1Dlg �޽��� ó����

BOOL CMFCApplication1Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

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

// ��ȭ ���ڿ� �ּ�ȭ ���߸� �߰��� ��� �������� �׸�����
//  �Ʒ� �ڵ尡 �ʿ��մϴ�. ����/�� ���� ����ϴ� MFC ���� ���α׷��� ��쿡��
//  �����ӿ�ũ���� �� �۾��� �ڵ����� �����մϴ�.

void CMFCApplication1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // �׸��⸦ ���� ����̽� ���ؽ�Ʈ�Դϴ�.

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
		CDialogEx::OnPaint();
	}
}

// ����ڰ� �ּ�ȭ�� â�� ���� ���ȿ� Ŀ���� ǥ�õǵ��� �ý��ۿ���
//  �� �Լ��� ȣ���մϴ�.
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
