#include<bits/stdc++.h>
using namespace std;
int main()
{
	

    int t,g=1;
    scanf("%d ",&t);
    while(t--)
    {
    	char s[101];
    	cin>>s;
    	//cout<<s<<endl;
    	int l=strlen(s);
    	int index=l-1,count=0;
    	while(1)
    	{
          if(index<0 || (index==0 && s[0]=='+' ) )
          	break;
          if(s[index]=='-')
          	{
          		while(s[index]=='-')
          		index--;
          	    count++;
          	    for(int y=index;y>=0;y--)
		         { 
			      	if(s[y]=='-')
			      		s[y]='+';
			      	else
			      		s[y]='-';
		          }
          	}
             else
	          {
			   index--;   
	          }   
    	}
    	cout<<"Case #"<<g<<": "<<count<<endl;
    	g++;
    }
	return 0;
}