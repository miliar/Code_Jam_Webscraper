#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
	int t,t1=0;
	cin>>t;
	while(t1++<t){
		int f[4][4],l[4][4], fa,sa;
		int row[4], count=0,ans;
		cin>>fa;
		fa--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				scanf("%d",&f[i][j]);
				if (i==fa)
					row[j]=f[i][j];
			}
		cin>>sa;
		sa--;
		/*cout<<"row =\n";
		for(int k=0;k<4;k++)
			cout<<row[k]<<" ";
		cout<<"\n";*/
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				scanf("%d",&l[i][j]);
				if (i==sa)
					for(int k=0;k<4;k++)
						if (row[k]==l[i][j]){
							//cout<<"row["<<k<<"] = "<<row[k]<<" = l["<<i<<"]["<<j<<"]";
							count++;
							ans=k;
					}
			}
		cout<<"Case #"<<t1<<": ";
		if (count==0)
			cout<<"Volunteer cheated!";
		else if (count>1)
			cout<<"Bad magician!";
		else
			cout<<row[ans];
		cout<<endl;
	}
}