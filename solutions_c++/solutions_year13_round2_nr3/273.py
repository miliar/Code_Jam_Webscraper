#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

FILE *dict=fopen("dictionary.txt","r");
FILE *out=fopen("CSmall.out","w");

char s[555];
int N;//,c=0,path[555];
//map<string,bool> m;
int trie[3333333][27],F[3333333],II;
int best[50][6][1125079];

int solve(int ind,int last,int tind)
{
	//printf("%d %d %d\n");
	if(tind==-1)return 1<<28;
	if(ind==N)
	{
		if(F[tind])return 0;
		return 1<<28;
	}
	
	if(best[ind][last][tind]!=-1)return best[ind][last][tind];
	
	int ret=1<<28;
	
	if(F[tind])ret=min(ret,solve(ind,last,0));
	
	if(last==5)
	{
		//path[I]=ind;
		fo(i,26)
			ret=min(ret,1+solve(ind+1,1,trie[tind][i]));
	}
	
	ret=min(ret,solve(ind+1,min(5,last+1),trie[tind][s[ind]-'a']));
	
	return best[ind][last][tind]=ret;
}


void addToTrie(string S)
{
	int ind=0;
	int NN=S.sz;
	fo(i,NN)
	{
		if(trie[ind][S[i]-'a']==-1)
		{
			trie[ind][S[i]-'a']=II;
			ind=II;
			
			II++;
			if(i==NN-1)
				F[ind]=1;
		}
		else ind=trie[ind][S[i]-'a'];
	}
}

int main()
{
    freopen ("C-small-attempt1.in","r",stdin);
    //freopen ("CSmall.out","w",stdout);
    
    int x=0;
    
    clr(trie,-1);
    II=1;
    
    while(fscanf(dict,"%s",s)!=EOF)
	{
		//m[string(s)]=1;
		x+=strlen(s);
		//if(strlen(s)<3)printf("%s\n",s);
		addToTrie(string(s));
	}
    //printf("%d %d\n",II,x);
    int T,k=0;
    
    scanf("%d",&T);
    //printf("%d\n",T);
    while(T--)
	{
		clr(best,-1);
		
		k++;
		
		scanf("%s",s);
		N=strlen(s);
		
		//printf("Case #%d: %d\n",k,solve(0,5,0));
		fprintf(out,"Case #%d: %d\n",k,solve(0,5,0));
	}
    
    
}


































