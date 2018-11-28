#include <iostream>
using namespace std;

int main() {
	int t,j,cnt=0;
	char p[110],tmp;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    cnt=0;
	    cin>>p;
	    while(1)
	    {
	        j=0;
	        while(p[j+1]!=0 && p[j]==p[j+1])
	            j++;
	        if(p[j+1]==0)
	            break;
	        cnt++;
	        for(int k=0;k<=j/2;k++)
	        {
	            tmp=p[k];
	            p[k]=p[j-k];
	            p[j-k]=tmp;
	        }
	        for(int k=0;k<=j;k++)
	        {
	            if(p[k]=='+')
	                p[k]='-';
	            else
	               p[k]='+';
	        }
	    }
	    if(p[0]=='-')
	        cout<<"Case #"<<i<<": "<<(cnt+1)<<endl;
	    else
	        cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}