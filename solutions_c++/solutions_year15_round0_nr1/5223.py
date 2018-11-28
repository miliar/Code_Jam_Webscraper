#include <iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

main()
{
    ifstream in("in.in");
    ofstream out("out.txt");
    int test;
    in>>test;
    long long sh;
    long long num;
    for(int i=1;i<=test;i++)
    {
        int sum=0 , c=0,standup=0;
        in>>sh;
        in>>num;
        int x;
        vector<int> t;
        for(int j=0;j<=sh;j++)
        {
            x=num%10;
            num/=10;
            t.push_back(x);
        }
        for(int j=0;j<=sh ;j++)
        {
            if(sum>=j )
                    sum+=t[sh-j];
            else
            {
                c+=j-sum;
                sum+=t[sh-j] + j-sum;
            }
        }
        out<<"Case #"<<i<<": "<<c<<endl;
    }

}
