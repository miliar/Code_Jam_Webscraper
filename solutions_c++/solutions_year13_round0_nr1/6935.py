#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    cin>>test;
    char a[4][4];
    for (int Test=1;Test<=test;Test++){
		long long x, y;
		string ans;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				cin>>a[i][j];
		int flag=0;
		int total=0;
		for (int i=0;i<4;i++){
			int x1=0,o1=0,t1=0,x2=0,o2=0,t2=0;
			for (int j=0;j<4;j++){
				if (a[i][j]=='X')
					x1++;
				if (a[i][j]=='O')
					o1++;
				if (a[i][j]=='T')
					t1++;
				if (a[i][j]=='.')
					total++;
				if (a[j][i]=='X')
					x2++;
				if (a[j][i]=='O')
					o2++;
				if (a[j][i]=='T')
					t2++;
			}
			if (x1==4 || x1==3 && t1==1 || x2==4 || x2==3 && t2==1)
				flag|=1;
			if (o1==4 || o1==3 && t1==1 || o2==4 || o2==3 && t2==1)
				flag|=2;
		}
		int x1=0,o1=0,t1=0,x2=0,o2=0,t2=0;
		for (int j=0;j<4;j++){
			if (a[j][j]=='X')
				x1++;
			if (a[j][j]=='O')
				o1++;
			if (a[j][j]=='T')
				t1++;
			if (a[j][3-j]=='X')
				x2++;
			if (a[j][3-j]=='O')
				o2++;
			if (a[j][3-j]=='T')
				t2++;
		}
		if (x1==4 || x1==3 && t1==1 || x2==4 || x2==3 && t2==1)
			flag|=1;
		if (o1==4 || o1==3 && t1==1 || o2==4 || o2==3 && t2==1)
			flag|=2;
		if (flag==1)
			ans="X won";
		else if (flag==2)
			ans="O won";
		else if (flag==3)
			ans="please check the problem";
		else if (total==0)
			ans="Draw";
		else
			ans="Game has not completed";
		cout<<"Case #"<<Test<<": "<<ans<<endl;
	}
    return 0;
}
