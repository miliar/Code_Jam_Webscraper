#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
 string T;
 getline(in, T);

	int Smax, Length = 0, p = 0, l = 0;
	for (int i = 0; i < T.length(); i++)
       Length = Length * 10 + int(T[i]) - 48;
    
	for(int j = 1; j <= Length; j++)
	{
        p++;
        in >> Smax;
		int *s = new int [Smax + 1];
		char a;
        for(int i = 0; i < Smax + 1; i++)
            {
				in >> a;
				s[i] = a - 48;
		}
        int count = 0, sum = 0;
        for(int i = 0; i < Smax; i++)
        {
            sum += s[i];
            while(sum < i+1){
                sum++;
                count++;
            }   
        }
        out<<"Case #"<<p<<": "<<count<<endl;
		delete []s;
    }
   
   return 0;
}

