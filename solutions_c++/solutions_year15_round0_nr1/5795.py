#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
using namespace std;

int main() {
    int t,o=1;
    cin>>t;
    while(t--)
    {
    	int s,c=0,i,t=0;
        char b[1001];
        cin>>s;
        cin>>b;

        for(i=0;i<=s;i++)
        {
            if(t<i)
            {
                c+=(i-t);
                
                t+=(b[i]-'0')+(i-t);
            }
            else if(t>=i)
                t+=(b[i]-'0');

        }

    	cout<<"Case #"<<o<<": "<<c<<endl;
    	
o++;
    }
    
return 0;         
}
