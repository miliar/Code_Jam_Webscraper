#include <iostream>
 
using namespace std;
 
int n, m;
int lawn[101][101];
 
void main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j,z,t,xc,yc,x,y;
	bool flag;

    cin>>t;

    for(z=0;z<t;z++)
    {
		cin>>n>>m;
 
        for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {
				cin>>lawn[i][j];
			}
		}
 
		flag=0;
 
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {

				xc=0; yc=0;
				for(x=0;x<n;x++) {					
					if (lawn[i][j]>=lawn[x][j]) xc++;
				}
				for(y=0;y<m;y++) {					
					if (lawn[i][j]>=lawn[i][y]) yc++;
				}
				if (xc==n||yc==m) flag=1; else flag=0;

				if(!flag) break;
			}
			if(!flag) break;
		}
		
		cout<<"Case #"<<z+1<<": ";
		if (flag) cout<<"YES"<<endl; else cout<<"NO"<<endl;
	}
}