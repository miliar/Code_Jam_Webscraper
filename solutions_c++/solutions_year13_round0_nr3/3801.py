#pragma comment(linker,"/opt:nowin98")
#pragma comment(lib,"shlwapi")
#pragma comment(lib,"ntl")

#define UNICODE

#include"NTL/ZZ.h"
#include<windows.h>
#include<shlwapi.h>
#include<stdio.h>

#define IDU_BUTTON1 100

TCHAR szClassName[]=TEXT("Window");


long len(const ZZ& n)
{
	long i;
	ZZ num;
	num=abs(n);
	for(i=0;num!=0;i++)num/=10;
	return (n>0)?i:i+1;
}

void zztostr(const ZZ& n,char* str,int len)
{
	ZZ num;
	num=abs(n);
	str[len--]='\0';
	do{
		str[len--]='0'+(char)(num%10);
		num/=10;
	}while(num!=0);
	if(n<0)str[0]='-';
}

BOOL is_palindromic(ZZ n)
{
	char str1[200];
	char str2[200];
	zztostr(n,str1,len(n));
	lstrcpyA(str2,str1);
	_strrev(str2);
	return _stricmp(str1,str2)==0;
}


LRESULT CALLBACK WndProc(HWND hWnd,UINT msg,WPARAM wParam,LPARAM lParam)
{
	static HWND hEdit;
	static HWND hStatic;
	static HWND hButton1;
	static HWND hButton2;
	switch(msg)
	{
	case WM_CREATE:
		hEdit=CreateWindowEx(WS_EX_CLIENTEDGE,TEXT("EDIT"),0,WS_VISIBLE|WS_CHILD|ES_AUTOHSCROLL,74,10,256,32,hWnd,(HMENU)100,((LPCREATESTRUCT)lParam)->hInstance,0);
		hStatic=CreateWindow(TEXT("STATIC"),TEXT("データ:"),WS_VISIBLE|WS_CHILD,10,10,64,32,hWnd,0,((LPCREATESTRUCT)lParam)->hInstance,0);
		hButton1=CreateWindow(TEXT("BUTTON"),TEXT("..."),WS_VISIBLE|WS_CHILD,74+256,10,32,32,hWnd,(HMENU)101,((LPCREATESTRUCT)lParam)->hInstance,0);
		hButton2=CreateWindow(TEXT("BUTTON"),TEXT("判定開始"),WS_VISIBLE|WS_CHILD|WS_DISABLED,10,50,128,32,hWnd,(HMENU)102,((LPCREATESTRUCT)lParam)->hInstance,0);
		DragAcceptFiles(hWnd,1);
		break;
    case WM_CTLCOLORSTATIC:
		SetBkMode((HDC)wParam,TRANSPARENT);
		return(LRESULT)GetStockObject(WHITE_BRUSH);
	case WM_COMMAND:
		if(LOWORD(wParam)==100)
		{
			if(HIWORD(wParam)==EN_CHANGE)
			{
				TCHAR szFilePath[MAX_PATH];
				GetWindowText(hEdit,szFilePath,MAX_PATH);
				EnableWindow(hButton2,PathFileExists(szFilePath));
			}
		}
		else if(LOWORD(wParam)==101)
		{
			OPENFILENAMEW ofn={0};
			TCHAR szFilePath[MAX_PATH]={0};
			TCHAR szFileName[MAX_PATH]={0};
			ofn.lStructSize=sizeof(ofn);
			ofn.hwndOwner=hWnd;
			ofn.lpstrFilter=TEXT("Data (*.*)\0*.*\0すべてのファイル(*.*)\0*.*\0\0");
			ofn.lpstrFile=szFilePath;
			ofn.lpstrFileTitle=szFileName;
			ofn.nMaxFile=sizeof(szFilePath)/sizeof(TCHAR);
			ofn.nMaxFileTitle=sizeof(szFileName)/sizeof(TCHAR);
			ofn.Flags=OFN_FILEMUSTEXIST;
			ofn.lpstrTitle=TEXT("ファイルを開く");
			if(GetOpenFileName(&ofn))
			{
				SetWindowText(hEdit,szFilePath);
			}
		}
		else if(LOWORD(wParam)==102)
		{
			// test code
			/*
			ZZ a;a=122;
			if(is_palindromic(a))
			{
				MessageBox(hWnd,0,0,0);
			}
			else
			{
				MessageBox(hWnd,TEXT("ちがう"),0,0);
			}
			return 0;
			*/

			TCHAR szInFilePath[MAX_PATH];
			TCHAR szOutFilePath[MAX_PATH];
			GetWindowText(hEdit,szInFilePath,MAX_PATH);
			lstrcpy(szOutFilePath,szInFilePath);
			lstrcat(szOutFilePath,TEXT(".out"));
			HANDLE hFile=CreateFile(szInFilePath,GENERIC_READ,0,0,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL,0);
			if(hFile==INVALID_HANDLE_VALUE)
			{
				MessageBox(0,TEXT("ファイルが開けません"),0,MB_OK);
			}
			else
			{
				DWORD dwReadSize;
				DWORD dwWriteSize;
				const DWORD dwFileSize=GetFileSize(hFile,0);
				LPSTR lpszText=(LPSTR)GlobalAlloc(GMEM_FIXED,dwFileSize+1);
				lpszText[dwFileSize]=0;
				ReadFile(hFile,lpszText,dwFileSize,&dwReadSize,0);
				CloseHandle(hFile);
				hFile=CreateFile(szOutFilePath,GENERIC_WRITE,0,0,CREATE_ALWAYS,FILE_ATTRIBUTE_NORMAL,0);
				CHAR seps[]="\r\n";
				CHAR *token=strtok(lpszText,seps);
				if(token)
				{
					const int nMax=atol(token);
					char szOutputText[1024];
					for(int i=0;i<nMax;i++)
					{
						token=strtok(0,seps);
						const char*pMin=token;
						char*p=token;
						while(*p!=' ')p++;*p=0;
						const char*pMax=p+1;
						ZZ zzMin,zzMax;
						conv(zzMin,pMin);
						conv(zzMax,pMax);

						ZZ zzStart=SqrRoot(zzMin);{char szText[1000];zztostr(zzStart,szText,len(zzStart));OutputDebugStringA("zzStart=");OutputDebugStringA(szText);OutputDebugStringA("\r\n");}
						ZZ zzEnd=SqrRoot(zzMax);{char szText[1000];zztostr(zzEnd,szText,len(zzEnd));OutputDebugStringA("zzEnd=");OutputDebugStringA(szText);OutputDebugStringA("\r\n");}

						ZZ zzCount;zzCount=0;
						for(ZZ j=zzStart;j<=zzEnd;j++)
						{
							ZZ var=j*j;
							if(zzMin<=var&&var<=zzMax&&is_palindromic(j)&&is_palindromic(j*j))
							{
								zzCount++;
							}
						}


						char szCount[200];
						zztostr(zzCount,szCount,len(zzCount));


						wsprintfA(szOutputText,"Case #%d: ",i+1);
						WriteFile(hFile,szOutputText,lstrlenA(szOutputText),&dwWriteSize,0);
						wsprintfA(szOutputText,"%s\r\n",szCount);
						WriteFile(hFile,szOutputText,lstrlenA(szOutputText),&dwWriteSize,0);

					}
				}
				CloseHandle(hFile);
				GlobalFree(lpszText);
			}
		}
		break;
	case WM_DROPFILES:
		{
			const HDROP hDrop=(HDROP)wParam; 
			TCHAR szFilePath[MAX_PATH];
			DragQueryFile(hDrop,0,szFilePath,sizeof(szFilePath));
			DragFinish(hDrop);
			SetWindowText(hEdit,szFilePath);
		}
		break;	
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd,msg,wParam,lParam);
	}
	return 0;
}


int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPreInst,
				   LPSTR pCmdLine,int nCmdShow)
{
	MSG msg;
	WNDCLASS wndclass={
		CS_HREDRAW|CS_VREDRAW,
		WndProc,
		0,
		0,
		hInstance,
		0,
		LoadCursor(0,IDC_ARROW),
		(HBRUSH)(COLOR_WINDOW+1),
		0,
		szClassName
	};
	RegisterClass(&wndclass);
	HWND hWnd=CreateWindow(
			szClassName,
			TEXT("Window"),
			WS_OVERLAPPEDWINDOW,
			CW_USEDEFAULT,
			0,
			CW_USEDEFAULT,
			0,
			0,
			0,
			hInstance,
			0
		);
	ShowWindow(hWnd,SW_SHOWDEFAULT);
	UpdateWindow(hWnd);
	while(GetMessage(&msg,0,0,0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return msg.wParam;
}
