#include <iostream>
#include <vector>
using namespace std;



int main() {
	int long no_of_testcases;
	int long no_of_pancakes;
	string rand_val;
	char sp = '+';
	char sn = '-';
	vector<string> input_set;
	std::cin>>no_of_testcases;
	for(int read_value_loop=0; read_value_loop<no_of_testcases; read_value_loop ++)
	{
	    int count = 0;
	    std::cin>>rand_val;
	    std::vector<char> rand_val_char(rand_val.begin(), rand_val.end());

	    no_of_pancakes=rand_val.length();
	    
	    for(int cake_no=no_of_pancakes -1; cake_no>=0; cake_no --)
        {
            if(rand_val_char[cake_no] ==sn)
            {
                int x = cake_no;
                for(int cake_x=0; cake_x<=x; cake_x++)
                {
                    if(rand_val_char[cake_x]==sp)
                        rand_val_char[cake_x]=sn;
                    else rand_val_char[cake_x]=sp;
                }
                count = count +1;
            }
        }
        cout<<"Case #"<<read_value_loop+1<<": "<<count<<'\n';
    }
	return 0;
}