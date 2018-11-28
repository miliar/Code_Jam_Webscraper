#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stdint.h>

using namespace std;

#include <boost/foreach.hpp>
#include <boost/multiprecision/gmp.hpp>
#include <boost/unordered_set.hpp>
#include <boost/unordered_map.hpp>

using namespace boost;
using namespace multiprecision;


int main(int argc, char * argv[])
{
    int T, N;

	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
	    bool impossible = false;
	    cin >> N;
	    std::vector<char> letters;
	    std::vector<std::vector<int> > counts(N);
	    
	    for (int n = 0; n < N; n++)
	    {
	        
	        
	        string str;
	        cin >> str;
	        
	        char prev_letter = '\0';
	        int letters_count = 0;
	        
	        for (int c = 0; c < str.size(); c++)
	        {
	            if (str[c] != prev_letter)
	            {
	                letters_count++;
	                
	                counts[n].push_back(1);

	                if (letters.size() < letters_count)
	                {
	                    if (n != 0)
	                    {
	                        impossible = true;
	                        break;
	                    }
	                    
	                    letters.push_back(str[c]);
	                }
	                else
	                {
	                    // cout << letters[letters_count-1] << " " << str[c] << endl;
	                    if (letters[letters_count-1] != str[c])
	                    {
	                        impossible = true;
	                        break;
	                    }
	                }
	            }
	            else
	            {
	                counts[n][letters_count-1]++;
	            }
	            
	            prev_letter = str[c];
	        }
	        
	        if (letters_count < letters.size())
	        {
	            impossible = true;
	        }
	        
	        /*BOOST_FOREACH(char c, letters)
	        {
	            cerr << c << " ";
	        }
	        
	        cerr << endl;
	        
	        BOOST_FOREACH(const vector<int> & v, counts)
	        {
	            BOOST_FOREACH(int count, v)
	            {
	                cerr << count << " ";
	            }
	            cerr << endl;
	        }
	        
	        cerr << endl;*/
	        
	        
	        if (impossible)
	        {
	            break;
	        }
	    }
	    
	    int total_sum = 0;
	    if (!impossible)
	    {
	        for (int l = 0; l < letters.size(); l++)
	        {
	            int min = INT_MAX, max = INT_MIN;
	            for (int n = 0; n < N; n++)
	            {
	                if (counts[n][l] < min)
	                {
	                    min = counts[n][l];
	                }
	                
	                if (counts[n][l] > max)
	                {
	                    max = counts[n][l];
	                }
	            }
	            
	            cerr << min << " " << max << std::endl;
	            
	            int min_sum = INT_MAX;
	            for (int val = min; val < max+1; val++)
	            {
	                int sum = 0;
	                for (int n = 0; n < N; n++)
	                {
	                    sum += abs(counts[n][l]-val);
	                }
	                
	                if (sum < min_sum)
	                {
	                    min_sum = sum;
	                }
	            }
	            
	            total_sum += min_sum;
	        }
	        
	    }
	    
	    if (impossible)
	    {
	        cout << "Case #" << (t+1) << ": Fegla Won" << endl;
	    }
	    else
	    {
	        cout << "Case #" << (t+1) << ": " << total_sum << endl;
	    }
	}
    return 0;
}
