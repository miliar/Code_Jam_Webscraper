#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

const char *vinit[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int ispresent[10];
string text;

int search_word (int index, string word)
{
	int total = 0;
	string text_copy = text;
	for (;;){
	for (int i = 0; i < word.size(); i++)
	{
		size_t position = text_copy.find (word[i]); 
		if (position == string::npos)
			return total;
		else
			text_copy.erase(position, 1);
		
	} 
	ispresent [index]++;
	total+= word.size();
	text = text_copy;
	}
}

string pretty_print (){
	stringstream stream_;
	int total = 0;
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < ispresent[i];j++)
		{
			stream_ << i;
		}
	}
	return stream_.str();
}


int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      string case_;
      cin >> case_;
	  
	  bool valid = false;
	  int initial_index = 0;
		
	  while (valid == false)
	  {
		int total=0;
	    text = case_;
	  
		for (int j = 0;j < 10;j++)
		{
		    ispresent [(j+ initial_index)%10] = 0;
	        total+=search_word ((j+ initial_index)%10, vinit[(j+ initial_index)%10]);
	    }
	    
		if (total == case_.size())
		{
			valid = true;
		}else
		{
			initial_index++;
		}
	  }
	  
	  cout << "Case #"<< i+1 <<":" << " " << pretty_print() << endl;
	}
      
    
         
}

   

