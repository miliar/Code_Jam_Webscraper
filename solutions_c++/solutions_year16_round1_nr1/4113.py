#include <iostream>
#include<deque>
#include<string.h>
#include<stdio.h>

using namespace std;

int main() {
	// your code goes here
	deque<char> dq;
	char s[101];
	int T,temp,i;
	cin>>T;
	for(int j=1;j<=T;j++)
	{
	    
         cin.ignore(256, '\n');
	    cin>>s;
	    temp=strlen(s);
	    dq.push_front(s[0]);
	    
	    for( i=1;i<temp;i++)
	    {
	        if(s[i]>=dq.at(0))
	        dq.push_front(s[i]);
	        else
	        dq.push_back(s[i]);
	    }
		cout<<"Case #"<<j<<": ";
	      for( i=0;i<temp;i++)
	    {
			cout<<dq[i];
	        
	    }
	    cout<<endl;
	    
		dq.erase (dq.begin(),dq.begin()+temp);
	}
	return 0;
}
