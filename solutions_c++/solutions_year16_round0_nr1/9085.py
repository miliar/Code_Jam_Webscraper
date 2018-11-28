#include <iostream>
#include <vector>
using namespace std;

int main() {
	
	int long flag[2][10]; 
	
	
	int long no_of_testcases;
	int long rand_val;
	vector<int> random_number;
	vector<int> output_number;
	std::cin>>no_of_testcases;
	for(int read_value_loop=0; read_value_loop<no_of_testcases; read_value_loop ++)
	{
	    std::cin>>rand_val;
	    random_number.push_back(rand_val);
        for (int x=0; x<10; x++)
    	{
    	    flag[0][x]=x+1;
    	    flag[0][9]=0;
    	    flag[1][x]=0;
    	}
        if(random_number[read_value_loop]==0)
        {
            output_number.push_back(0);
    	    cout<<"Case #"<<read_value_loop+1<<": "<<"INSOMNIA"<<'\n';

            continue;
        }
        int multiple = 1;
        int sum=0;
        int a = random_number[read_value_loop];
	    while(sum!=10)
	    {
	        while(a>=1)
	        {
                sum = 0;
	            for(int j=0; j<10; j++)
	            {
                    if(flag[0][j]==(a%10))
                        flag[1][j]=1;
                    sum = sum + flag[1][j];
	            }
                if(sum==10) 
                {
                    output_number.push_back(random_number[read_value_loop]*multiple);
                    break;
                }
                if(sum==10) break;
                a=a/10;
            }
            multiple++;
            a=random_number[read_value_loop]*multiple;
	    }
	    cout<<"Case #"<<read_value_loop+1<<": "<<output_number[read_value_loop]<<'\n';

    }
	return 0;
}