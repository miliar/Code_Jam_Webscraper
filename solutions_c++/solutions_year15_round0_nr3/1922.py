//
//  main.cpp
//  dijkstra
//
//  Created by Prasanna Prakash on 4/11/15.
//  Copyright (c) 2015 Prasanna Prakash. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;
string result(string c, string d);
string reduce(string s);

int main()
{
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
    string n, s, new_str, lines, nchar;
    int line=0, c=0;
    getline(fin, lines);
    line=atoi(lines.c_str());
    
    for(int i=1;i<=(line*2);i+=2)
    {
        c++;
        getline(fin, n);
        nchar=n.substr(0,n.find(" "));
        n=n.substr(n.find(" ")+1);
        int num=atoi(n.c_str());
        getline(fin,s);
        
        for (int i=1; i<=num; i++)
            new_str+=s;
        
        if(new_str.length()<3 || nchar.compare("1")==0)
            fout<<"Case #"<<c<<": "<<"NO"<<endl;
        else if(new_str.length()==3)
        {
            if(new_str.compare("ijk")==0)
                fout<<"Case #"<<c<<": "<<"YES"<<endl;
            else
                fout<<"Case #"<<c<<": "<<"NO"<<endl;
        }
        else
            fout<<"Case #"<<c<<": "<<reduce(new_str)<<endl;
        
        new_str="";
    }
    
    fin.close();
    fout.close();
    
    return 0;
    
}

string result(string c, string d)
{
    string result,first=c;
    
    if(c[0]=='-')
        c=c[1];
    
    if(c==d)result = "-1";
    else if(c.compare("1")==0 && d.compare("1")!=0)result = d;
    else if(c.compare("1")==0 && d.compare("1")==0)result = "1";
    else if(c.compare("i")==0 && d.compare("j")==0)result = "k";
    else if(c.compare("i")==0 && d.compare("k")==0)result = "-j";
    else if(c.compare("j")==0 && d.compare("i")==0)result = "-k";
    else if(c.compare("j")==0 && d.compare("k")==0)result = "i";
    else if(c.compare("k")==0 && d.compare("i")==0)result = "j";
    else if(c.compare("k")==0 && d.compare("j")==0)result = "-i";
    
    if(first[0]=='-' && result[0]=='-')
        result=result[1];
    else if(first[0]=='-' && result[0]!='-')
        result="-"+result;
    
    return result;
    
}

string reduce(string s)
{
    bool flag=false;
    int i=0,j=0,k=0;
    string s_i,s_j,s_k;
    s_i=s[0];
    
    for(i=1;i<s.length();i++)
    {
        
        if(s_i=="i")
        {
            flag=true;
            break;
        }
        s_i=result(s_i,s.substr(i,1));
    }
    
    
    if(flag)
    {
        flag=false;
        s_j=s[i];
        for(j=i+1;j<s.length();j++)
        {
            
            if(s_j=="j")
            {
                flag=true;
                break;
            }
            s_j=result(s_j,s.substr(j,1));
        }

    }
    
    
    if(flag)
    {
        flag=false;
        s_k=s[j];
        for(k=j+1;k<s.length();k++)
        {
           
            s_k=result(s_k,s.substr(k,1));
        }
        
        if(s_k=="k")
        {
            flag=true;
        }

    }
    
    if(flag)
        return "YES";
    else
        return "NO";
    
}

