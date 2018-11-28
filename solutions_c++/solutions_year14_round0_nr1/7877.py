#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define N 5
using namespace std;

int BG[1005],GB;
int k;
string ans[N]= {"Case #",": ","Bad magician!", "Volunteer cheated!"};

int judge(int f[N][N],int o,int s[N][N],int t,int* a)
{
	int pos = -1;
	for(int i = 1; i < N; i++)
		for(int j = 1; j < N; j++) if(f[o][j] == s[t][i]) (*a) = f[o][j],pos++;
    return pos;
}

void doit()
{
	int first[N][N], second[N][N], one, two,pos,result;
	cin>>k;
	for(int bg=1; bg<= k; bg++)
	{
		cin>>one;
		for(int i = 1; i <N ; i++)
			for(int j = 1; j <N ; j++) cin>>first[i][j];
		cin>>two;
		for(int i = 1; i <N ; i++)
			for(int j = 1; j <N ; j++) cin>>second[i][j];
		cout<<ans[0]<<bg<<ans[1];
		pos = judge(first,one,second,two,&result);
		if(-1 == pos) cout<<ans[3];
		else if(pos) cout<<ans[2]; else cout<<result;
		cout<<endl;
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    doit();
    return 0;
}

