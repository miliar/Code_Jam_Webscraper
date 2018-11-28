#include <iostream>

using namespace std;

int main()
{
    int n,i,a,b;
    unsigned long x,buff,res;
    cin >> n;
    bool ciphers[10] = {false};
    bool done;
    for(i = 0; i < n; i++)
    {
	for(b = 0; b< 10;b++) ciphers[b] = false;
	cin >> x;
	if ( x == 0)
	{   
	    cout<<"Case #"<< i+1 <<": "<<"INSOMNIA"<<endl;
	    continue;
	}
	for(res = 1;;res++)
	{
	    buff = res*x;
	    while(buff > 0) 
	    {
		ciphers[buff % 10] = true;
		buff /= 10;	
	    }

	    done = true;
	    for(b = 0; b < 10;b++)
	    {
		if(ciphers[b] == false)
		{
		    done = false;
		    break;
		}
	    }

	    if ( done )
	    {
		break;
	    }
	}
	cout<<"Case #"<< i+1 <<": "<<x*res<<endl;

    
    }



}
