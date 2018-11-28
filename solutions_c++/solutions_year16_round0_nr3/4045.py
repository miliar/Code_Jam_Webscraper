#include <iostream>
#include <cmath>

long long int prime(long long int n0);

long long int func(int base_copy,long long int n0);

void add(long long int& n0);

int main()
{
	int t=0,a=1,a0=0;
	bool jamcoin=true;
	long long int n=0,j=0,number=0,divisor0[11]={};
	std::cin>>t;
	std::cin>>a0>>a0;
	std::cout<<"Case #1:\n";
	for(long long int i=100000000000000;number<=50;add(i))
	{
        n=(i*10)+1;
		jamcoin=true;
        for(int base=2;base<=10;++base)
        {
        	if( prime(func(base,n))==0 )
        	{
        		jamcoin=false;
        		break;
        	}
        	else
        	{
        		divisor0[base]=prime(func(base,n));
        	}
        }
        if(jamcoin==true)
        {
        	std::cout<<n<<" ";
        	for(int j=2;j<=10;++j)
        	{
        		std::cout<<divisor0[j]<<" ";
        	}
            std::cout<<"\n";
        	++number;
        }
        else
        {
        	;
        }
        if(number==50)
        {
            break;
        }
        else
        {
            ;
        }
        
	}
    return 0;
}

long long int prime(long long int n0)
{
    if(n0==2)
    {
        return 0;
    }
    else
    {
        if(n0%2==0) 
        {
            return 2;
        }
        else
        {
            for(long long int i=3;i<=std::pow(n0,0.5);i+=2)
            {
                if(n0%i==0)
                {
                    return i;
                }
                else
                {
                    ;
                }
            }
        }
        return 0;
    }
}

long long int func(int base_copy,long long int n0)
{
	long long int answer=0,a0=0;
	while(n0!=0)
	{
		answer+=((n0%10)*std::pow(base_copy,a0));
		n0/=10;
		++a0;
	}
	return answer;
}

void add(long long int& n0)
{
    int carry=0;
    long long int n0_copy=n0;
    if(n0%10==0)
    {
    	++n0;
    }
    else
    {
        n0=0;
        carry=1;
        n0_copy/=10;
    	for(int i=1;i<14;++i)
    	{
    		if((carry==1)&&((n0_copy%10)==1))
    		{
    		    carry=1;
    		}
    		else
    		{
    			n0+=((carry+(n0_copy%10))*(static_cast<long long int>(std::pow(10,i))));
                carry=0;
    		}
    		n0_copy/=10;
    	}
        n0+=(((n0_copy%10))*(static_cast<long long int>(std::pow(10,14))));;
    }
}