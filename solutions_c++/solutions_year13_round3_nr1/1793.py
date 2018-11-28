

#include<iostream>
# include <cmath>
# include <algorithm>
# include <cstdio>
# include <cstring>
# include <string>
# include <cstdlib>
# include <vector>
# include <bitset>
# include <map>
# include <queue>
# include <stack>
# include <set>
# include <list>
# include <deque>
# include <functional>
# include <ctime>
using namespace std;

//#define DEBUG



#ifdef DEBUG
#define D(x) cout<<#x<<"="<<x<<" "
#define DN(x)  cout<<#x<<"="<<x<<"\n"
#define DA(a,n) cout<<#a<<"=["; printarray(a,n); cout<<"]\n"
#define DAR(a,n,s) cout<<#a<<"["<<s<<"-"<<s+n-1<<"]=["; printarray(a,n,s); cout<<"]\n"
#define DPR(fmt, ...) \
	do { printf(fmt, ## __VA_ARGS__); } while (0)
#else
#define D(x) 
#define DN(x)
#define DA(a,n) 
#define DAR(a,n,s)
#define DPR(fmt, ...) \
	do { } while (0)
#endif


// Useful constants
#define inf                         (int)1e9
#define eps		(double)1e-9
# define mod 1000000007
# define pi  3.14159265358979323846

#define sz(a)                       ((int)(a.size()))


//STL output ********************************
template <typename T1, typename T2>
inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p)
{
	return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v)
{
	bool first = true;
	os << "[";
	for(unsigned int i = 0; i < v.size(); i++)
	{
		if(!first)
			os << ", ";
		os << v[i];
		first = false;
	}
	return os << "]";
}


	
template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v)
{
	bool first = true;
	os << "[";
	for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
	{
		if(!first)
			os << ", ";
		os << *ii ;
		first = false;
	}
	return os << "]";
}
//*****************************************
//printing array
template<typename T,typename T2>
void printarray(T  a[],T2 sz,T2 beg=0)
{
	for(T2 i=beg;i<beg+sz;i++) cout<<a[i]<<" ";
}
//*********************************8

bool isvow(char a)
{
	return a=='a'||a=='e'||a=='i'||a=='o'||a=='u';
}
int fun_count(char *str,int n,int pre=0)
{
	int state=0;
	int conspre=0;
	int i=0,count=0;

	while(str[i]&& state==0)
	{
		if (!isvow(str[i])) 
		{
			state=1;
			break;
		}
		pre++;
		i++;
	}
	DN(i); 
	
	while(str[i]&& state==1)
	{
		if (isvow(str[i])) 
		{
			state=2;
			break;
		}
		conspre++;
		if(conspre>=n)
		{
			count+=conspre-n+1+pre;
		}
		i++;
	}
	int rem=0;
	if(str[i])
	{
		if (conspre>=n) 
		{
			rem=strlen(str)-i;
			count+=rem*(conspre-n+1+pre);
		}		
	}
	int nextpre;
	if(conspre<n) nextpre=pre+conspre;
	else nextpre=n-1;
	DN(count); 
	
	if(str[i])
	{
		count+=fun_count(&str[i],n,nextpre);
	}
	return count;
}

char str[1000005];
int main()
{
	int t,q;
	int i,j;
	int n,m,casen=0;
	scanf("%d",&t);
	while(++casen<=t)
	{
		//START
		D(casen); 
		
		scanf("%s",str);
		scanf("%d",&n);
		D(str); 
		DN(n); 
		
		int count=fun_count(str,n);
	
		printf("Case #%d: ",casen);
		printf("%d ",count);
		
		printf("\n");
	}
	return 0;
}	

