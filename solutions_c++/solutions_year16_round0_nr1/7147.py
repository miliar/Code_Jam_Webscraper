//#include<iostream>
#include<fstream>
#include<set>
using namespace std;

int main()
{
    int T,N;
    ifstream cin("/Users/saymyname/Desktop/Competitive/GCJ/input.txt");
    ofstream cout("/Users/saymyname/Desktop/Competitive/GCJ/output.txt");
    cin>>T;
    for(int i=1; i<=T; i++)
    {
        cin>>N;

        if(N==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            set<int>digits;
            long long temp=N;
            while(1)
            {
                long long nTemp=temp;
                while(temp)
                {
                    digits.insert(temp%10);
                    temp/=10;
                }

                if(digits.size()==10)
                {
                    cout<<"Case #"<<i<<": "<<nTemp<<endl;
                    break;
                }
                temp=nTemp+N;
            }
        }
    }
    return 0;
}
