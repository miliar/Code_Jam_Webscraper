#include<iostream>
using namespace std;
#include<algorithm>
#include<cstring>
#include<fstream>
#include<ostream>
const int N=1000+10;
double a[N],b[N];
double aa[N],bb[N];
int visa[N],visb[N];
int main()
{
	ifstream fin("D-large.in");  // 已有输入文件
ofstream fout("output.txt");  //输出文件
streambuf *cinbackup;  
streambuf *coutbackup; 
coutbackup= cout.rdbuf(fout.rdbuf());  //用 rdbuf() 搜索重新定向
cinbackup= cin.rdbuf(fin.rdbuf());  //用 rdbuf() 重新定向
	int tcase; cin>>tcase;
	int k=1;
	while(k<=tcase){
		int n; cin>>n;
		int i,j;
		for(i=1;i<=n;i++) cin>>a[i]; memset(visa,0,sizeof(visa));
		for(i=1;i<=n;i++) cin>>b[i]; memset(visb,0,sizeof(visb));
		sort(a+1,a+n+1); sort(b+1,b+n+1);
		//for(i=1;i<=n;i++) { aa[i]=a[n+1-i]; bb[i]=b[n+1-i]; }
		//for(i=1;i<=n;i++) { a[i]=aa[i]; b[i]=bb[i]; }
		//for(i=1;i<=n;i++) cout<<a[i]<<" "; cout<<endl;
		//for(i=1;i<=n;i++) cout<<b[i]<<" "; cout<<endl;
		int ans1=0,ans2=0;
		for(i=j=1;i<=n;i++){
			if(j>n) break;
			while(j<=n && b[i]>a[j]) j++;
			if(j<=n) ans1++;
			j++;
		}
		/*
		for(i=1;i<=n;i++){
			if(a[i]<b[n+1-i]) continue;
			else break;
		}
		ans1=n+1-i;
		*/
		for(i=j=1;i<=n;i++){
			if(j>n) break;
			while(j<=n && a[i]>b[j]) { ans2++; j++; }
			j++;
		}
		cout<<"Case #"<<k++<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}