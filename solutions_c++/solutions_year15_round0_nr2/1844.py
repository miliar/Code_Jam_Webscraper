//
//  main.cpp
//  dinner
//
//  Created by Prasanna Prakash on 4/11/15.
//  Copyright (c) 2015 Prasanna Prakash. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;
int count_min(vector<int> &a, int max, int c, int initial);

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    
    string s="";
    string s1, strn;
    vector<int> a;
    int n=0, max=0, num=0;
    
    getline(fin,strn);
    num = atoi(strn.c_str());
    
    for(int j=1; j<=(num*2); j++)
    {
        getline(fin,s);
        if(j%2==0)
        {
            s=s+' ';
    
            for(int i=0;i<s.size();i++)
            {
                if(s[i]!=' ')
                    s1+=s[i];
                else
                {
                    n=atoi(s1.c_str());
                    if(n>max)
                        max=n;
                    a.push_back(n);
                    s1="";
                }
            }
   
    
            fout<<"Case #"<<(j/2)<<": "<<count_min(a, max, max, max)<<endl;
            a.clear();
            max=0;
            s1="";
    
        }
    }
    
    fin.close();
    fout.close();
    
    return 0;
}

int count_min(vector<int> &a, int max, int c, int initial)
{
    if(max==1)
        return c;
    vector<int> v=a;
    int mid=max-1;
    int count=0, i;
    for(i=0; i<v.size(); i++)
    {
        if(v[i]>mid)
        {
            count++;
            v.push_back(v[i]-mid);
            v[i]=mid;
        }
    }
    
    
    count=count+mid;
    
    if(count<c)
        c=count;
    return count_min(a,mid,c,initial);
}
