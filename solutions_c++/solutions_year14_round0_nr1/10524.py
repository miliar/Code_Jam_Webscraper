#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	int n,a,b,c[4][4],d[4][4],i,j,f,m,t;
	cin>>n;
	t=0;
	while(t++<n){
		f=0;
		cin>>a;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>c[i][j];
		cin>>b;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>d[i][j];
		a--;
		b--;
		cout<<"Case #"<<t<<": ";
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(c[a][i]==d[b][j]){	
					f=1;
					m=c[a][i];
					goto p;
				}
	p:	if (f==1){
			for(i++;i<4;i++)
				for(j=0;j<4;j++)
					if(c[a][i]==d[b][j]){	
						f=2;
						goto q;
					}
		}
	q:	if(f==1){
			cout<<m<<endl;
		}
		else if(f==2){
			cout<<"Bad magician!\n";
		}
		else
			cout<<"Volunteer cheated!\n";
	}
	return 0;
}