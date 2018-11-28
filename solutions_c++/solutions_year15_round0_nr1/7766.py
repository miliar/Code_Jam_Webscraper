#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
int tests=0;//num of tests
string shyvals;
int maxshy;//max shy value
int invite=0;//number of ppl to invite
int standing=0;//number standing
int a[10000];
int acount=0;//count of variables used in a[]
string filename;//name of inputfile
ifstream input;//input filestream
ofstream output;//output filestream

cin >> filename;
input.open(filename.c_str());
output.open("standingovation.txt");
input >> tests;
//cout << tests << endl;
//cout << shyvals[0] << endl;
for(int i=0; i<tests; i++)
{
    input >> maxshy;
    input >> shyvals;
    while(acount<shyvals.length())
    {
          a[acount]=shyvals[acount]-48;
          acount++;
    }
a[acount]=-1;

 for(int j=0; j<=maxshy;j++)
 {
     //cout << shyvals[0] << endl;
     if(a[j]==0 && j==0)
     {invite++;
     standing++;
        // cout << "it equals 0"<< endl;
     }

if(a[j] != 0)
{
    if(standing < j)
    {
        invite=invite+(j-standing);
        standing=standing+(j-standing)+a[j];
    }
    else
    {
        standing=standing+a[j];
    }
}

 }
output << "Case #" << i+1 << ": " << invite << endl;
standing=0;
invite=0;
acount=0;
}

return 0;
}
