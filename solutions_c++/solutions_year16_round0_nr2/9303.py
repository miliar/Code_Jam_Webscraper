#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;
string str;
char arr[110];
//int counter ;
int main()
{
ifstream fin ("B-large.in");
 ofstream fout("output2.out");
//string str = "+++";
 int t; fin >> t;
 for(int tc = 1; tc <= t; tc++) {
   for(int i=0; i < 10;  i++)
      arr[i] =0;
    int counter =0 ;
     fin >> str;
     arr[0]=str[0];
    for (int i=1 ;i<str.length() ;i++){
       arr[i]= str [i];
       //cout<<str<<",,,"<<arr[i-1]<<','<<arr[i]<<endl;
      if ((arr[i-1]=='+')&& (arr[i]=='-')){
        counter ++ ;

      }
      else if( (arr[i-1]=='-')&& (arr[i]=='+'))
       counter++;
       //cout << i;

    }
if (arr[str.length()-1]=='-'){
counter += 1;
}
//cout<<counter<<endl;
fout << "Case #" << tc << ": " << counter<< endl;
//cout << counter;
}
fin.close();
    fout.close();
return 0 ;
}
