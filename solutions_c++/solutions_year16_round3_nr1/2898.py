#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    
    int t,a,b,c,i,j,count=1,n;
    a=b=c=0;
    cin>>t;
    while(t--)
    {
    	cout<<"Case #"<<count<<": ";
    	count++;
    	cin>>n;
    	if(n==2)
    	{
    		cin>>a;
    		cin>>b;
    		while(a>0 && b>0)
    		{
    			cout<<"AB"<<" ";
    			a--;b--;
    		}
    		while(a>0)
    			{
    				cout<<"A"<<" ";
    				a--;
    			}
    		while(b>0)
    		{
    			cout<<"B"<<" ";
    			b--;
    		}
    		cout<<endl;
    	}
    	if(n==3)
    	{
    		cin>>a;
    		cin>>b;
    		cin>>c;
    		if(a>b)
    		{
    			if(b>c)
    			{
    				while(a>c && b>c)
    				{
    					cout<<"AB"<<" ";
    					b--;a--;
    				}
    				while(a>c)
	    			{
	    				cout<<"A"<<" ";
	    				a--;
	    			}
		    		while(b>c)
		    		{
		    			cout<<"B"<<" ";
		    			b--;
		    		}

		    		while(c>0)
		    		{
		    			cout<<"C"<<" ";
		    			c--;
		    		}

		    		while(a>0 && b>0)
		    		{
		    			cout<<"AB"<<" ";
		    			a--;b--;
		    		}

		    		cout<<endl;

    			}
    		
    			else
    			{
    				while(a>b && b<c)
    				{
    					cout<<"AC"<<" ";
    					c--;a--;
    				}
    				while(a>b)
	    			{
	    				cout<<"A"<<" ";
	    				a--;
	    			}
		    		while(b<c)
		    		{
		    			cout<<"C"<<" ";
		    			c--;
		    		}

		    		while(c>0)
		    		{
		    			cout<<"C"<<" ";
		    			c--;
		    		}

		    		while(a>0 && b>0)
		    		{
		    			cout<<"AB"<<" ";
		    			a--;b--;
		    		}

		    		cout<<endl;
    			}
    		}

    		else
    		{
    			if(a>c)
    			{
    				while(a>c && b>c)
    				{
    					cout<<"AB"<<" ";
    					b--;a--;
    				}
    				while(a>c)
	    			{
	    				cout<<"A"<<" ";
	    				a--;
	    			}
		    		while(b>c)
		    		{
		    			cout<<"B"<<" ";
		    			b--;
		    		}

		    		while(c>0)
		    		{
		    			cout<<"C"<<" ";
		    			c--;
		    		}

		    		while(a>0 && b>0)
		    		{
		    			cout<<"AB"<<" ";
		    			a--;b--;
		    		}

		    		cout<<endl;

    			}
    			else
    			{
    				while(a<c && b>a)
    				{
    					cout<<"CB"<<" ";
    					b--;c--;
    				}
    				while(a<c)
	    			{
	    				cout<<"C"<<" ";
	    				c--;
	    			}
		    		while(b>a)
		    		{
		    			cout<<"B"<<" ";
		    			b--;
		    		}

		    		while(c>0)
		    		{
		    			cout<<"C"<<" ";
		    			c--;
		    		}

		    		while(a>0 && b>0)
		    		{
		    			cout<<"AB"<<" ";
		    			a--;b--;
		    		}

		    	

		    		cout<<endl;
    			}
    		}
    	}
    }
    return 0;
}