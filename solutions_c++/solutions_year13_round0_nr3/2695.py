#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool isFair(int n)
{
    string s,tmp;
    s=to_string(n);//in c++11
    tmp=s;
    reverse(s.begin(), s.end());
    if(s==tmp)
    {
//        cout << n << "is fair" << endl;
//        cout <<"n2: " << n*n << endl;
        return true;
    }
    else
    {
        return false;
    }
}

int main ()
{
    vector<int> data;
    ifstream infile ("/Users/diego/Desktop/Google Code Jam/fairAndSquare/data.in");
    ofstream outFile ("/Users/diego/Desktop/Google Code Jam/fairAndSquare/data.out");
    
    int cases;
    
    if (infile.is_open() && outFile.is_open())
    {
        infile >> cases;
        int counter,LOW,UP;
        for(int i=0;i<cases;i++)
        {
            infile >> LOW;
            infile >> UP;
            counter=0;
            for(int a=1;a*a<=UP;a++)
            {
                if(isFair(a))
                {
                    if(isFair(a*a))
                    {
                        if((a*a)<=UP && (a*a)>=LOW)
                        {
                            counter++;
                        }
                    }
                }
            }
            outFile << "Case #" << i+1 << ": " << counter << endl;
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}