#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
#include<conio.h>
int main()
{
			int test;
			cin>>test;
			for(int i=1;i<=test;i++)
			{
                    int n;
                    cin>>n;
                    int g;
                    int t;
                    vector<int> v;
                    if(n==0)
                    {
                        cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
                        continue;
                    }
                    else
                    {

                        int f=1;
                        while(v.size()!=10)
                        {
                            t=f*n;
                            g=t;
                            for(; g; g/=10)
                            {
                                 int z=g%10;
                                 if (std::find(v.begin(), v.end(), z) == v.end())
                                        v.push_back( z );
                            }
                           f++;

                        }
                    }
                    cout<<"Case #"<<i<<": "<<t<<endl;

			}
}
