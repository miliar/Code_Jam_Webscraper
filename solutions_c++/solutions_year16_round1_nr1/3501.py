#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
vector<char> str;

int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("A-large.in");
    f2.open("output.out");
    int c=1,t,x,r,col;
    string arr;
    f1>>t;
    while(c<=t)
    {
               f2<<"Case #"<<c++<<": ";
               f1>>arr;
               str.clear();
               x = arr.length();
               str.push_back(arr[0]);
			   for(int i=1;i<x;i++)
               {
               		if( arr[i] >= str[0])
               		{
               			str.insert(str.begin() , arr[i]);
               		}
               		else str.push_back(arr[i]);
               }
               for(int i=0;i<x;i++)f2<<str[i];
               f2<<endl;
    }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
}
