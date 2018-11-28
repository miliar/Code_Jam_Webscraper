#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;

int main()
{
    ifstream input("A-small-attempt1.in");
    ofstream output("output.txt");
    string line;
    int t, ans, row[4], match, r, num;
    input >> t;     
    for(int i=0; i<t; i++)
    {
            input >> ans;
            getline(input, line);
            for(int j=0; j<4; j++)
            {
                    if(j+1 == ans)
                    {
                           for(int j=0; j<4; j++)
                           {
                                   input >> row[j];
                           }
                           getline(input, line);
                    }
                    else
                    {
                        getline(input, line);
                    }
            }
            input >> ans;
            getline(input, line);
            for(int j=0; j<4; j++)
            {
                    if(j+1 == ans)
                    {
                            match = 0;
                            for(int j=0; j<4; j++)
                            {
                                    input >> r;
                                    for(int j=0; j<4; j++)
                                    {
                                           if(r == row[j])
                                           {
                                                match+=1;
                                                num = r;
                                           }
                                    }
                            }
                            getline(input, line);
                    }
                    else
                    {
                        getline(input, line);
                    }
            }
            if(match == 0)
            {
                 //cout<<"Case #"<<i+1<<": Volunteer cheated!" << endl;
                 output<<"Case #"<<i+1<<": Volunteer cheated!" << endl;
            }
            else if(match == 1)
            {
                 //cout<<"Case #"<<i+1<<": "<<num << endl;
                 output<<"Case #"<<i+1<<": "<<num << endl;
            }
            else if(match >= 2)
            {
                 //cout<<"Case #"<<i+1<<": Bad magician!"<<endl;                                      
                 output<<"Case #"<<i+1<<": Bad magician!"<<endl;                                    
            }  
    }
    input.close();
    return 0;               
}
