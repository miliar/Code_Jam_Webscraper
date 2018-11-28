#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

map <string, int> visited_;


char switch_char (char to_be_switched)
{
	if (to_be_switched == '+')
	   return '-';
	else
           return '+';
}

string flip_top_N (string original, unsigned int top_N)
{
    string copy = original;
    //cout << "===" << copy << endl;
    for (unsigned int n = 0; n < top_N/2; n++)   
    {
	char auxiliary = copy [n];	
	copy [n] = copy [top_N - 1 - n];
        copy [top_N - 1 -n] = auxiliary; 
    }

    for (unsigned int n1 = 0;n1 < top_N;n1++)
    {
	copy[n1] = switch_char(copy[n1]);
    }	
    //cout << "====" << copy <<endl;
    return copy;	
}

string build_key (string pile, unsigned int j)
{ 
	stringstream ss;
	ss << pile << ";" << j;
	return ss.str();
} 

int search_algorithm (string pile, unsigned int last_j = 0)
{
	//cout << "->" << pile << ";" << last_j << endl;	
	unsigned int i = 0;	
	for (; i< pile.size() && pile[i]=='+';i++);
	if (i == pile.size()) return 0;
	unsigned int minimum = -1;
	
	if (visited_.find (build_key(pile, last_j)) != visited_.end()) return visited_.find (build_key(pile, last_j))->second; 

        visited_.insert(pair<string, int>(build_key(pile, last_j), -1));
        
	for (unsigned int j = 1; j <= pile.size();j++)
	{
	    if (j != last_j)
	    {		
		string flipped = flip_top_N(pile, j);
	        if (flipped != pile)
                { 
                	unsigned int result = search_algorithm (flipped, j);
			if (result != -1)			
			     result ++;	        
			if (minimum == -1)
			{
		    	   minimum = result;	
                	}else
			{
		    	    if (result < minimum) minimum = result;
			}
		}
	    }
        }
        visited_ [build_key(pile, last_j)] = minimum;
	return minimum;
}    

string reduce_string (string to_reduce)
{
    stringstream ss;
    ss << to_reduce[0];

    for (unsigned int j = 1; j < to_reduce.size(); j++)
    {
        if (to_reduce[j] != to_reduce[j-1])
	{
	    ss << to_reduce[j];	
	}
    }	
   
    return ss.str();
}

int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      string case_;
      cin >> case_;
	visited_.clear();      
      
      unsigned int result = search_algorithm (reduce_string (case_));
      cout << "Case #"<< i+1 <<":" << " " << result << endl;
   }
}
