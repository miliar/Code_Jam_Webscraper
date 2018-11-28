#include <iostream>
#include<string.h>
using namespace std;

void checklast(char S[1000])
{   int n=strlen(S);
    int pointer = n;
    for(int i=n-1;i>=0;i--)
    {
        if(S[i]=='+')
         pointer--;
        else if(S[i]=='-')
         break;
        
    }
    S[pointer]='\0';
}
void rev(char S[1000])
{
    int n=strlen(S);
     for(int i=0;i<n/2;i++)
	            {
	                char t=S[i];
	                S[i]=S[n-i-1];
	                S[n-i-1]=t;
	            }
	            for(int i=0;i<n;i++)
	            {
	                if(S[i]=='+')
	                 S[i]='-';
	                else
	                 S[i]='+';
	            }
    
}
void change(char S[1000])
{
    int n=strlen(S);
    for(int i=0;i<n;i++)
    {
        if(S[i]=='+')
        S[i]='-';
        else
        break;
    }
}

int main() {
	int t;
	cin>>t;
	int q=t;
	while(t>0)
	{
	    int count=0;
	    char S[1000];
	    cin>>S;
	    checklast(S);
	    while(strlen(S)!=0)
	    {
	        checklast(S);
	        int n=strlen(S);
	        if(n==0)
	        break;
	        //cout<<"n="<<n<<endl;
	        if(S[0]=='-')
	        {
	           rev(S);
	            count++;
	        }
	        else
	        {
	            change(S);
	            count++;
	        }
	        //cout<<S<<endl;
	        //cout<<"count="<<count<<endl;
	        
	}
	cout<<"Case #"<<q-t+1<<": "<<count<<endl;
	t--;
	}
	return 0;
}
