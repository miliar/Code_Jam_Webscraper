#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define SMALL
//#define LARGE

string operator*(std::string s, size_t count)
{
    	string ret;
	for(size_t i = 0; i < count; ++i)
    	{
        	ret = ret + s;
    	}
    	return ret;
}

int main()
{

	#ifdef SMALL
		freopen("C-small-attempt1.in","rt",stdin);
		freopen("C-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("C-large.in","rt",stdin);
		freopen("C-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	char mult[4][4] = { 'h' , 'i' , 'j' , 'k' , 'i' , 'h' , 'k' , 'j' , 'j' , 'k' , 'h' , 'i' , 'k' , 'j' , 'i' , 'h' };
	int sign[4][4] = { 1 , 1 , 1 , 1 , 1 , -1 , 1 , -1 , 1 , -1 , -1 , 1 , 1 , 1 , -1 , -1 };
	for(i=1;i<=t;i++)
	{
		int ans=0,l,x,r,c,j,k;
		string a;
		char b[]="ijk";
		char letter;
		int positive = 1;
		cin>>l>>x>>a;
		if(l == 1)
		{
			cout<<"Case #"<<i<<": NO"<<endl;
			continue;
		}	
		a = a*x;	
		k = 0;
		letter = 'h';	
		for(j = 0; j < a.size(); j++)
		{
			r = (int)letter - 104;
			if(j == a.size())
				c = 0;
			else						
				c = (int)a[j] - 104;
			letter = mult[r][c];
			positive = positive * sign[r][c];
			if(k<2 && letter==b[k] && positive==1)
			{
				k++;
				letter = 'h';
			}
		}
		if(k==2 && letter == 'k' && positive==1)
			ans=1;
		if(ans==1)
			cout<<"Case #"<<i<<": YES"<<endl;		
		else
			cout<<"Case #"<<i<<": NO"<<endl;
	}
	
	return 0;
}
