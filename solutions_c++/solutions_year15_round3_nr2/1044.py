//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define PB push_back
#define SZ size
#define MP make_pair

//cout<<"Case #"<<qw<<": ";

string keys, target;
int k, l, s;
int toadd;
int minbananas;

std::vector<string> all;

void foo()
{
	int i=0, j;

	fl(i,1,l)
	{
		string f = target.substr(0,i);
		string b = target.substr(l-i,i);
		//cout<<f<<" "<<b; nline;
		if(f!=b)
			break;
	}

	toadd=i-1;
	toadd = l-toadd;
}

void genall(int ind, string str1)
{
	//cout<<ind<<" "<<str1; nline;
	if(ind==s)
	{
		all.PB(str1);
		return;
	}

	int i, j;

	fl(i,0,k)
	{
		string temp = str1;
		temp+=keys[i];
		genall(ind+1, temp);
		//genall(ind,str1);
	}

	return;
}

int main()
{
	freopen("in2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
	int i, j, cases, qw;
	

	cin>>cases;
	fl(qw,1,cases+1)
	{
		cout<<"Case #"<<qw<<": ";
		all.clear();
		cin>>k>>l>>s;
		cin>>keys>>target;
		foo();
		//toadd = l-;
		//cout<<toadd;
		//cout<<toadd<<" ";
		int temp = s-l;
		temp = temp/toadd;


		minbananas = temp+1;

		//cout<<"min = "<<minbananas; nline;
		int f = 0;
		fl(i,0,l)
		{
			f=0;
			fl(j,0,k)
			{

				if(keys[j]==target[i])
				{
					f=1;
					break;
				}
			}
			if(f==0)
			{
				break;
			}
		}

		if(!f)
		{
			cout<<"0.0";
			nline;
			continue;
		}


		int total = 0;

		genall(0,"");
		//nline;
		int inlimit = all.SZ();

		minbananas = 0;

		fl(i,0,inlimit)
		{
			string test = all[i];
			//cout<<test;
			int limit = test.SZ();
			int count = 0;
			fl(j,0,limit-l+1)
			{
				//cout<<j<<" ";
				if(test.substr(j,l)==target )
					count++; 
			}
			//cout<<test<<" "<<count; nline;
			//if(minbananas-count < 0)
			//	cout<<"here";
			minbananas = max(minbananas, count);
		}

		fl(i,0,inlimit)
		{
			string test = all[i];
			//cout<<test;
			int limit = test.SZ();
			int count = 0;
			fl(j,0,limit-l+1)
			{
				//cout<<j<<" ";
				if(test.substr(j,l)==target )
					count++; 
			}
			//cout<<test<<" "<<count; nline;
			//if(minbananas-count < 0)
			//	cout<<"here";
			total+=(minbananas - count);
		}
		//nline;
		//cout<<total<<" "<<all.SZ()<<" ";
		
		printf("%0.9lf", 1.0*((1.0*total)/(1.0*all.SZ())));
		nline;
		

		//cout<<all.SZ();
	}

	
	
	return 0;
}


/*
	Powered by Buggy plugin
*/