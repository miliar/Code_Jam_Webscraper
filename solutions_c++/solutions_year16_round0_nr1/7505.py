#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

int t,g=1;
cin >> t;
while(t--)
{
	long long int x,count=1;
    cin >> x;
    string s;
    int y[10]={0};
    long long int p=2;
    long long int z = x;
    
    if(x==0)
        cout << "Case #"<<g++<<": "<<"INSOMNIA"<<endl;
    else
    {
    while(count--)
    {
    	s = to_string(z);
    	for(int i = 0;i < s.length();i++)
    	{
        	if(s[i]=='0')
        		y[0]=1;
        	if(s[i]=='1')
        		y[1]=1;
       		if(s[i]=='2')
        		y[2]=1;
        	if(s[i]=='3')
        		y[3]=1;
        	if(s[i]=='4')
        		y[4]=1;
        	if(s[i]=='5')
        		y[5]=1;
        	if(s[i]=='6')
        		y[6]=1;
        	if(s[i]=='7')
        		y[7]=1;
        	if(s[i]=='8')
        		y[8]=1;
        	if(s[i]=='9')
        		y[9]=1;
    	}
    	for(int i = 0;i < 10;i++)
    		{
    			if(y[i]==0)
    				count=1;
    		}
    	if(count==1)
    		z = p*x;
        p++;
    }
    
    cout << "Case #"<<g++<<": "<<z<<endl;
  }
}
    return 0;
}