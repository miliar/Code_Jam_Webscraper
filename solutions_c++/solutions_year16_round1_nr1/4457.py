    #include <bits/stdc++.h>
    using namespace std;
     
    int main() {
    	// your code goes here
    int t;
    cin>>t;
    int c=1;
    while(t--)
    {
    	char s[1000];
    	cin>>s;
    	int len=strlen(s);	
    	for(int i=1;i<len;i++)
    	{	if(s[i]>=s[0]) {	
    		char t=s[i];	
    		for(int j=i-1;j>=0;j--) s[j+1]=s[j]; 
    		s[0]=t;	
    		}
    	}
    	cout<<"Case #"<<c<<": "<<s;
    	c++;
    	cout<<endl;
    }
    	return 0;
    }