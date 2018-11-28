#include <STDIO.H>
#include <WINSOCK2.H>

#pragma comment(lib,"ws2_32.lib")

int main()
{
	WORD wVersionRequested;
	WSADATA wsaData;
	int err;

	wVersionRequested = MAKEWORD( 1, 1 );

	err = WSAStartup( wVersionRequested, &wsaData );
	if ( err != 0 ) {
		/* Tell the user that we could not find a usable */
		/* WinSock DLL.                                  */
		return 0;
	}

	/* Confirm that the WinSock DLL supports 2.2.*/
	/* Note that if the DLL supports versions greater    */
	/* than 2.2 in addition to 2.2, it will still return */
	/* 2.2 in wVersion since that is the version we      */
	/* requested.                                        */

	if ( LOBYTE( wsaData.wVersion ) != 1 ||
		HIBYTE( wsaData.wVersion ) != 1 ) {
			/* Tell the user that we could not find a usable */
			/* WinSock DLL.*/
			WSACleanup( );
			return 0; 
	}

	/* The WinSock DLL is acceptable. Proceed. */
	SOCKET sockSrv = socket(AF_INET, SOCK_STREAM, 0);

	SOCKADDR_IN addrSrv;
	addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);
	addrSrv.sin_family = AF_INET;
	addrSrv.sin_port = htons(80);

	//绑定端口
	bind(sockSrv, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));

	//监听5555端口
	listen(sockSrv, 5);
	printf("以非阻塞方式监听 5555 端口\n");

	SOCKADDR_IN addrClient;
	int len = sizeof(SOCKADDR);

	//建立连接的套接字
	SOCKET sockConn = accept(sockSrv, (SOCKADDR*)&addrClient, &len);

	//发送数据
	// 	char sendBuf[100];
	// 	sprintf(sendBuf, "Welcome %s to my program\n", inet_ntoa(addrClient.sin_addr));
	// 	send(sockConn, sendBuf, strlen(sendBuf)+1, 0);

	while(1)
	{
		//接受数据
		char recvBuf[1024];
		memset(recvBuf, 0, 1024);
		int nReadLen = recv(sockConn, recvBuf, 100, 0);
		printf("%s\n", recvBuf);

		//发送数据
		char sendBuf[10000]="HTTP/1.1 200 OK..Cache-Control: private..Content-Type: text/html; charset=utf-8..Server: Microsoft-IIS/7.5..X-AspNet-Version: 2.0.50727..X-Powered-by: ASP.NET..Date: Wed, 10 Apr 2013 17:14:06 GMT..Connection:close..Content-Length: 1136....\\346\\234\\215\\345\\212\\241\\345\\231\\250\345\\212\\250\\344\\275\\234:101\\r\\n\\350\\200\\227\\346\\227\\266:44 \\346\\257\\253\\347\\247\\222 \\345\\256\\214\\346\\210\\220\\346\\203\\205\\345\\206\\265:True\\r\\n[truncated] \\350\\277\\224\\345\\233\\236\\344\\273\\243\\347\\240\\201\\357\\274\\232<outstr>D6FQQAAAAAAAABAA5W6QOYA4JGLCKJRPNXFHW72K6VFNPYDUUEEIAYATETMJAQAQ5TAYRTPGSLWB22KHEMU2WKUBZJSVMZK5MYLEBTHNTW6PPXT35667PXT35667POR3TVHCP567747VYZTEAFWPNTSK3LEZ4IM";
		send(sockConn, sendBuf, strlen(sendBuf)+1, 0);
	}
	closesocket(sockConn);
	return 0;
}





//#include <string>
//#include <stdio.h>
//#include <iostream>
//#include <vector>
//#include <algorithm>
//
//using namespace std;
//
//#define PARENT(i)	((i)/2)
//#define LEFT(i)		((i)*2)
//#define RIGHT(i)	((i)*2+1)
//
////保持最大堆性质
//void MaxHeapify(int* A, int i, int len)
//{
//	int l=LEFT(i+1) - 1;
//	int r=RIGHT(i+1) - 1;
//	int largest=0;
//	if (l <= len-1 && A[l] > A[i])
//	{
//		largest = l;
//	}
//	else
//	{
//		largest = i;
//	}
//	if (r <= len-1 && A[r] > A[largest])
//	{
//		largest = r;
//	}
//	if (largest != i)
//	{
//		swap(A[largest], A[i]);
//		MaxHeapify(A, largest, len);
//	}
//
//}
//
////建立最大堆
//void BuildMaxHeap(int* A, int len)
//{
//	for (int i=(len/2)-1; i>=0; i--)
//	{
//		MaxHeapify(A, i, len);
//	}
//}
//
////堆排序
//void HeapSort(int* A, int len)
//{
//	for (int i=len-1; i>=1; i--)
//	{
//		swap(A[0], A[i]);
//		len--;
//		MaxHeapify(A, 0, len);
//	}
//}
//
//int main()
//{
//	int A[10] = {16, 4, 10, 14, 7, 7, 3, 2, 8, 1};
//	BuildMaxHeap(A,10);
//	HeapSort(A, 10);
//	return 0;
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//#include<iostream>
//#include<cmath>
//using namespace std;
//
//
//int main()
//{
//	int T, t;
//	cin>>T;
//	t = 1;
//	while (t <= T)
//	{
//		int N, M, K;
//		cin>>N>>M>>K;
//		int result = 0;
//		if (N > M)
//		{
//			int tmp = N;
//			N = M;
//			M = tmp;
//		}
//		int n1 = int(K*K), n2 = M;
//		n1 = n1 > N ? N : n1;
//		for (; n1 * n2 > K; --n2);
//		int max = 0;
//		while (n1 >= 2 && n2 <= M)
//		{
//			int k = K;
//			result += ( n1 * (n1 - 1) * n2 * (n2 - 1) ) >> 2;
//			k -= n1 * n2;
//			if (n2 < M)
//				result += n2 * (k * (k - 1) / 2);
//			else
//				result += n1 * (k * (k - 1) / 2);
//			max = result > max ? result : max;
//			--n1;
//			n2 = K / n1;
//			result = 0;
//		}
//		cout<<"Case #"<<t<<": "<<max<<endl;
//		++t;
//	}
//	//cin>>t;
//	return 0;
//}
//
//
//


