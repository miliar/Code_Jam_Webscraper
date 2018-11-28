#include <iostream>
#include <vector>
#include <map>

using namespace std;





int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      string case_;
      cin >> case_;
      string result;

      for (int j=0;j<case_.size();j++)
	{
		if (result.size()<=0){
		   result = case_[j];
                }
		else
		{
		    if (case_[j] >= result [0])
		    {
			result = case_[j] + result;
		    }else
		    {
		    	result = result + case_[j]; 
 		    }
		}
	}
      
       cout << "Case #"<< i+1 <<":" << " " << result << endl;
    }     
}

   

