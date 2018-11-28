

#include <iostream>
using namespace std;

int main() {


//	freopen("A.in","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int t,tt;
	cin>>t;
	tt=t;
	while(t--)
	{
		int ch;
		cin>>ch;
		int chs[4];
		int ar[4][4];
		for(int q=0;q<4;q++)
		if(q==ch-1)
		for(int qq=0;qq<4;qq++)
		cin>>chs[qq];
		else
		for(int qq=0;qq<4;qq++)
		cin>>ar[q][qq];
		
		int ch2;
		cin>>ch2;
		int chs2[4];
		int ar2[4][4];
		for(int q=0;q<4;q++)
		if(q==ch2-1)
		for(int qq=0;qq<4;qq++)
		cin>>chs2[qq];
		else
		for(int qq=0;qq<4;qq++)
		cin>>ar2[q][qq];
		
		int co=0,ans;
		
		for(int q=0;q<4;q++)
		for(int qq=0;qq<4;qq++)
		if(chs[q]==chs2[qq])
		{co++;ans=chs2[qq];}
	
		cout<<"Case #"<<tt-t<<": ";
		if(co==1)
		cout<<ans<<endl;
		else 
		if(co==0)
		cout<<"Volunteer cheated!"<<endl;
		else if(co>1)
		cout<<"Bad magician!"<<endl;
	}
	return 0;
}