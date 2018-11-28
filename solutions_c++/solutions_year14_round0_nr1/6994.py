#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

#define fori(i,n) for(i=0;i<n;++i)
#define forin(i,s,n) for(i=s;i<=n;++i)
#define forn(i,n) for(i=n-1;i>=0;--i)
#define forni(i,n,e) for(i=n;i>=e;--i)
#define nil NULL
#define itr iterator
#define MAX(a,  b) ((a) > (b) ? (a) : (b))
#define MIN(a,  b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SQ(X) ( (X) * (X) )
#define pb push_back
//#define mod 1000000009
//#define getchar getchar_unlocked

typedef long int li;
typedef long long int lli;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long> vli;
typedef vector<long long> vlli;
typedef pair<int,int> ii;

/*------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++Source Code+++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------*/
//Functions and Global variables
//int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }
//double pi=2*acos(0.0);
inline void fReadInt(int &x,FILE *fp) {
	    //Change the comment in macro of getchar_unlocked
		register int c = fgetc(fp);
	    x = 0;
	    int neg = 0;
	 
	    for(; ((c<48 || c>57) && c != '-'); c = fgetc(fp));
	 
	    if(c=='-') {
	        neg = 1;
	        c = fgetc(fp);
	    }
	 
	    for(; c>47 && c<58 ; c = fgetc(fp)) {
	        x = (x<<1) + (x<<3) + c - 48;
	    }
	 
	    if(neg)
	        x = -x;
	}
//Main()
int main()
{  
	int t,i;
	FILE *fp,*fo;
	fp=fopen("A-small-attempt1.in","r");
	fo=fopen("output.in","a");
	//scanf("%d",&t);
	fReadInt(t,fp);
	fori(i,t)
	{
		int a[5][5];
		int r,j,k;
		//scanf("%d",&r);
		fReadInt(r,fp);
		fori(j,4)
		fori(k,4)
		fReadInt(a[j][k],fp);
		//scanf("%d",&a[j][k]);
		
		vi v(4);
		vi::itr it;
		int v1[4];
		int v2[4];
		
		v1[0]=(a[r-1][0]);
		v1[1]=(a[r-1][1]);
		v1[2]=(a[r-1][2]);
		v1[3]=(a[r-1][3]);
		
		//scanf("%d",&r);
		fReadInt(r,fp);
		fori(j,4)
		fori(k,4)
		fReadInt(a[j][k],fp);
		//scanf("%d",&a[j][k]);
		
		
		v2[0]=(a[r-1][0]);
		v2[1]=(a[r-1][1]);
		v2[2]=(a[r-1][2]);
		v2[3]=(a[r-1][3]);
		sort(v1,v1+4);
		sort(v2,v2+4);
		fori(j,4)
		
		/*cout<<v1[j]<<' ';
		cout<<endl;
		fori(j,4)
		cout<<v2[j]<<' ';
		cout<<endl;*/
		
		
		it=set_intersection(v1,v1+4,v2,v2+4,v.begin());
	
		
		//for(vi::itr it=v.begin();it!=v.end();++it)
		//cout<<*it<<' ';
		//cout<<endl;
		v.resize(it-v.begin());
		
		int s=v.size();
		//cout<<"Case #"<<i+1<<":"<<' ';
		fprintf(fo,"Case #%d: ",i+1);
		/*if(s==0)
		cout<<"Volunteer cheated!\n";
		else if(s==1)
		cout<<v[0]<<endl;
		else
		cout<<"Bad magician!\n";*/
		
		if(s==0)
		fprintf(fo,"Volunteer cheated!\n");
		else if(s==1)
		fprintf(fo,"%d\n",v[0]);
		else
		fprintf(fo,"Bad magician!\n");
		
		v.clear();
		
		
		
		
	}
	fclose(fp);
	fclose(fo);
	
  return 0;
}


