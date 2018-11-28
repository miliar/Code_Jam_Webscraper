#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
   ofstream myfile;
   myfile.open("output.in");
   int cases=0;
   cin >>cases;

   for(int i=0;i<cases;i++)
   {
      string word;
      cin>>word;
      vector<char> last_word;
      last_word.push_back(word[0]);
      for(int j=1;j< word.length();j++)
      {
           if(static_cast<int>(word[j])>= static_cast<int>(last_word[0]))
           {
             last_word.insert ( last_word.begin() , word[j] );
           }
           else last_word.push_back(word[j]);

      }
      cout << "Case #"<<i+1<<": ";
      myfile << "Case #"<<i+1<<": ";
      for(int k=0;k< word.length();k++)
      {
        cout<<last_word[k];
        myfile <<last_word[k];
      }
      cout<<endl;
      myfile<<endl;;
   }

    myfile.close();

    return 0;
}
