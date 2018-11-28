#include <cstdio>
#include <fstream>
#include <cmath>
#include <queue>
#include <iostream>
using namespace std;
char graph[4][4];
int main()
{
    ifstream input;
    input.open("C:\\Users\\Administrator\\Desktop\\C-small-attempt1.in");
    int t;
    //cin>>t;
    input>>t;
    long long n,m;
    //getchar();
    ofstream output;
    output.open("C:\\Users\\Administrator\\Desktop\\C-small-attempt1.out");
    for (int c = 1;c <= t;c++)
    {
        //cin>>n>>m;
        input>>n>>m;
        int count = 0;
        for (long long i = sqrt(n);i <= sqrt(m);i++)
        {
            queue<int> s;
            long long temp = i;
            long long res = temp;
            while(temp != 0)
            {
                s.push(temp%10);
                temp /= 10;
            }
            while(!s.empty())
            {
                temp*=10;
                temp += s.front();
                s.pop();
                //cout<<temp<<endl;
            }
            if(res == temp)
            {
                temp = pow(i,2);
                res = temp;
                while(temp != 0)
                {
                    s.push(temp%10);
                    temp /= 10;
                }
                while(!s.empty())
                {
                    temp*=10;
                    temp += s.front();
                    s.pop();
                    //cout<<temp<<endl;
                }

                if(temp == res && res >= n&&res <=m)
                {
                    cout<<temp<<" "<<res<<endl;
                    count++;
                }
            }
        }
        cout<<"Case #"<<c<<": "<<count<<"\n";
        output<<"Case #"<<c<<": "<<count<<"\n";
    }
    input.close();
    output.close();
}
