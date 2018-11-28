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
                  string s;
                  cin>>s;
                  vector<char> v(s.begin(), s.end());
                 /* for(int j=0;j<v.size();j++)
                  {
                      cout<<v[j]<<endl;
                  }*/
                  //int answer=compute(v);
                 /* std::sort(v.begin(), v.end());
                 std::reverse(v.begin(), v.end());
                  for(int j=0;j<v.size();j++)
                  {
                      cout<<v[j]<<endl;
                  }*/
                  char a=v[0];
                  vector<char> v1;
                  v1.push_back(a);
                  for(int j=1;j<v.size();j++)
                  {
                      if(v[j]<a)
                        v1.push_back(v[j]);
                      else if((v[j]==a)||(v[j]>a))
                      {

                            v1.insert( v1.begin() , v[j] );
                            //v1[g]=v[j];
                      }
                      a=v1[0];

                  }
                  cout<<"Case #"<<i<<": ";
                   for(int j=0;j<v1.size();j++)
                  {

                        cout<<v1[j];
                  }
                  cout<<"\n";





            }
}


