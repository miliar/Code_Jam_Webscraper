#include<iostream>
#include<fstream>
#include <vector>
#include <string>

using namespace std;

#define MAGIC 11

bool isValidNum(vector<int> res, int n)
{
	int sum=res[0];
	for(int i=1;i<n;++i)
	{
		if(i&1)
		{
			sum-=res[i];
		}else
		{
			sum+=res[i];
		}
	}
	if(sum % MAGIC == 0)
		return true;
		
	return false;
}

int main ()
{
    ifstream ifile("C-large.in");
    ofstream ofile;
    ofile.open("C-large.out");
    long long t, cases = 0, n, j;
    string divisors = " 3 2 5 2 7 2 9 2 11";
    ifile>>t;
    bool flag;
    while(t--)
    {
    	flag  = false;
        ifile>>n>>j;
        vector<int> res(n, 0);
        res[0] = res[n - 1]  = 1;
        ofile<<"Case #"<<++cases<<": \n";
        for(int i = 0; i < j;)
        {
        	if(isValidNum(res, n))
			{
				for(int m=0; m < n; ++m)
					ofile<<res[m];
				ofile<<divisors<<endl;
				++i;
				if(i==j){
					flag=true;
					break;
				}
			}
			if(flag == true)
				break;
				
			for(int k=1; k< n-2; ++k)
			{
				res[k] = 1;
				for(int l = k+1; l < n-1; ++l)
				{
					res[l]=1;
					if(isValidNum(res, n))
					{
						for(int m=0; m < n; ++m)
							ofile<<res[m];
						ofile<<divisors<<endl;
						++i;
						if(i==j){
							flag=true;
							break;
						}
					}
					res[l]=0;
				}
				if(flag == true)
					break;
					
				res[k]=0;
			}
			if(flag == true)
				break;
			
			for(int k=1;k < n-4; ++k)
			{
				res[k]=1;
				for(int l=k+1;l < n-3; ++l)
				{
					res[l] = res[l+1] = res[l+2] = 1;
					if(isValidNum(res, n))
					{
						for(int m=0; m < n; ++m)
							ofile<<res[m];
						ofile<<divisors<<endl;
						++i;
						if(i==j){
							flag=true;
							break;
						}
					}
					res[l] = res[l+1] = res[l+2] = 0;
				}
				if(flag == true)
					break;
					
				res[k]=0;
			}
			if(flag)
				break;
			
			for(int k = 1; k < n-6; ++k)
			{
				res[k] = 1;
				for(int l = k+1; l < n-5; ++l)
				{
					res[l] = res[l+1] = res[l+2] = res[l+3] = res[l+4] = 1;
					if(isValidNum(res, n))
					{
						for(int m=0; m < n; ++m)
							ofile<<res[m];
						ofile<<divisors<<endl;
						++i;
						if(i==j){
							flag=true;
							break;
						}
					}
					res[l] = res[l+1] = res[l+2] = res[l+3] = res[l+4] = 0;
				}
				if(flag == true)
					break;
					
				res[k]=0;
			}
			if(flag)
				break;
		}
	}
	return 0;
}

