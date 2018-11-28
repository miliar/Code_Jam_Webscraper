#include <iostream>
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int T,N;
    string input;
    getline(cin,input);
    istringstream test(input);
    test>>T;

    for(int i=0;i<T;i++)
    {
        getline(cin,input);
        istringstream iss(input);
        iss>>N;
        bool digits[10]={false,false,false,false,false,false,false,false,false,false};
        bool sleep=false;
        if(N==0)
        cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
        {
            int t=1;
            int number=N;
            while(!sleep)
            {
                number=N*t;
                input=to_string(number);
                int len=input.length();
                for(int j=0;j<len;j++)
                {
                    int index=input[j]-'0';
                    digits[input[j]-'0']=true;
                }
                sleep=true;
                for(int j=0;j<10;j++)
                    if(!digits[j])
                        sleep=false;
                t++;

            }
            cout<<"Case #"<<i+1<<": "<<number<<endl;
        }
    }
    return 0;
}
