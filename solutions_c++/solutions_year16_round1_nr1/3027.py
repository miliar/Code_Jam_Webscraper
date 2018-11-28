#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
   // cout << "Hello world!" << endl;
   int T;
   string input,out;
   getline(cin,input);
    istringstream iss(input);
   iss>>T;
   for(int i=0;i<T;i++)
   {
        getline(cin,input);
        int len=input.length();
        out="";
        for(int i=0;i<len;i++)
        {
            if(i==0)
                out=out+input[i];
            else
            {
                if(out[0]>input[i])
                {
                    out=out+input[i];
                }
                else
                {
                   out=input[i]+out;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<out<<endl;
   }
    return 0;
}
