#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }


int main()
{

    ofstream myfile;
    myfile.open ("Out.txt");

    int t;
    cin>>t;

    for(int k=0;k<t;k++)
    {
    int n;
    cin>>n;
    string s;

    int a[10];
    for(int i=0;i<10;i++)
    {
        a[i] = 0;
    }

    int counter = 0;
    int j = 1;
    int m = n;
    if(n!=0)
    {
    while(counter!=10)
    {
        n = m*j;
        string s = NumberToString(n);
        for(int i=0;i<s.size();i++)
        {
            int x = s[i]-'0';
            if(a[x]==0)
            {
                counter++;
                a[x] = 1;
            }
        }
        j++;
    }
     myfile<<"Case #"<<k+1<<": "<<n<< endl;
    }
    else
    {
        myfile<<"Case #"<<k+1<<": "<<"INSOMNIA"<< endl;
    }
    }

     myfile.close();


    return 0;
}
