// ti1Dlg.cpp : ʵ���ļ�
//

#include "stdafx.h"
#include "ti1.h"
#include "ti1Dlg.h"
#include <vector>
#include <map>

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



struct isPointSmaller
{	// functor for operator<
	bool operator()(const CPoint& p1, const CPoint& p2) const
	{
		if (p1.x==p2.x)
		{
			return p1.y < p2.y;
		}
		return p1.x < p2.x;
	}
};


map<CPoint, vector<CString>, isPointSmaller> mapStrTable;

//ʣ�µ�����ȥ���nLengthλ���ص��ַ�����
const vector<CString>& getStrArrUnderN(int nMax, int nLength)
{
	CPoint p(nMax, nLength);
	map<CPoint, vector<CString>, isPointSmaller>::iterator iter = mapStrTable.find(p);
	if (iter != mapStrTable.end())
	{
		return iter->second;
	}
	if (nMax<=0 || nLength<=0)
	{
		mapStrTable[p].clear();
		return mapStrTable[p];
	}
	if (nLength==1)
	{
		if (nMax>=4)
		{
			mapStrTable[p].push_back("2");
		}
		mapStrTable[p].push_back("1");
		return mapStrTable[p];
	}
	const vector<CString>& strArr0 = getStrArrUnderN(nMax, nLength-1);
	const vector<CString>& strArr1 = getStrArrUnderN(nMax-1, nLength-1);
	const vector<CString>& strArr2 = getStrArrUnderN(nMax-4, nLength-1);
	vector<CString> strArrNew;
	strArrNew.reserve(strArr0.size()+strArr1.size()+strArr2.size());
	for (int i = 0; i < strArr0.size(); i++)
	{
		strArrNew.push_back(strArr0[i]+"0");
	}
	for (int i = 0; i < strArr2.size(); i++)
	{
		strArrNew.push_back(strArr2[i]+"2");
	}
	for (int i = 0; i < strArr1.size(); i++)
	{
		strArrNew.push_back(strArr1[i]+"1");
	}
	mapStrTable[p] = strArrNew;
	return mapStrTable[p];
}

//ʣ�µ�����ȥ���nLengthλ
long getNumUnderN(int nMax, int nLength)
{
	return getStrArrUnderN(nMax, nLength).size();
}

long getHuiWenNumAt(int nLength)
{
	if (nLength==1)
	{
		return 3;
	}
	if (nLength%2==0)
	{
		return getNumUnderN(4, nLength/2);
	}
	else
	{
		return getNumUnderN(4, (nLength-1)/2)*2+getNumUnderN(2, (nLength-1)/2);
	}
}

vector<CString> getHuiWenStrAt(int nLength)
{
	vector<CString> strArr;
	if (nLength==1)
	{
		strArr.push_back("1");
		strArr.push_back("2");
		strArr.push_back("3");
		return strArr;
	}
	if (nLength%2==0)
	{
		strArr = getStrArrUnderN(4, nLength/2);
		for (int i = 0; i < strArr.size(); i++)
		{
			CString strT = strArr[i];
			strT.MakeReverse();
			strArr[i]+=strT;
		}
		return strArr;
	}
	else
	{
		vector<CString> strArrT = getStrArrUnderN(4, (nLength-1)/2);
		vector<CString> strArrT2 = getStrArrUnderN(2, (nLength-1)/2);
		strArr.reserve(strArrT.size()*2+strArrT2.size());
		for (int i = 0; i < strArrT.size(); i++)
		{
			CString strT = strArrT[i];
			strT.MakeReverse();
			strArr.push_back(strArrT[i]+"0"+strT);
			strArr.push_back(strArrT[i]+"1"+strT);
		}

		for (int i = 0; i < strArrT2.size(); i++)
		{
			CString strT = strArrT2[i];
			strT.MakeReverse();
			strArr.push_back(strArrT2[i]+"2"+strT);
		}
	}
	return strArr;
}

CString sqrStr(CString str)
{
	if (str == "1")
	{
		return "1";
	}
	else if (str == "2")
	{
		return "4";
	}
	else if (str == "3")
	{
		return "9";
	}

	CString strR = str+str;
	strR.Delete(0);
	for (int i = 0; i < strR.GetLength(); i++)
	{
		strR.SetAt(i, '0');
	}

	for (int i = 0; i < str.GetLength(); i++)
	{
		if (str[i] == '0')
		{
			continue;
		}
		int nBei = (str[i]-'0');
		for (int j = 0; j < str.GetLength(); j++)
		{
			strR.SetAt(i+j, strR[i+j]+(str[j]-'0')*nBei);
		}
	}

	return strR;
}


int isShorter(const CString& s1, const CString& s2)
{
	if (s1==s2)
	{
		return 0;
	}
	int n1 = s1.GetLength();
	int n2 = s2.GetLength();
	if (n1!=n2)
	{
		if (n1<n2)
		{
			return -1;
		}
		return 1;
	}
	if (s1<s2)
	{
		return -1;
	}
	return 1;
}


int CalTi3(CString s1, CString s2)
{
	int nWei1 = (s1.GetLength()+1)/2;
	int nWei2 = (s2.GetLength()+1)/2;
	if (nWei1 == nWei2)
	{
		vector<CString> strArr =getHuiWenStrAt(nWei1);
		int nR = 0;
		for (int i = 0; i < strArr.size(); i++)
		{
			strArr[i] = sqrStr(strArr[i]);
			if (isShorter(s1,strArr[i])!=1 && isShorter(s2,strArr[i])!=-1)
			{
				nR++;
			}
		}
		return nR;
	}

	int nR = 0;
	vector<CString> strArr =getHuiWenStrAt(nWei1);
	for (int i = 0; i < strArr.size(); i++)
	{
		strArr[i] = sqrStr(strArr[i]);
		if (isShorter(s1,strArr[i])!=1)
		{
			nR++;
		}
	}
	strArr.clear();
	strArr = getHuiWenStrAt(nWei2);
	for (int i = 0; i < strArr.size(); i++)
	{
		strArr[i] = sqrStr(strArr[i]);
		if (isShorter(s2,strArr[i])!=-1)
		{
			nR++;
		}
	}

	for (int i = nWei1+1; i < nWei2; i++)
	{
		nR+= getHuiWenNumAt(i);
	}
	return nR;
}

void Cti1Dlg::OnBnClickedOk()
{
	// TODO: �ڴ���ӿؼ�֪ͨ����������

	if (1)
	{
		CStdioFile file;
		BOOL bOpen = file.Open("C:\\input3", CFile::modeRead);
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
			for (int i = 0; i < nSize; i++)
			{
				vector<CString> strArrT = string2Arr(strArr[i+1], ' ');
				if (strArrT.size()!=2)
				{
					AfxMessageBox("error!!");
					return;
				}
				int nS = CalTi3(strArrT[0], strArrT[1]);
				CString strIndex;
				strIndex.Format("Case #%d: %d", i+1, nS);
				strRArr.push_back(strIndex);
			}

			CStdioFile fileT;
			bOpen = fileT.Open("C:\\output3", CFile::modeWrite|CFile::modeCreate);
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
