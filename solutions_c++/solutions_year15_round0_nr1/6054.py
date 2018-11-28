#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;


int str2int(string s)
{
    stringstream ss;
    ss << s;
    int v;
    ss >> v;
    return v;
}

int standingOvation(int maxS, string values)
{
    int friends = 0;
    int standing = 0;
    
    for(int s=0; s<= maxS; ++s)
    {
        int n = str2int(values.substr(s, 1));
        
        if(n != 0 && s > (standing+friends))
            friends += (s - (standing+friends));
        
        standing += n;
    }
    
   
    return friends;
}

int main(int argc, char** argv)
{
    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(argv[2]);
    
    int testNumber;
    input >> testNumber;
    
    
    int maxS;
    string values;
    for(int i=1; i<=testNumber; ++i)
    {
        input >> maxS >> values;
        output << "Case #" << i << ": " << standingOvation(maxS, values) << endl;
    }

    return 0;
}
