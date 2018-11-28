#include <iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in",ios::in);//to open the input file
    ofstream fout("output.txt",ios::out);// to write in output file
    int t;
    fin>>t;     //no of test cases
    for(int j=0;j<t;j++)
    {
        string s;
        int no_people=0,ad_people=0,smax;
        fin>>smax;
        fin>>s;//the string that has to be processed
        for(int i=0;i<=smax;i++)
        {
            if(i==0)
            {
                if(s[i]=='0')
                {
                    no_people=1;
                    ad_people=1;
                }
            }
            else if(no_people < i)
            {
                ad_people+=(i - no_people);
                no_people=i;

            }
            no_people+=(s[i]-48);
        }
        fout<<"Case #"<<j+1<<": "<<ad_people<<"\n";  // answer

    }


}
