#include<bits/stdc++.h>
using namespace std;

int main() 
{
    freopen("A.in", "r", stdin);
    freopen("out", "w", stdout);	
    int tt,qq;
    cin>>tt;
    string a;
    for(qq=1;qq<=tt;qq++)
    {
        cin>>a;
        int c=0,i;
        size_t x = a.find_last_of("-");
        while(x>=0 && x<=100)
        {
            for(i=x;i>=0;i--)
            {
                if(a[i]=='-')
                    a[i] = '+';
                else
                    a[i] = '-';
                    
            }
            c++;
            x = a.find_last_of("-");
            
        }
        cout<<"Case #"<<qq<<": "<<c<<endl;
    }
    	
	return 0;
}
