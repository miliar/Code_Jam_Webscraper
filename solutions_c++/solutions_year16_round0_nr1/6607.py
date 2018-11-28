
    #include <stdint.h>
    #include <iostream>
    #include<fstream>

    using namespace std;

    int return_b
    	(int64_t d)
    {
    	int b = 0;

    	while(d)
    	{
    		b |= (1 << (d % 10));
    		d /= 10;
    	}

    	return b;
    }

    int main()
    {
        ofstream outfile;
        ifstream infile;

        outfile.open("output.txt");
        infile.open("A-large.txt");
    	int n;

    	infile >> n;

    	const int target_b = (1 << 10) - 1;

    	for(int i = 1; i <= n; i++)
    	{
    		int64_t d;
    		int64_t d_accum = 0;

    		infile >> d;

    		if(d == 0)
    		{
    			outfile << "Case #" << i << ": INSOMNIA" << endl;
    			continue;
    		}

    		int b = 0;

    		while(true)
    		{
    			d_accum += d;

    			b |= return_b(d_accum);

    			if(b == target_b)
    				break;
    		}

    		outfile << "Case #" << i << ": " << d_accum << endl;
    	}

    	return 0;
    }
