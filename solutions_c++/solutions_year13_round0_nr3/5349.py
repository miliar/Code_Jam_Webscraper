#include<iostream>
#include<cstdlib>
#include<math.h>
#include<string.h>
#include <sstream>
using namespace std;

#define mod 1000000007
typedef long long ll ;


int main()
{
freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.in", "w", stdout);
    int n;
    cin>>n;
    
    for(int t=1;t<=n;t++)
    {
    	int a,b;
    	
    	cin>>a>>b;
    	int count=0;
		for(int i=a;i<=b;i++)
		{
			double root = sqrt(i);
			int flag=1;
			if(fmod(root,1)== 0)
			{
			//cout<<i <<" " ;
		 		string s;
				stringstream con1,con2; 
				con1 << i;
				s = con1.str();
				
				
				int len = s.length();
				
				for(int j=0;j<len/2;j++)
				{
					if(s[j] != s[len-j-1] ) {
						flag=0;
						break;
					}
				}
				//cout<<"flag = "<< flag;
				if(flag==1)
				{
					con2 << root;
				s = con2.str();
				int len = s.length();
				
				for(int j=0;j<len/2;j++)
				{
					if(s[j] != s[len-j-1] ) {
						flag=0;
						break;
					}
				}
				}
				//cout<<"flag = "<< flag<<endl;
				if(flag==1) count++;
				
		}

	}
    	
    		cout<<"Case #"<<t<<": "<<count<<endl;
   			 
    }
    return 0;
    }
