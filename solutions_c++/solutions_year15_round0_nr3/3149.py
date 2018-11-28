
//~        Author : Sarvesh Mahajan                             
//               IIIT,Hyderabad                                   
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) cout<<n<<' '
#define si(n) cin>>n
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
#define F first
#define S second
#define sz(x) (int) x.size()
#define pLL(x) cout<<x<<' '
#define fill(x,c) memset(x,c,sizeof(x))
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#ifdef DEBUG
#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#else
#define DB(x)
#define DB2(x,y)
#define DB3(x,y,z)
#endif

char leftP[100005],rightP[100005];
int sign[100005],sign2[100005];
char xx[3]={'i','j','k'};
char get(char x,char y)
{
	int i;
	if(x == '1')
		return y;
	if(y == '1')
		return x;
	if(x == y)
		return '1';
	loop(i,3)
	{
		if(xx[i]!=x and xx[i]!=y)
			return xx[i];
	}
}

int getSign(char x,char y)
{
	if(x == '1' or y == '1')
		return 1;
	if(x == y)
		return -1;
	if(x == 'i' and y == 'k')
		return -1;
	if(x == 'j' and y == 'i')
		return -1;
	if(x == 'k' and y == 'j')
		return -1;
	return 1;
}

bool ok(char reqd,int idx)
{
	if(reqd == 'i')
		return (leftP[idx]=='i' and sign[idx]==1);
	else
		return (rightP[idx] == 'k' and sign2[idx] == 1);
}

string str;
bool check(int start,int end)
{
	int sign=1,i;
	char s='1';
	for(i=start;i<=end;++i)
	{
		sign*=getSign(s,str[i]);
		s=get(s,str[i]);
	}
//	DB2(s,sign)

	return (s=='j' and sign == 1);
}


pair<char,int> inv(char x,char y,int signx,int signy)  //x*inv=y
{
	//DB3(x,y,signx)
	//DB(signy)
	
	int sign=signx*signy;
	if(x == y)                return mp('1',sign);
	if(x == '1')              return mp(y,sign);
	if(y == '1')              return mp(x,sign*-1);
	if(x == 'i' and y == 'j')  return mp('k',-sign);
	if(x == 'i' and y == 'k')  return mp('j',sign);

	if(x == 'j' and y == 'i')  return mp('k',sign);
	if(x == 'j' and y == 'k')  return mp('i',-sign);
	if(y == 'i')               return mp('j',-sign);
	return mp('i',sign);
}
	




	

int main()
{
int n,t,m,l,k,ans,i,j,fl,T;
cin>>T;
string s;
int x;
Loop(t,T)
{
	str="";
	cin>>l>>x;
	cin>>s;
	loop(i,x)
		str+=s;
	leftP[0]=str[0];
	sign[0]=1;
	for(i=1;i<l*x;++i)
	{
		leftP[i]=get(leftP[i-1],str[i]);
		sign[i]=sign[i-1]*getSign(leftP[i-1],str[i]);
	}


	n=l*x;
	/*loop(i,n)
	{
		DB(leftP[i]);
		DB(sign[i]);
	}*/


	rightP[n-1]=str[n-1];
	sign2[n-1]=1;
	for(i=n-2;i>=0;--i)
	{
		rightP[i]=get(str[i],rightP[i+1]);
		sign2[i]=sign2[i+1]*getSign(str[i],rightP[i+1]);
	}
/*	loop(i,n)
	{
		DB(rightP[i]);
		DB(sign2[i]);
	}*/

	bool done=0;
	for(i=1;i<n-1;++i)
	{
		for(j=i;j<n-1;++j)
		{
			if(!ok('i',i-1))
				continue;
			if(!ok('k',j+1))
				continue;
		//	DB2(i,j)

	
			pair<char,int> tmp=inv(leftP[i-1],leftP[j],sign[i-1],sign[j]);//check(i,j))
	//		DB(tmp.F)
			if(tmp.F == 'j' and tmp.S == 1)	
			{
					done=1;
					break;
			}
		}
		if(done)
			break;
	}



	if(done)
	printf("Case #%d: %s\n",t,"YES");
	else
	printf("Case #%d: %s\n",t,"NO");
			
	


}
return 0;
}
