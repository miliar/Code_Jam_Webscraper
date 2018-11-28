#include <iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
using namespace std;

int main()
{
   ifstream file("input.in");
   ofstream out("output.txt");
   int T,a,b,k;
   file>>T;
   int count=0;
   for(int i=1;i<=T;i++)
   {
      file>>a;
      file>>b;
      file>>k;
      for(int j=0;j<a;j++)
          for(int l=0;l<b;l++)
    	{
			if((j&l)<k)
            {
				//cout<<j<<" "<<l<<endl;
                count++;
            }
		}
		
      out<< "Case #" << i << ": " << count << endl;
      count=0;
   }
   file.close();
   out.close();
   return 0;
}

