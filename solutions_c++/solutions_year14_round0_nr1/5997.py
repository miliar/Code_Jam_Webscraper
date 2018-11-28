#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <ios>
#include <vector>

/*
 * 
 */

/*
 * Input:
 * T : test cases
 * int : answer to first question
 * a11 a12 a13 a14  <---- The cards, 4x4 array.
 * a21 a22 a23 a24
 * a31 a32 a33 a34
 * a41 a42 a43 a44
 * answer to second question
 * b11 b12 b13 b14  <---- The cards, 4x4 array (different to the other one)
 * b21 b22 b23 b24
 * b31 b32 b33 b34
 * b41 b42 b43 b44
 * 
 * Output:
 * Case #t: y
 * y = Card that the volunteer choosed (if unique), if more than one card "Bad magician!", and if there are no card consistent with the answers, 
 *     should be "Volunteer cheated!"
 * 
 * Limits: 
 * T<=100
 * answer between 1 and 4
 * Numbers unique in the array (1 to 16).
 * 
 * In order for this to work, the magician has to put each card of the first answer, on a *different* row, if the magician put two cards of the original answer
 * on the same row on the second arrangement, it is a bad magician. 
 * 
 * A player can only be detected to be cheating if the magician is bad too..... sigh.... Because otherwise, there will always be a unique answer (even if she cheats).
 * 
 * Then, we first check for a "bad magician", once in that case, we check the second answer, if it points to a row where there are no card of the first answer
 * row: she is cheating.
 * 
 * Basically, read the file, and take *only* the row from the first answer.
 * 
 * Next, take the "second answer" row of the second array, and compare each member to the original row.
 * 
 * If we have a single card matching: that have to be the answer.  If we have more than one card matching, we have a bad magician.
 * If we have no cards matching, we have a cheating volunteer.
 * 
 */

int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  int T;  // number of test cases.
  int a1,a2; // the answers
  int t=0,y;  // t: case number, y=answer (numeric)
  int a[4];  //I only care about the row given in the first answer.
  int b;
  int i,j,k,l;
  std::string bad_magic="Bad magician!";
  std::string cheater="Volunteer cheated!";
  if(argc==2)
  {
    in.open(argv[1]);
    out.open((std::string(argv[1]) + ".out").c_str(),std::ofstream::out|std::ofstream::trunc);
    std::getline(in,s); // number of test cases.
    buf.str(s);
    buf >> T;
    buf.clear();
    while(std::getline(in,s))  // a1
    {
      t++; // increment test case counter.
      l=0;
      buf.str(s);
      buf >> a1;  // row we will concentrate on.
      buf.clear();
      for(i=0;i<4;i++)
      {
	std::getline(in,s);
	if(i==(a1-1))
	{
	  buf.str(s);
	  // the row we are interested in
	  for(j=0;j<4;j++)
	  {
	    buf >> a[j];
	  }
	  buf.clear();
	}
      }
      std::getline(in,s);
      buf.str(s);
      buf >> a2; // second answer.
      buf.clear();
      for(i=0;i<4;i++)
      {
	std::getline(in,s);
	if(i==(a2-1))
	{
	  // the row the volunteer told us.
	  // search it for a[] elements.
	  buf.str(s);
	  for(j=0;j<4;j++)
	  {
	    buf >> b;
	    for(k=0;k<4;k++)  // search for b in a.
	    {
	      if(a[k] == b)  // found it.
	      {
		l++;  // increase counter
		y=b;  // possible answer.
	      }
	    }
	  }
	  buf.clear();
	}
      }
      if(!l) // cheater
      {
	s=cheater;
      }
      else
      {
	if(l==1)
	{
	  buf.clear();
	  buf.str("");
	  buf << y;
	  s=buf.str(); // answer
	}
	else
	{
	  // not 0, not 1 : bad magician
	  s=bad_magic;
	}
      }
      out << "Case #" << t << ": " << s << std::endl;
    }
    in.close();
    out.close();
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}


