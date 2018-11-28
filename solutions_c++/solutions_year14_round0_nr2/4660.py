#include<iostream>
using namespace std;
#include<fstream>
#include<ostream>
#include<iomanip>
#include<cstdio>
int main()
{
	
	ifstream fin("B-small-attempt6.in");  // 已有输入文件
ofstream fout("output.txt");  //输出文件
streambuf *cinbackup;  
streambuf *coutbackup; 
coutbackup= cout.rdbuf(fout.rdbuf());  //用 rdbuf() 搜索重新定向
cinbackup= cin.rdbuf(fin.rdbuf());  //用 rdbuf() 重新定向
	
	int tcase; cin>>tcase;
	int k=1;
	while(k<=tcase){
		long double c,f,x; cin>>c>>f>>x;
		long double cp=2,ans=0;
		long double ans1=c/cp+x/(cp+f),ans2=x/cp;
		while(1){
			if(ans1-ans2>1e-7) { ans+=ans2; break; }
			ans+=c/cp; cp+=f;
			ans1=c/cp+x/(cp+f); ans2=x/cp;
		}
		cout<<"Case #"<<k++<<": ";
		cout<<setiosflags(ios::fixed)<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
