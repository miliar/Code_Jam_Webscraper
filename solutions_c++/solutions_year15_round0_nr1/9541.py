/*
   It's opening night at the opera, and your friend is the prima donna (the lead female singer). You will not be in the audience, but you want to make sure she receives a standing ovation -- with every audience member standing up and clapping their hands for her.

   Initially, the entire audience is seated. Everyone in the audience has a shyness level. An audience member with shyness level Si will wait until at least Si other audience members have already stood up to clap, and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing and clapping.

   You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the prima donna to be in the audience to ensure that everyone in the crowd stands up and claps in the end. Each of these friends may have any shyness value that you wish, not necessarily the same. What is the minimum number of friends that you need to invite to guarantee a standing ovation?
   Input

   The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1 single digits. The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness level k. For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially always be between 0 and 9 people with each shyness level.

   The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.

   Output

   For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.

   Limits

   1 ≤ T ≤ 100.
   Small dataset

   0 ≤ Smax ≤ 6.

   Large dataset

   0 ≤ Smax ≤ 1000.

   Sample


   Input 

   4
   4 11111
   1 09
   5 110011
   0 1

   Output 
   Case #1: 0
   Case #2: 1
   Case #3: 2
   Case #4: 0
   In Case #1, the audience will eventually produce a standing ovation on its own, without you needing to add anyone -- first the audience member with Si = 0 will stand up, then the audience member with Si = 1 will stand up, etc.

   In Case #2, a friend with Si = 0 must be invited, but that is enough to get the entire audience to stand up.

   In Case #3, one optimal solution is to add two audience members with Si = 2.

   In Case #4, there is only one audience member and he will stand up immediately. No friends need to be invited.
 */

#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
using namespace std;

static const int MAX_LINE_SIZE = 1024;
static const int MAX_SHYNESS_LEVEL_SMALL = 6;
static const int MAX_SHYNESS_LEVEL_LARGE = 1000;
static const int MAX_NUM_TESTS = 100;

int main(int argc, char* argv[])
{
  if (argc != 2)
    return -1;

  string filename(argv[1]);
  FILE* inp = fopen(filename.c_str(), "r");
  if (inp == NULL) //file not found
    return -2;  

  int linenum = 0;
  unsigned int numTests = 0;
  char input_line[MAX_LINE_SIZE];
  while(fgets(input_line, MAX_LINE_SIZE, inp) != NULL &&
      linenum <= numTests)
  {
    if (linenum++ == 0)
    {
      numTests = strtol(input_line, NULL, 10);
      if (numTests > MAX_NUM_TESTS)
        return -3;
      continue;
    }
    string test(input_line);

    size_t space_pos = test.find_first_of(' ');
    unsigned s_max = strtol(test.substr(0,space_pos).c_str(), NULL, 10);
    string count_string = test.substr(space_pos+1);
    
    if (s_max > MAX_SHYNESS_LEVEL_LARGE)
      return -4;

    //unsigned count_audience[MAX_SHYNESS_LEVEL_LARGE+1] = {0};
    unsigned sum_shyness_level[MAX_SHYNESS_LEVEL_LARGE+1] = {0};
    int need_friends = 0;

    for (int i = 0; i <= s_max; i++)
    {
      char c = count_string[i];
      if (c < '0' || c > '9')
        return -5;
      
      if (i == 0) 
      {
        sum_shyness_level[i] = c - '0';
        continue;
      }

      if (c == '0')  //no members at this audience level
      {
        sum_shyness_level[i] = sum_shyness_level[i-1];
        continue;
      }
      
      if (sum_shyness_level[i-1] < i) //less than 'i' people standing at this point
      {
        int new_friends =  i - sum_shyness_level[i-1];
        sum_shyness_level[i] = sum_shyness_level[i-1] + new_friends + (c - '0');  
        need_friends += new_friends;
      }
      else
      {
        sum_shyness_level[i] = sum_shyness_level[i-1] + (c - '0');
      }
    }

    cout << "Case #" << linenum - 1 << ": " << need_friends << endl;  
  }

  fclose(inp);

  return 0;
}
