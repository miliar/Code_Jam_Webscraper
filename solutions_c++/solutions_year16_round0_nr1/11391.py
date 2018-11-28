# include <iostream>
# include <conio.h>
# include <stdlib.h>
# include <string.h>
# include <sstream>
# include <fstream>
# include <iterator>
# include <algorithm>


using namespace std;

string method_(int, string);

int main ()
{
  string myArray[101];

  ifstream file("../input.txt");

  file.unsetf(std::ios_base::skipws);

  unsigned line_count = count(
      std::istream_iterator<char>(file),
      std::istream_iterator<char>(), 
      '\n');

  cout << "Lines: " << line_count << "\n";

  file.close();

  file.open ("../input.txt", ifstream::in);

  /*string line;
  while (getline(file, line))
    cout << line << endl;*/

  int i = 0;
  while(!file.eof() && i < line_count) 
  {
    getline(file,myArray[i]); // read the next line into the next string
    cout<<myArray[i]<<endl;
    ++i;
  }

  int numofTestcases = line_count-1;

  ofstream out("../output.txt");
  for (int testcase = 1; testcase <= numofTestcases; ++testcase)
  {
    cout<<"Case #"<<testcase<<": "<<method_(testcase, myArray[testcase])<<endl;
    out<<"Case #"<<testcase<<": "<<method_(testcase, myArray[testcase])<<endl;
  }
  out.close();
  getch();
  return 0;
}

string method_ (int testcase, string str)
{ 
  istringstream buffer(str);
  int input;
  buffer >> input;
  
  //cout<<" Enter a number = ";
  //cin>>input;

  if (input == 0)
  {
    //cout<<"Case #"<<testcase<<": "<<"INSOMNIA"<<endl;
    //getch();
    return "INSOMNIA";
  }

  struct refer
  {
    char digit;
    bool check;
  };
  refer refe[10] = {
    {'0', false},
    {'1', false},
    {'2', false},
    {'3', false},
    {'4', false},
    {'5', false},
    {'6', false},
    {'7', false},
    {'8', false},
    {'9', false},
  };

  string lstString("");

  for (int i=1; input*i < 20000; ++i)
  {
    int temp = input * i;
    ostringstream ss;
    ss << temp;
    lstString = ss.str();
    //cout<<lstString<<endl;    

    for (int j=0; j<10; ++j)
    {
      if (!refe[j].check)
      {
        if (lstString.find(refe[j].digit) != string::npos) 
        {
          refe[j].check = true;
          //cout << "found!" << refe[j].digit << '\n';
        }
      }
    }

    bool tobeFound = false;
    for (int j=0; j<10; ++j)
    {
      if (!refe[j].check)
      {
        tobeFound = true;  
      }
    }

    if(tobeFound == false)
    {
      //cout<<"Case #"<<testcase<<": "<<lstString<<endl;
      //break;
      return lstString;
    }
  }

  for (int j=0; j<10; ++j)
  {
    if (!refe[j].check)
    {
      //cout<<"Case #"<<testcase<<": "<<"INSOMNIA"<<endl;
      //return 0;
      return "INSOMNIA";
    }
  }

  //getch();
  return 0;
}