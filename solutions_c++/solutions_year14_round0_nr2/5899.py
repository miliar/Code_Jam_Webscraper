#include <iostream>
#include <fstream>
#include<iomanip>
#include <cmath>
using namespace std;

int main()
{
	ifstream cin;
	cin.open("a.in");
	ofstream cout("a.out");
	cout<<setprecision(7);
	int T;
	cin>>T;
	double C,F,X;
	int num=0;
	int n=0;
	while(n++<T)
	{
		double res=0;
		cin>>C>>F>>X;
		if((X*F-2*C)/(C*F)<0)
			num=0;
		else
			num=ceil((X*F-2*C)/(C*F))-1;
		for(int i=0;i<num;i++)
			res+=C/(i*F+2);
		res+=X/(num*F+2);
			cout<<"Case #"<<n<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<(double)(res)<<endl;

	}
}

/*//DFSµÚ¶þÕ½£¡£¡
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <queue>
using namespace std;
const int INF=1000000;
typedef pair<int,int> P;
char maze[300][300];
int n,m;
int sx,sy;
int gx,gy;
int d[300][300];
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};
int bfs()
{
	queue<P> que;
	for(int i = 0;i<n;i++)
		for(int j = 0;j<n;j++)
			d[i][j]=INF;
	que.push(P(sx,sy));
	d[sx][sy] = 0;
	while(que.size())
	{
		P p=que.front();
		que.pop();
		if(p.first==gx&&p.second==gy)
			break;
		for(int i = 0;i<4;i++)
		{
			int nx = p.first+dx[i];
			int ny = p.second+dy[i];
			if(0<=nx&&nx<n&&0<=ny&&ny<m&&maze[nx][ny]!='#'&&d[nx][ny]==INF)
			{	que.push(P(nx,ny));
			d[nx][ny]=d[p.first][p.second]+1;}
		}
	}
	return d[gx][gy];
}
int main()
{
	ifstream cin;
	cin.open("a.in");	
	cin>>n>>m;
	for(int i = 0;i<n;i++)
		for(int j = 0;j<n;j++)
		{
			cin>>maze[i][j];
			if(maze[i][j]=='G')
			{
				gx = i;
				gy = j;
			}else if(maze[i][j]=='S')
			{
				sx = i;
				sy = j;
			}
		}
	for(int i = 0;i<n;i++)
		{for(int j = 0;j<n;j++)
		cout<<maze[i][j];
	cout<<endl;}
	int d = bfs();
	cout<<d;
	return 0;
}*/
/*
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;
#define MAX 21
bool fi(int a,int n,int * b)
{
	for(int i=0;i<n;i++)
	{
		if(*(b+i)==a)
			return true;
	}
	return false;
}

int main(){
	ifstream cin;
	cin.open(("a.in"));
	int t,n,m;
	cin>>t;
	string a,b,sen;
	vector<string>::iterator it0,it1,it2;
	int ini = 0;
	while(ini++<t)
	{
		vector<string> str;
		int mp[MAX];
		for(int i = 0; i<MAX; i++)
		{
			mp[i]=-1;
		}
		int temp[MAX]={0};
		cin>>n>>m;
		int i=0;
		while(m--)
		{
			cin>>a>>b;
			it1 = find(str.begin(),str.end(),a);
			it2 = find(str.begin(),str.end(),b);
			if(it1 != str.end())
			{
				if(it2 != str.end())
					mp[it1-str.begin()] = it2-str.begin();
				else
				{
					mp[it1-str.begin()] = str.size();
					str.push_back(b);
				}
			}else
			{
				str.push_back(a);
				str.push_back(b);
				mp[str.size()-2] = str.size()-1;
			}
		}
		cin.clear();
		cin.ignore();
		getline(cin,sen);
		cout<<"Case #"<<ini<<": ";
		string word;
		while(sen.size())
		{
			if(find(sen.begin(),sen.end(),' ') != sen.end())
			{
				word = sen.substr(0,sen.find(' '));
				sen = sen.substr(word.size()+1,sen.size()-word.size()-1);
			}else{
				word = sen;
				sen = "";
			}
			it0 = find(str.begin(),str.end(),word);
			if(it0 != str.end())
			{
				int j = it0-str.begin();
				int k = 0;
				int flag = 0;
				while(1)
				{						
					if(mp[j]==-1)
					{
						flag = 1;
						break;
					}
					if(fi(mp[j],k,temp))
						break;
					temp[k++]=mp[j];
					j=mp[j];
				}
				if(flag)
					word=(n>=k)?str[temp[k-1]]:str[temp[n-1]];
				else
					word = str[temp[(n-1)%k-1]];
			}
			cout<<word;
			if(sen.size())
				cout<<' ';
		}
		cout<<endl;			
	}
	return 0;
}
*/





/*
inline vo                                                                                           id swap(int &x, int &y)
{
	int temp = x;
	x = y;
	y = temp;
}
void perm(int *list,int k,int m){
	int i ;
	for(i = k;i <= m;i++)
		cout<<list[i];
		cout<<endl;
	if(k == m){
		for(i = 0;i <= m;i++)
		cout<<list[i];
		cout<<endl;
	}else{
		for(i = k;i <= m;i++)
		{
			swap(list[i], list[k]);
			perm(list,k+1,m);
			swap(list[i],list[k]);
		}
	}
}
int main(){
	int list[3]={1,2,3};
	perm(list,0,2);
	return 0;
}
*/