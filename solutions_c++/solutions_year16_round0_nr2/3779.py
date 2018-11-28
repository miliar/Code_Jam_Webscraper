#define _USE_MATH_DEFINES
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

bool check(char S[],int n)
{
	for(int i=0;i<n;i++)
		if(S[i]!='+')
			return false;
	return true;
}

bool flip(char S[], int n)
{
	int i;
	bool x=false;
	for(i=0;i<n;i++)
	{
		x=true;
		if(S[i]=='+')
			S[i]='-';
		else
			S[i]='+';
	}
	for(i=0;i<n/2;i++)
	{
		char temp=S[i];
		S[i]=S[n-i-1];
		S[n-i-1]=temp;
	}
	return x;
}

int main()
{
    unsigned int t,i,n;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    	char S[101];
    	cin>>S;
    	n=0;
    	cout<<"Case #"<<i<<": ";
    	while(!check(S,strlen(S)))
    	{
    			int j,k;
    			for(j=0;j<strlen(S);j++)
    			{
    				if(S[j]!='+')
    					break;
    			}
    			if(flip(S,j))
    			    n++;
    			for(k=strlen(S)-1;k>=0;k--)
    			{
    				if(S[k]!='+')
    					break;
    			}
    			if(flip(S,k+1))
    			    n++;
    	}
    	cout<<n<<endl;
    }
    return 0;
}
