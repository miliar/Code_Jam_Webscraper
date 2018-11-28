#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    //reading file for no of test cases
    string line;
    ifstream myfile("SI.in");
    ofstream nfile("SO.txt");
    getline(myfile,line);
    int nCases = stoi(line);
    //reading file for no of test cases
    
    for(int i=0; i < nCases; i++)
    {
        vector<int> store;
        int num;
        getline(myfile,line);
        num = stoi(line);
        int temp = num;
        int a;
        
        if(num == 0)
        {
            nfile << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        }
        else
        {
            while(temp > 0)
            {
                a = temp%10;
                temp = temp/10;
                int check = 0;
                for(int p=0; p < store.size(); p++)
                {
                    if(a == store[p])
                        check = 1;
                }
                if(check == 0)
                    store.push_back(a);
            }
            
            int j = 2;
            int fool;
            
            while(store.size() != 10)
            {
                fool = num * j;
                j++;
                
                int temp = fool;
                int a;
                while(temp > 0)
                {
                    a = temp%10;
                    temp = temp/10;
                    int b = 0;
                    for(int k=0; k < store.size(); k++)
                    {
                        if(a == store[k])
                            b=1;
                        
                    }
                    if(b == 0)
                        store.push_back(a);
                }
                
            }
            nfile << "Case #" << i+1 << ": " << fool << endl;
        }
    }
    nfile.close();
}