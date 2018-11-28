#include<cstdio>
#include<iostream>
#include<algorithm>
#include <fstream>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

int main()
{
    ifstream in; //Creating object for input stream
    ofstream out; //Creating object for output stream
    in.open("large.in");    //open a file to read input
    out.open("outlarge.txt"); //open a file to write output
    long long test,loop,len,i,n1,n2,hsh[200];
    vector<int> ans;
    string s;
    in>>test;
    for(loop=1;loop<=test;loop++)
    {
        memset(hsh,0,sizeof hsh);
        ans.clear();
        in>>s;
        len=s.length();
        for(i=0;i<len;i++)
            hsh[s[i]]++;
        while(hsh['Z']!=0)
        {
            hsh['Z']--;
            hsh['E']--;
            hsh['R']--;
            hsh['O']--;
            ans.push_back(0);
        }
        while(hsh['W']!=0)
        {
            hsh['T']--;
            hsh['W']--;
            hsh['O']--;
            ans.push_back(2);
        }
        while(hsh['X']!=0)
        {
            hsh['S']--;
            hsh['I']--;
            hsh['X']--;
            ans.push_back(6);
        }
        while(hsh['S']!=0)
        {
            hsh['S']--;
            hsh['E']--;
            hsh['V']--;
            hsh['E']--;
            hsh['N']--;
            ans.push_back(7);
        }
        while(hsh['V']!=0)
        {
            hsh['F']--;
            hsh['I']--;
            hsh['V']--;
            hsh['E']--;
            ans.push_back(5);
        }
        while(hsh['F']!=0)
        {
            hsh['F']--;
            hsh['O']--;
            hsh['U']--;
            hsh['R']--;
            ans.push_back(4);
        }
        while(hsh['O']!=0)
        {
            hsh['O']--;
            hsh['N']--;
            hsh['E']--;
            ans.push_back(1);
        }
        while(hsh['G']!=0)
        {
            hsh['E']--;
            hsh['I']--;
            hsh['G']--;
            hsh['H']--;
            hsh['T']--;
            ans.push_back(8);
        }
        while(hsh['H']!=0)
        {
            hsh['T']--;
            hsh['H']--;
            hsh['R']--;
            hsh['E']--;
            hsh['E']--;
            ans.push_back(3);
        }
        while(hsh['I']!=0)
        {
            hsh['N']--;
            hsh['I']--;
            hsh['N']--;
            hsh['E']--;
            ans.push_back(9);
        }
        out<<"Case #"<<loop<<":"<<" ";
        sort(ans.begin(),ans.end());
        for(i=0;i<ans.size();i++)
            out<<ans[i];
        out<<endl;
    }
    in.close();             //closing the input file
    out.close();            //closing the output file
return 0;
}
