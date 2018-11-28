/*
 * Author: ambreen2006@gmail.com
 * 
 * */

#include <iostream>
#include <sstream>
#include <limits>
#include <map>

#include <utils/codejam_io.h>

using namespace std;

using quaternions_map = map<string,string>;

bool advance_target(string& target)
{
  if(target[0] == 'i')
  {
    target = "j";
    return true;
  }
  
  if(target[0] == 'j')
  {
    target = "k";
    return true;
  }
  
  if(target[0] == 'k')
  {
    // goal already met :) yay!
      return false;
  }
}

// returns yes if there is a minus sign
bool get_replacement_is_negative(string& evaluation_str,quaternions_map& qmap, string& replacement)
{
   replacement = qmap[evaluation_str];
   bool negative = false;
   
   if(  evaluation_str.compare("ii") == 0 || evaluation_str.compare("ik") == 0 
     || evaluation_str.compare("ji") == 0 || evaluation_str.compare("jj") == 0
     || evaluation_str.compare("kj") == 0 || evaluation_str.compare("kk") == 0
   )
   {
     negative = true;
   }
  return negative;
}


string run_test( int length_of_string, long repeatation, string& misspelling, quaternions_map& quaternions)
{
    string 	result = "YES";
    long 	rep_count = repeatation;
    string 	target = "i";
    int    	negative_count = 0;
    bool   	goal_met = false;
    string	full_str;
  
    
    if(length_of_string == 1)
    { 
	return "NO";
    }
    
    for(long i = 0; i < repeatation; i++)
    {
      full_str.append(misspelling);
    }
    
    long max = length_of_string * repeatation;
    string replacement = "";
    long index = 0;
    char pos_1, pos_2;
    int found = 0;
    
    while(index < (max+1) )
    {
        if(found == 3 && index >= max)
	  break;
	
	if(replacement.empty())
	{
	   if (index < max )
	   { 
	    pos_1 = full_str[index];
	    index++;
	   }
	}
	else
	{
	  pos_1 = replacement[0];
	}
	
	if( pos_1 == target[0] )
	{
	  if ((found+1) == 3 && index != max)
	  {
	    
	  }
	  else
	  {
	    advance_target(target);
	      
		replacement = "";
		found++;
		continue;     
	      
	  }
	  
	}
	
	if(!(index < max))
	    break;
	{
	    
	   pos_2 = full_str[index];
	   index++;
	
	
	stringstream ss;
	ss << pos_1 << pos_2;
	  
	string token;
	ss >> token;
	  
	if(get_replacement_is_negative(token,quaternions,replacement))
	{
	     negative_count++;
	}
	}
	
    }
    
   /*   int index = 0;
    
  
      string replacement;
      string modified_complete;
      char   pos_1, pos_2;
      bool   read_two = true;
      
      index = 0;
      long compared_num = 0;

      long max = length_of_string * repeatation;	
      
      while(compared_num < max)  {
	
	//cout << misspelling << " ";
	if(replacement.empty())
	{
	   index = compared_num%length_of_string;
	   pos_1 = misspelling[index];
	   compared_num++;
	}
	else
	{
	  pos_1 = replacement[0];
	}
	// check if the pos_1 matches target
	if(pos_1 == target[0])
	{
	    // since we found the target, lets looks for the next target
	    if(advance_target(target))
	    {
	      replacement = "";
	      continue;
	    }
	    else
	    {
	      goal_met = true;
	      if(compared_num == max)
		break;
	    }
	}
	
	index = compared_num%length_of_string;
	pos_2 = misspelling[index];
	compared_num++;
	
	stringstream ss;
	ss << pos_1 << pos_2;
	  
	string token;
	ss >> token;
	  
	if(get_replacement_is_negative(token,quaternions,replacement))
	{
	     negative_count++;
	} 


      }
	
*/
   
  // cout << "Negative Count " << negative_count << endl;
   
    if(negative_count % 2!=0)
    {
      return "NO";
    }
    
    if(found!=3)
    {
   //   cout << "Found " << found << " last used " << index << endl;
      return "NO";
    }
    return result;
}



void create_quaternions(quaternions_map& qmap)
{
    qmap["11"] =  "1";
    qmap["1i"] =  "i";
    qmap["1j"] =  "j";
    qmap["1k"] =  "k";
    
    qmap["i1"] =  "i";
    qmap["ii"] =  "1";
    qmap["ij"] =  "k";
    qmap["ik"] =  "j";
    
    qmap["j1"] =  "j";
    qmap["ji"] =  "k";
    qmap["jj"] =  "1";
    qmap["jk"] =  "i";
    
    qmap["k1"] =  "k";
    qmap["ki"] =  "j";
    qmap["kj"] =  "i";
    qmap["kk"] =  "1";
}


int main(int argc, char **argv)
{
    CJInputFile  		ifile("C-small-attempt2.in");
    //CJInputFile  		ifile;
    CJOutputFile 		ofile;
    int 	 		number_of_tests;
    quaternions_map 		quaternions;
    
    create_quaternions(quaternions);
    
    number_of_tests = ifile.getNumberOfTests();
    
    //string misspelling = "ji";
    //string result = run_test(2,6,misspelling,quaternions);
    //cout << "case 1 " << result << endl; 
    
   
    for(int i = 0; i < number_of_tests; i++)
    {
	 int L = ifile.nextIntegerToken();
	 long X = ifile.nextIntegerToken();
	 string misspelling = ifile.nextToken();
	 string result = run_test(L,X,misspelling,quaternions);
	 ofile.write_result<string>(result); 
	//cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}

