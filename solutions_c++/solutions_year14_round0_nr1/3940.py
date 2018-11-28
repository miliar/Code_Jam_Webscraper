#include <bits/stdc++.h>
using namespace std;

int main(int argc,char *argv[]) {
	// your code goes here
	freopen("gcj1input.txt","r",stdin);
	freopen("gcj1output.txt","w",stdout);
	int T,R1,R2,a[5][5];
	cin>>T;
	set<int> s1,s2;
	int cnt=0;
	for(int TC=1;TC<=T;TC++)
	{
		cin>>R1;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin>>a[i][j];
		for(int i=0;i<4;i++) s1.insert(a[R1-1][i]);
		cin>>R2;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin>>a[i][j];
		for(int i=0;i<4;i++) s2.insert(a[R2-1][i]);
		cnt=0;
		int result=0;
		for(set<int>::iterator it=s1.begin();it!=s1.end();++it)
		{
			if(s2.find(*it)!=s2.end())
				{ result=*it; cnt++; }
		}
		if(cnt==1)
		{
			printf("Case #%d: %d\n",TC,result);
		}
		else if(cnt>1)
		{
			printf("Case #%d: Bad magician!\n",TC);
		}
		else if(cnt==0)
		{
			printf("Case #%d: Volunteer cheated!\n",TC);
		}
		s1.clear();s2.clear();
	}
	return 0;
}