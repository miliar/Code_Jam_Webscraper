#include<iostream>
#include<map>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for( int q = 0; q<t; q++ )
	{
		string s;
		cin>>s;
		char arr[101];
		arr[0] = s[0];
		int len = s.size();
		int ptr = 0;
		int ans = 0;			
		for( int i=1; i<len; i++)
		{
			if( arr[ptr] != s[i] )
			{
				arr[++ptr] = s[i];
			}
		}		
		arr[++ptr] = '\0';
		//cout<<arr<<" "<<ptr;
		//trim +s from back	
		int j;	
		for( j = ptr; j>0; j--)
		{
			if(arr[j-1]!='+') 
			{
			//	j--;			
				break;
			}
			else
			arr[j-1] = '\0';
		}
		if(j==0) ans = 0; //all +s
		else		
		/*if(j==1 && arr[0] == '-') ans = 1;
		else		
		if( arr[0] == '-') ans = j;
		else
			ans =  
		*/
		ans = j;
		cout<<"Case #"<<q+1<<": "<<ans<<"\n";
	}
}
