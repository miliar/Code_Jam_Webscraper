#include <iostream>
#include <fstream>

using namespace std;

bool isConsonant(char c)
{
    if(c=='a')
    {
        return false;
    }
    else if(c=='e')
    {
        return false;
    }
    else if(c=='i')
    {
        return false;
    }
    else if(c=='o')
    {
        return false;
    }
    else if(c=='u')
    {
        return false;
    }
    else
    {
        return true;
    }
}

bool hasNConsonants(string s,int n)
{
    int counter=0;
    for(int i=0;i<s.size();i++)
    {
        if(!isConsonant(s[i]))
        {
            counter=0;
        }
        else
        {
            counter++;
        }
        
        if(counter==n)
        {
//            cout << "string: " << s << " has at least " << n << " consonants" << endl;
            return true;
        }
    }
//    cout << "string: " << s << " does not have at least " << n << " consonants" << endl;
    return false;
}

int main(int argc, const char * argv[])
{
    int T;
    
    ifstream infile ("/Users/diego/Desktop/Google Code Jam/consonants/data.in");
    ofstream outFile ("/Users/diego/Desktop/Google Code Jam/consonants/data.out");
    
    if (infile.is_open() && outFile.is_open())
    {
        string s,numStr;
        infile >> T;
        getline(infile, s);
        for(int caso=0;caso<T;caso++)
        {
            int counter=0;
            getline(infile, s);
            unsigned long pos=s.find(" ");
            numStr=s.substr(pos+1);
            int n = atoi(numStr.c_str());
            s=s.substr(0,pos);
            
            cout << endl;
            for(int i=0;i<s.size()-n+1;i++)
            {
                for(int j=n;j<s.size()+1-i;j++)
                {
//                    cout << "(i,j)=(" << i << "," << j << ")" << endl;
                    if(hasNConsonants(s.substr(i,j), n))
                    {
                        counter++;
                    }
                }
            }
            cout << endl;
            
            outFile << "Case #" << caso+1 << ": " << counter << endl;
//            cout << "Case #" << caso+1 << "(" << s << "): " << counter << endl;
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}

