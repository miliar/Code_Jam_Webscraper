// ti1Dlg.cpp : ʵ���ļ�
//

#include "stdafx.h"
#include "ti1.h"
#include "ti1Dlg.h"
#include <vector>

using namespace std;

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// ����Ӧ�ó��򡰹��ڡ��˵���� CAboutDlg �Ի���

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// �Ի�������
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV ֧��

// ʵ��
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


// Cti1Dlg �Ի���




Cti1Dlg::Cti1Dlg(CWnd* pParent /*=NULL*/)
	: CDialog(Cti1Dlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void Cti1Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(Cti1Dlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(IDOK, &Cti1Dlg::OnBnClickedOk)
END_MESSAGE_MAP()


// Cti1Dlg ��Ϣ�������

BOOL Cti1Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// ��������...���˵�����ӵ�ϵͳ�˵��С�

	// IDM_ABOUTBOX ������ϵͳ���Χ�ڡ�
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// ���ô˶Ի����ͼ�ꡣ��Ӧ�ó��������ڲ��ǶԻ���ʱ����ܽ��Զ�
	//  ִ�д˲���
	SetIcon(m_hIcon, TRUE);			// ���ô�ͼ��
	SetIcon(m_hIcon, FALSE);		// ����Сͼ��

	// TODO: �ڴ���Ӷ���ĳ�ʼ������

	return TRUE;  // ���ǽ��������õ��ؼ������򷵻� TRUE
}

void Cti1Dlg::OnSysCommand(UINT nID, LPARAM lParam)
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

// �����Ի��������С����ť������Ҫ����Ĵ���
//  �����Ƹ�ͼ�ꡣ����ʹ���ĵ�/��ͼģ�͵� MFC Ӧ�ó���
//  �⽫�ɿ���Զ���ɡ�

void Cti1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // ���ڻ��Ƶ��豸������

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// ʹͼ���ڹ��������о���
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// ����ͼ��
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

//���û��϶���С������ʱϵͳ���ô˺���ȡ�ù����ʾ��
//
HCURSOR Cti1Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



bool CalTi2(const vector<vector<int>>& nArr)
{
	//�ȿ�����
	vector<vector<int>> nArrT = nArr;
	for (int i = 0; i < nArr.size(); i++)
	{
		int nMax = 0;
		for (int j = 0; j < nArr[i].size(); j++)
		{
			if (nMax < nArr[i][j])
				nMax = nArr[i][j];
		}

		for (int j = 0; j < nArr[i].size(); j++)
		{
			if (nMax == nArr[i][j])
				nArrT[i][j] = 0;
		}
	}

	for (int j = 0; j < nArr[0].size(); j++)
	{
		int nMax = 0;
		for (int i = 0; i < nArr.size(); i++)
		{
			if (nMax < nArr[i][j])
				nMax = nArr[i][j];
		}

		for (int i = 0; i < nArr.size(); i++)
		{
			if (nMax == nArr[i][j])
				nArrT[i][j] = 0;
		}
	}

	for (int i = 0; i < nArrT.size(); i++)
	{
		for (int j = 0; j < nArrT[i].size(); j++)
		{
			if (nArrT[i][j]!=0)
			{
				return false;
			}
		}
	}
	return true;
}



vector<CString> string2Arr(CString str, char cSplit)
{
	vector<CString> strArr;
	int nStart = 0;
	while (true)
	{
		int nPos = str.Find(cSplit, nStart);
		if (nPos < 0)
		{
			strArr.push_back(str.Mid(nStart));
			break;
		}
		strArr.push_back(str.Mid(nStart, nPos-nStart));
		nStart = nPos+1;
	}
	return strArr; 
}


void Cti1Dlg::OnBnClickedOk()
{
	// TODO: �ڴ���ӿؼ�֪ͨ����������

	if (1)
	{
		CStdioFile file;
		BOOL bOpen = file.Open("C:\\input2", CFile::modeRead);
		vector<CString> strArr;
		if (bOpen)
		{
			CString strT;
			while (file.ReadString(strT))
			{
				strArr.push_back(strT);
			}
			file.Close();
		}

		if (bOpen)
		{
			int nSize = atoi(strArr[0]);
			vector<CString> strRArr;
			int nPos = 1;
			for (int i = 0; i < nSize; i++)
			{
				vector<CString> strArrT = string2Arr(strArr[nPos++], ' ');
				if (strArrT.size()!=2)
				{
					AfxMessageBox("error!!");
					return;
				}
				int nHang = atoi(strArrT[0]);
				int nLie = atoi(strArrT[1]);
				vector<vector<int>> nArr(nHang);
				for (int j = 0; j < nHang; j++)
				{
					vector<CString> strArrT = string2Arr(strArr[nPos++], ' ');
					if (strArrT.size()!=nLie)
					{
						AfxMessageBox("error!!!!!");
					}
					vector<int> nArrT(nLie);
					for (int k = 0; k < nLie; k++)
					{
						nArrT[k] = atoi(strArrT[k]);
					}
					nArr[j] = nArrT;
				}
				bool bR = CalTi2(nArr);
				
				CString strIndex;
				strIndex.Format("Case #%d: ", i+1);
				if (bR)
				{
					strIndex += "YES";
				}
				else
				{
					strIndex += "NO";
				}
				strRArr.push_back(strIndex);
			}

			CStdioFile fileT;
			bOpen = fileT.Open("C:\\output2", CFile::modeWrite|CFile::modeCreate);
			if (bOpen)
			{
				for (int i = 0; i < strRArr.size(); i++)
				{
					fileT.WriteString(strRArr[i]+"\n");
				}
				fileT.Close();
			}
		}
	}

}
