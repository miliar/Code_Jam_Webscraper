#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <windows.h>
#include <iostream>
#include <string>

using namespace std;

void main()
{
	int T = 0;
    int startTime = 0;

	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");

	in >> T;

	for(int i=0; i<T; ++i)
	{
        startTime = GetTickCount();

        int stringsCount;

        

        in >> stringsCount;

        vector<string> v(stringsCount);

        getline(in,string());

        for(int i=0; i<stringsCount; i++)
        {
            getline(in,v[i]);
        }

        int solve = 0;

        while(v[0].size() != 0)
        {
            char s = v[0][0];

            vector<int> chars(stringsCount);

            for(int j=0; j<stringsCount; j++)
            {
                int k =0;
                if(v[j].size() != 0)
                    while(v[j][k] == s)
                    {                    
                        k++;

                        if(k >= v[j].size())
                            break;
                    }

                v[j] = v[j].substr(k,v[j].size()-k);

                chars[j] = k;
            }

            sort(chars.begin(), chars.end());

            int min = chars[stringsCount-1];

            if(chars[0] == 0)
            {
                solve = -1;
                break;
            }

            for(int j=chars[0]; j<=chars[stringsCount-1];j++)
            {
                int sum = 0;
                for(int k=0; k<stringsCount; k++)
                    sum += abs(chars[k] - j);

                if(sum < min)
                    min = sum;
            }

            solve += min;
        }

        for(int j=0; j<stringsCount; j++)
            if(v[j].size()!=0)
            {
                solve = -1;
                break;
            }
				

        if(solve == -1)
		    out << "Case #" << i+1 << ": " << "Fegla Won";
        else
            out << "Case #" << i+1 << ": " << solve;
		out << endl;


        cout << "Case #" << i+1 << ", time(ms) =  " << GetTickCount() - startTime << endl;
	}
}