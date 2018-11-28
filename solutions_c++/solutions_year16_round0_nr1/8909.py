#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.txt");
	int t;
	input>>t;
	for(int i=0;i<t;++i)
	{
        long long int k=1,n,number;
        int digit;
        input>>n;
        int arr[10]={0};
        int total_left=10;
        if(n==0)
            output<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
        else
        {
            while(total_left!=0)
            {
                number=k*n;
                while(number>0)
                {
                    digit=number%10;
                    if(arr[digit]==0)
                    {
                        ++arr[digit];
                        --total_left;
                    }
                    number/=10;
                }
                k++;
            }
            output<<"Case #"<<(i+1)<<": "<<((k-1)*n)<<endl;
        }
	}
    return 0;
}