//
//
//#include <iostream>
//#include <assert.h>
//#include <algorithm>
//#include <vector>
//#include <map>
//#include <memory.h>
//#define MIN(x,y)((x)<(y)?(x):(y))
//#define MAX(x,y)((x)>(y)?(x):(y))
//
//using namespace std;
//
//
//int main()
//{
//	int t;
//	cin>>t;
//	for (int tt=0; tt<t; tt++)
//	{
//		int N=0,M=0,num=0;
//		cin>>N>>M>>num;
//		if (N > M)
//		{
//			int temp = N;
//			N = M;
//			M = temp;
//		}
//		int minNum=999999, minr=0, minc = 0;
//		if (num > N*M)
//		{
//			num = N*M;
//		}
//		if (N == 1 || M == 1 || num < 3)
//		{
//			cout<<"Case #"<<tt+1<<": "<<0<<endl;
//			continue;
//		}
//		long re=0;
//		for (int i=2; i<=N; i++)
//		{
//			for(int j=2; j<=M; j++)
//			{
//				if (0 <= (num - i*j ) && ((num - i*j) <= MIN(i,N) || (num - i*j) <= MIN(j,M)) )
//				{
//					minr = i;
//					minc = j;
//					minNum = num - i*j;
//
//					int m = minr-1;
//					int n = minc-1;
//					long all=n*m*(1+n)*(1+m)/4;
//					if (0 < minNum)
//					{
//						if (minr > minc)
//						{
//							int temp = minr;
//							minr = minc;
//							minc = temp;
//						}
//						if (N > M)
//						{
//							int temp = N;
//							N = M;
//							M = temp;
//						}
//						int cc = 0;
//						if (minc < M)
//						{
//							cc = minc+1;
//						}
//						else
//						{
//							cc = minr + 1;
//						}
//						if (minr < minNum)
//						{
//							if (minr == N)
//							{
//								continue;
//							}
//							cc = minr+1;
//						}
//						for (int idex=1; idex<minNum; idex++)
//						{
//							all += idex*(cc-1);
//						}
//					}
//					if (re < all)
//					{
//						re = all;
//					}
//				}
//			}
//		}
//
//		cout<<"Case #"<<tt+1<<": "<<re<<endl;
//		//cout<<minr<<" "<<minc<<endl;
//	}
//	cin>>t;
//	return 0;
//}
//
//
//






//#include <iostream>
//using namespace std;
//
//const int maxm = 10005;	//最大边数
//const int maxn = 105;	//最大点数
//
//struct aaa
//{
//	int s,f,next;	//邻接表的域，s表示边的起点，f表示终点，next指向点s的下一条边
//};
//
//aaa c[maxm];	//图的邻接表
//
//int sta[maxn],fa[maxn],zh[maxn];	//使用邻接表保存图中的边，sta数组为每个点邻接表表头指针，c数组存储了每条边。
//									//fa数组和zh数组用于广搜最短路径。
//									//其中zh数组为广搜使用的队列，fa数组保存了广搜的路径，f[i]表示i节点的父亲
//
//int d[maxn][maxn],e[maxn];//d保存了当前搜索的最短路径，d[i,j]表示搜索第i层（第i次寻找最短路径中）找到的第j个节点的编号
//
//bool b[maxn];
//
//int n,m,now,tot;	//now用于建邻接表时的累加，tot为迭代加深搜索的“界“
//bool goal;			//表示是否搜到了满足要求的界（不超过tot个点的解），如果找到了，goal=true，搜索退出
//
//void ins(int s, int f)
//{
//	now++;
//	c[now].s = s;
//	c[now].f = f;
//	c[now].next = sta[s];
//	sta[s] = now;
//}
//
//void bfs() //广搜最短路径
//{
//	int i,cl,op,k,t;
//	cl=0;
//	op=1;
//	for (i=1; i<=n; i++)
//	{
//		fa[i] = 0;
//	}
//	zh[1]=1;
//	fa[1]=-1;
//	while(cl<op)
//	{
//		cl++;
//		k=zh[cl];
//		for (t=sta[k];t;t=c[t].next)
//		{
//			if (b[c[t].f] && fa[c[t].f] == 0)
//			{
//				op++;
//				zh[op]=c[t].f;
//				fa[c[t].f]=c[t].s;
//				if (c[t].f == n)
//				{
//					break;
//				}
//			}
//		}
//		if (fa[n])
//		{
//			break;
//		}
//	}
//}
//
//
//
//int main()
//{
//	return 0;
//}
//
//
//
