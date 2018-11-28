#include<bits/stdc++.h>
using namespace std;
struct ST
{
	vector<int>V;
	int s;
}tmp,frt;
queue<ST>Q;
set<string>S;
string ts(ST s)
{
	string r="";
	int i,sz=s.V.size();
	for(i=0;i<sz;i++)r+=char('0'+s.V[i]);
	sort(r.begin(),r.end());
	return r;
}
void OUT(ST s)
{
	cout<<s.s<<":{";
	if(s.V.empty()){cout<<"}"<<endl;return;}
	cout<<s.V[0];
	for(int i=1;i<s.V.size();i++)cout<<","<<s.V[i];
	cout<<"}"<<endl;
}
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout); 
	int T,cse,D,pi,i,j;
	string ss;
	scanf("%d",&T);
	vector<int>::iterator it;
	for(cse=1;cse<=T;cse++)
	{
		scanf("%d",&D);
		tmp.V.clear();
		tmp.s=0;
		for(i=0;i<D;i++){scanf("%d",&pi);tmp.V.push_back(pi);}
		while(!Q.empty())Q.pop();
		Q.push(tmp);
		S.clear();
		S.insert(ts(tmp));
		while(!Q.empty())
		{
			frt = Q.front();
			//OUT(frt);
			Q.pop();
			if(frt.V.empty())
			{
				printf("Case #%d: %d\n",cse,frt.s);
				goto NOP;
			}
			tmp = frt;
			tmp.s++;
			for(it=tmp.V.begin();it!=tmp.V.end();)
			{
				(*it)--;
				if(*it==0)tmp.V.erase(it);else it++;
			}
			ss=ts(tmp);
			if(S.find(ss) == S.end()){Q.push(tmp);S.insert(ss);}//OUT(tmp);
			for(i=0;i<frt.V.size();i++)
			{
				for(j=1;j<=frt.V[i]/2;j++)
				{
					tmp = frt;
					tmp.V[i]-=j;
					tmp.V.push_back(j);
					tmp.s++;
					ss=ts(tmp);
					if(S.find(ss) == S.end()){Q.push(tmp);S.insert(ss);}
					//OUT(tmp);
				}
			}
		}
		NOP:;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
