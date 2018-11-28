// ti1Dlg.cpp : ʵ���ļ�
//

#include "stdafx.h"
#include "ti1.h"
#include "ti1Dlg.h"
#include <vector>
#include <set>
#include <map>
#include <algorithm>
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

bool CalTi4(multiset<int> nKeySet, const map<int,vector<int>>& keyBoxMap, const map<int,vector<int>>& boxHasKey, vector<int>& nRArr)
{
	if (nRArr.size() == boxHasKey.size())
	{
		return true;
	}
	map<int,int> boxKeyMap;
	for (multiset<int>::const_iterator i = nKeySet.begin(); i != nKeySet.end(); i++)
	{
		map<int,vector<int>>::const_iterator a = keyBoxMap.find(*i);
		if (a != keyBoxMap.end())
		{
			for (int j = 0; j < a->second.size(); j++)
			{
				boxKeyMap[a->second[j]] = *i;
			}
		}
	}
	for (int i = 0; i < nRArr.size(); i++)
	{
		boxKeyMap.erase(nRArr[i]);
	}
	for (map<int,int> ::const_iterator itt = boxKeyMap.begin(); itt != boxKeyMap.end(); ++itt)
	{
		multiset<int> nKeySetT = nKeySet;
		multiset<int>::iterator iter = nKeySetT.find(itt->second);
		if (iter == nKeySetT.end())
		{
			continue;
		}
		nRArr.push_back(itt->first);
		nKeySetT.erase(iter);
		map<int,vector<int>>::const_iterator it = boxHasKey.find(itt->first);
		nKeySetT.insert(it->second.begin(), it->second.end());

		//������������һ��Կ�� Ҫ�õ���Ҫ�ĵط�
		if (nKeySetT.find(itt->second) == nKeySetT.end())
		{
			map<int,vector<int>>::const_iterator a = keyBoxMap.find(itt->second);
			if (a != keyBoxMap.end())
			{
				set<int> boxSet(a->second.begin(), a->second.end());
				for (int i = 0; i < nRArr.size(); i++)
				{
					boxSet.erase(nRArr[i]);
				}
				if (!boxSet.empty())
				{
					for (int i = 0; i < nRArr.size(); i++)
					{
						boxSet.insert(nRArr[i]);
					}
					set<int> otherBoxKeySet;
					for (map<int,vector<int>>::const_iterator i = boxHasKey.begin(); i != boxHasKey.end(); i++)
					{
						if (boxSet.find(i->first)!=boxSet.end())
						{
							continue;
						}
						otherBoxKeySet.insert(i->second.begin(), i->second.end());
					}
					if (otherBoxKeySet.find(itt->second) == otherBoxKeySet.end())
					{
						nRArr.pop_back();
						continue;
					}
				}
			}
		}
		

		
		

		if (CalTi4(nKeySetT, keyBoxMap, boxHasKey, nRArr))
		{
			return true;
		}
		nRArr.pop_back();
	}
	return false;
}

void Cti1Dlg::OnBnClickedOk()
{
	// TODO: �ڴ���ӿؼ�֪ͨ����������

	if (1)
	{
		CStdioFile file;
		BOOL bOpen = file.Open("C:\\input4", CFile::modeRead);
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
				}
				int nKeyNum = atoi(strArrT[0]);
				int nBoxNum = atoi(strArrT[1]);
				multiset<int> nKeySet;
				map<int, vector<int>> keyBoxMap;
				map<int, vector<int>> boxHasKey;
				strArrT.clear();
				strArrT = string2Arr(strArr[nPos++], ' ');
				if (strArrT.size()!=nKeyNum)
				{
					AfxMessageBox("error!!!");
				}
				for (int j = 0; j < nKeyNum; j++)
				{
					nKeySet.insert(atoi(strArrT[j]));
				}



				multiset<int> nKeyNeedSet;
				multiset<int> nKeyAllSet = nKeySet;
				for (int j = 0; j < nBoxNum; j++)
				{
					vector<CString> strArrT = string2Arr(strArr[nPos++], ' ');
					if (strArrT.size()<2)
					{
						AfxMessageBox("error!!!!!");
					}
					nKeyNeedSet.insert(atoi(strArrT[0]));
					keyBoxMap[atoi(strArrT[0])].push_back(j+1) ;
					boxHasKey[j+1].clear();
					for (int k = 2; k < strArrT.size(); k++)
					{
						boxHasKey[j+1].push_back(atoi(strArrT[k]));
						nKeyAllSet.insert(atoi(strArrT[k]));
					}
				}
				vector<int> nRArr;
				CString strR = " IMPOSSIBLE";
				if (std::includes(nKeyAllSet.begin(), nKeyAllSet.end(), nKeyNeedSet.begin(), nKeyNeedSet.end()))
				{
					if (CalTi4(nKeySet, keyBoxMap, boxHasKey, nRArr))
					{
						strR = "";
						for (int j = 0; j < nRArr.size(); j++)
						{
							strR+= " ";
							CString strT;
							strT.Format("%d", nRArr[j]);
							strR += strT;
						}
					}
				}
				else
				{
					strR = " IMPOSSIBLE";
				}
				CString strIndex;
				strIndex.Format("Case #%d:", i+1);
				strIndex += strR;
				strRArr.push_back(strIndex);
			}

			CStdioFile fileT;
			bOpen = fileT.Open("C:\\output4", CFile::modeWrite|CFile::modeCreate);
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
