#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

bool digits[10];
int c;
int c_t;

bool processNumber(int n)
{
	
    int i = 1;
    bool toReturn = false;
    int next_digit;
    int next_pow;
    
    do
    {    	
    	next_pow = ((int)pow(10.0, i));    	    	
        next_digit = (n % next_pow) / (next_pow / 10);        
        if(!digits[next_digit])
        {
            c--;
            digits[next_digit] = true;
            toReturn = true;
        }
        
        i++;
    }while(next_pow<=n);
    
    return toReturn;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int t,n,i_m,t_case;
    cin>>t;
    t_case = 1;
    while(t_case <= t)
    {
        cin>>n;
        c = 10;
        c_t = 0;
        i_m = 1;
        for(int i=0; i<10; i++)
        {
            digits[i] = false;
        }
        while(c_t <= 100 && c > 0)
        {
            if(!processNumber(i_m * n))
            {
                c_t++;
            }
            else
            {
                c_t = 0;
            }
            i_m++;
        }
        cout<<"Case #"<<t_case<<": ";
        
        if(c > 0)
        {
            cout<<"INSOMNIA";
        }
        else
        {
            cout<<(n*(i_m-1));
        }
        cout<<endl;
        t_case++;
    }

}
