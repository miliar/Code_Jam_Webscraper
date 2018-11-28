#include <iostream>
#include<string>
#include<sstream>
#include<fstream>

using namespace std;
//ofstream out("A-small-attempt0.txt");
int main()
{
   // ifstream in("A-small-attempt0.in");
    int t,i,j;
    string input;
    getline(cin,input);
    stringstream mystrm(input);
    mystrm>>t;
    int res[t];
    for(i=0;i<t;i++)
    {
        int smax;
        string test;
        getline(cin,test);
        stringstream my (test);
        my>>smax;
        string str;
        my>>str;
        int sum=str[0]-'0';
       // cout<<sum;
        int count=0;
        //cout<<str;
        //cout<<str.length();
        for(j=1;j<str.length();j++)
        {
            if(str[j]!='0'&&j<=sum)
            sum=sum+str[j]-'0',cout<<sum<<endl;
            else if(str[j]!='0'&&j>sum)
           {
            //cout<<sum;
            count=count+j-sum;
            sum=j+str[j]-'0';
           }
            else if(str[j]=='0')
            continue;

        }
      res[i]=count;
    }
   // cout << "Hello world!" << endl;
   for(i=0;i<t;i++)
   cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
    return 0;
}

