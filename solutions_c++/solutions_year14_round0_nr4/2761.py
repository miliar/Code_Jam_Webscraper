
#include <iostream>
#include <cstdio>
using namespace std;

int main() {



//	freopen("D.in","r",stdin);
//	freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);


	int ttt,tt;
	cin>>tt;
	ttt=tt;
	while(tt--)
	{
		int nn;
		cin>>nn;
		double n[1000],t[1000];
		
		for(int q=0;q<nn;q++)
		cin>>n[q];
		for(int q=0;q<nn;q++)
		cin>>t[q];
		for(int q=0;q<nn;q++)
		for(int qq=q+1;qq<nn;qq++)
		{
			if(n[q]>n[qq])
			{
				double p=n[q];
				n[q]=n[qq];
				n[qq]=p;
			}
			if(t[q]>t[qq])
			{
				double p=t[q];
				t[q]=t[qq];
				t[qq]=p;
			}
		}
		
		int nnn=nn,tc=0,nc=0,tco=nn-1,nco=nn-1,dw=0;
		while(nnn--)
		{
			if(n[nc]<t[tc])
			{
				nc++;
				tco--;
			}
			else
			{
				nc++;
				tc++;
				dw++;
			}
		}
		
		nnn=nn;nc=tc=0;nco=tco=nn-1;
		int w=0;
		while(nnn--)
		{
			if(n[nco]>t[tco])
			{
				nco--;
				tc++;
				w++;
			}
			else
			{
				nco--;
				tco--;
				
			}
		}
		cout<<"Case #"<<ttt-tt<<": ";
		//printf("%.7f",ret);
		cout<<dw<<" "<<w<<endl;
	}
	return 0;
}