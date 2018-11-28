#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>
#include <map>
#include <strstream>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <vector>
#include <math.h>

unsigned long long lookup[] ={ 1
,4
,9
,121
,484
,676
,10201
,12321
,14641
,40804
,44944
,69696
,94249
,698896
,1002001
,1234321
,4008004
,5221225
,6948496
,100020001
,102030201
,104060401
,121242121
,123454321
,125686521
,400080004
,404090404
,522808225
,617323716
,942060249
,10000200001
,10221412201
,12102420121
,12345654321
,40000800004
,637832238736
,1000002000001
,1002003002001
,1004006004001
,1020304030201
,1022325232201
,1024348434201
,1086078706801
,1210024200121
,1212225222121
,1214428244121
,1230127210321
,1232346432321
,1234567654321
,1615108015161
,4000008000004
,4004009004004
,4051154511504
,5265533355625
,9420645460249
,100000020000001
,100220141022001
,102012040210201
,102234363432201
,121000242000121
,121242363242121
,123212464212321
,123456787654321
,123862676268321
,144678292876441
,165551171155561
,400000080000004
,900075181570009
,4099923883299904
,10000000200000001
,10002000300020001
,10004000600040001
,10020210401202001
,10022212521222001
,10024214841242001
,10201020402010201
,10203040504030201
,10205060806050201
,10221432623412201
,10223454745432201
,12100002420000121
,12102202520220121
,12104402820440121
,12120030703002121
,12122232623222121
,12124434743442121
,12321024642012321
,12323244744232321
,12341234943214321
,12343456865434321
,12345678987654321
,40000000800000004
,40004000900040004
,94206450305460249
,1000000002000000001
,1000220014100220001
,1002003004003002001
,1002223236323222001
,1020100204020010201
,1020322416142230201
,1022123226223212201
,1022345658565432201
,1210000024200000121
,1210242036302420121
,1212203226223022121
,1212445458545442121
,1232100246420012321
,1232344458544432321
,1234323468643234321
,4000000008000000004
,4253436912196343524
,6158453974793548516,
0
};


bool hasPalndromeRoot(unsigned long long num )
{
  unsigned long long root = sqrt(num);
  if( num == 676 )
  {
    int a= 3;
  }
  std::string str = boost::lexical_cast<std::string>(root);
  for( int i = 0; i < str.length() / 2; i++ )
  {
    if( str[i] != str[str.length() - i-1] )
    {
      return false;
    }
  }
  
  return true;
}

unsigned int solveTestCase( const std::string& line )
{
    std::istringstream str(line);
    unsigned long long num1;
    unsigned long long num2;
    str >> num1;
    str >> num2;

    unsigned int num1Len = boost::lexical_cast<std::string>(num1).length();
    int num1Palindromes = 0;
    int index=0;
    while( lookup[index]!=0 && lookup[index] < num1 )
    {
      if( hasPalndromeRoot( lookup[index]) )
      {
	num1Palindromes++;
      }
      
      index++;
    }
    
    unsigned int num2Len = boost::lexical_cast<std::string>(num2).length();
    int num2Palindromes = 0;
    index = 0;
    while( lookup[index]!=0 && lookup[index] <= num2 )
    {
      if( hasPalndromeRoot( lookup[index]) )
      {
	num2Palindromes++;
      }
      
      index++;
    }
    
    if( num1Palindromes == num2Palindromes )
    {
      return 0;
    }
    
    return num2Palindromes - num1Palindromes;
}

int main(int argc, char **argv) {
    std::ifstream file( "input.txt" );
    if( file.good() )
    {
        char buff[255];
        file.getline( buff, sizeof(buff) );
        unsigned int numberOfTests = boost::lexical_cast<unsigned int>(buff);

        for( unsigned int i = 0; i < numberOfTests && file.good(); i++ )
        {
            file.getline(buff, sizeof( buff) );
            int result = solveTestCase(buff);
            std::cout << "Case #" << i+1 << ": " << result << std::endl;
        }
    }

    return 0;
}
