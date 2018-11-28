#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <queue>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))


typedef long long LL;

using namespace std;

int seen[10];

void A()
{	int t; cin>>t;
	LL num;

	FO(j,0,t)
	{	ARR0(seen);
		cin >> num;
 
		if(num==0)
			cout << "Case #"<<(j+1)<<": INSOMNIA"<<endl;
		else
		{	bool cont=true;
			int iter =1;
			while(cont)
			{	LL tmp = num*iter;
				while(tmp>0)
					{seen[tmp%10]=1;
					tmp/=10;}

				bool found =true;
				FO(k,0,10)
					if(seen[k]==0) found= false;

				if(found)
					break;
				iter++;

			}

			cout << "Case #"<<(j+1)<<": "<<(num*iter)<<endl;
		}
	}


}

int pcakes[101];

void bflip(int n)
{
	//cout << n << endl;
	int tofl= (n%2==0)?(n/2):(n/2)+1;


	FO(j,0,tofl)
		{
			int tmp = pcakes[j];
			pcakes[j] = (pcakes[n-j]==1)?0:1;
			pcakes[n-j] = (tmp==1)?0:1;
			
		}

	if(n%2==0)
	   pcakes[n/2] = (pcakes[n/2]==1)?0:1;
	
		

}

void showit(int total)
{
	FO(j,0,total)
		cout << pcakes[j];
	cout << endl;
}

void B()
{
	int t; cin>>t;
	LL num;
	int res;
	string str;
	int turns;
	FO(i,0,t)
	{	res =0;turns=0;
		cin>>str;
		ARR0(pcakes);
		int total = str.length();
		FO(j,0,total)
			pcakes[j] = str[j]=='-'?0:1;

		bool cont=true;
		int last;
		

		while(1==1)
		{	last = total-1;
			RO(j,total-1,0)
				if(pcakes[j]==1)
					last = j-1;
				else
					break;

			if(last<0)
				break;

			int first=0;
			if(pcakes[0]==0)
			{
				bflip(last);
			//	showit(total);
			}
			else
			{	int frrr=0;
				FO(k,0,last+1)
				{	//cout << k << " "<<pcakes[k]<<" - "<<pcakes[k+1]<<endl;
					if(pcakes[k]!=pcakes[k+1]&&pcakes[k]==1)
						{frrr = k;break;}
				}
			
				frrr = frrr<0?0:frrr;
				bflip(frrr);
			//	showit(total);
			}
			turns++;

		}

		
		cout << "Case #"<<(i+1)<<": "<<turns<<endl;
	}

}

int tt = 0;

LL allpos[20000];
void nextnum(LL num,int n)
{	tt++;
	LL mul=1;
	FO(j,0,n) mul*=10;
 
	allpos[tt] = (num + mul);

	if(n<14)
	{
		nextnum(num,n+1);
		nextnum(num+mul,n+1);
			
	}
}

LL iscoinjamtest(LL num)
{
	for(LL j=2;j*j<=num;j++)
		if(num%j==0)
			return j;
	
	return num;
}

LL getbasenum(LL n,int base)
{	LL ret=0;

	LL mum = 10;
	LL bmul=1;
	while(n>0)
	{   ret += (n%10)*bmul;
		n/=10;
		bmul*=base;
	}

	return ret;

}


LL numdivs[10];
void iscoinjam(int tofind)
{	
	int numfound=0;
	FO(i,0,17000)
	{
		ARR0(numdivs);
		bool found =true;
		FO(k,2,11)
		{	LL basenum = getbasenum(allpos[i],k);
			LL ntdiv = iscoinjamtest(basenum);
			if(ntdiv==basenum)
   				found =false;
   			numdivs[k-2] = ntdiv;
   		}

   		if(found)
   		{
   			numfound++;
   			cout<< allpos[i];
   			FO(k,0,9)
   					cout << " "<<numdivs[k];
   			
   			cout << endl;

   			if(numfound==tofind) break;
   		}
   		
   	}
}


void csolver(int caseno)
{
	int n,j;
	cin >> n >> j;

	cout<<"Case #"<<(caseno+1)<<":"<<endl;

	LL st = 1000000000000001;
	allpos[0] =st;
	nextnum(st,1);	
	iscoinjam(j);
}

void C()
{ int t;cin>>t;

  FO(j,0,t)
  {	
  	csolver(j);
  }

}

void dsolver(int caseno)
{	LL k,c,s; cin >> k >>c >>s;

	if(k>s)
		cout<<"Case #"<<(caseno+1)<<": IMPOSSIBLE"<<endl;
	else
	{	cout<<"Case #"<<(caseno+1)<<":";
		FO(j,0,s)
			cout << " " << (j+1);
		cout << endl;
	}
}

void D()
{
	int t;cin>>t;

  FO(j,0,t)
  {	
  	dsolver(j);
  }
}

int main()
{	
    ios::sync_with_stdio(false);
   	D();
   /*
	

  	*/

   	//int dd=0;
   	/*FO(k,2,1000)
   		if(k==iscoinjamtest(LL(k)) )
   		{ dd++;
   			cout << dd << " " << iscoinjamtest(LL(k)) << endl;
   		}
   	*/
   //	LL temp =1101;
   
    return 0;

}