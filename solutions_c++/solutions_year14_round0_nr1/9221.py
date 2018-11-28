#include<iostream>

using namespace std;

int a[4][4],b[4][4];
bool vis[100];

void doit(int casenum)
{
	int x,y;
	cin>>x;
	int ans = 0;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			cin>>a[i][j];
	cin>>y;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			cin>>b[i][j];
	for(int i=0;i<20;++i)
		vis[i] = false;
	for(int j=0;j<4;++j)
		vis[a[x-1][j]]=true;
	int pos =0;
	for(int j=0;j<4;++j)
		if(vis[b[y-1][j]])
		{
			++ans;
			pos=b[y-1][j];
		}
	if(ans==0)
		cout<<"Case #"<<casenum<<": Volunteer cheated!"<<endl;
	else if(ans==1)
	{
		cout<<"Case #"<<casenum<<": "<<pos<<endl;
	}else{
		cout<<"Case #"<<casenum <<": Bad magician!"<<endl;
	}

}
int main()
{
	freopen ("myfile.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;++i)
		doit(i+1);
	return 0;
}