#include<iostream>
using namespace std;
#include<fstream>
#include<ostream>
#include<iomanip>
#include<cstdio>
int main()
{
	
	ifstream fin("B-small-attempt6.in");  // ���������ļ�
ofstream fout("output.txt");  //����ļ�
streambuf *cinbackup;  
streambuf *coutbackup; 
coutbackup= cout.rdbuf(fout.rdbuf());  //�� rdbuf() �������¶���
cinbackup= cin.rdbuf(fin.rdbuf());  //�� rdbuf() ���¶���
	
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
