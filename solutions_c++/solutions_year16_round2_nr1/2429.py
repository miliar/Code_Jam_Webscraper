#include <stdio.h>

#include <iostream>

#include <vector>

#include <algorithm>

#include <queue>

#include <fstream>

using namespace std;

int main()

{
    
    ifstream input;
    
    ofstream output;
    
    input.open("input.txt");
    
    output.open("output.txt");
    

    
    int t;
    
    input>>t;
    
    
    
    for(int k=1 ; k<=t ; k++)
        
    {
        output<<"Case #"<<k<<": ";
        vector<int> num;
        int size=0;
        int c[26]={0};
        string s;
        input>>s;
        size = s.size();
        for(int i=0 ; i<s.size() ; i++)
        {
            c[s[i]-'A']++;
        }
        int size1 = size;
        while(size)
        {
            if(c['z'-'a'])
            {
                size-=4;
                num.push_back(0);
                c['z'-'a']--;
                c['e'-'a']--;
                c['r'-'a']--;
                c['o'-'a']--;
            }
            else if(c['x'-'a'])
            {
                size-=3;
                num.push_back(6);
                c['s'-'a']--;
                c['i'-'a']--;
                c['x'-'a']--;
            }
            else if(c['g'-'a'])
            {
                size-=5;
                num.push_back(8);
                c['e'-'a']--;
                c['i'-'a']--;
                c['g'-'a']--;
                c['h'-'a']--;
                c['t'-'a']--;
            }
            
            else if(c['h'-'a'])
            {
                size-=5;
                num.push_back(3);
                c['t'-'a']--;
                c['h'-'a']--;
                c['r'-'a']--;
                c['e'-'a']--;
                c['e'-'a']--;
            }
            
            else if(c['r'-'a'])
            {
                size-=4;
                num.push_back(4);
                c['f'-'a']--;
                c['o'-'a']--;
                c['u'-'a']--;
                c['r'-'a']--;
            }
            
            else if(c['f'-'a'])
            {
                size-=4;
                num.push_back(5);
                c['f'-'a']--;
                c['i'-'a']--;
                c['v'-'a']--;
                c['e'-'a']--;
            }
            
            else if(c['v'-'a'])
            {
                size-=5;
                num.push_back(7);
                c['s'-'a']--;
                c['e'-'a']--;
                c['v'-'a']--;
                c['e'-'a']--;
                c['n'-'a']--;
            }
            
            else if(c['i'-'a'])
            {
                size-=4;
                num.push_back(9);
                c['n'-'a']--;
                c['i'-'a']--;
                c['n'-'a']--;
                c['e'-'a']--;
            }
            
            else if(c['t'-'a'])
            {
                size-=3;
                num.push_back(2);
                c['t'-'a']--;
                c['w'-'a']--;
                c['o'-'a']--;
            }
            
            else if(c['o'-'a'])
            {
                size-=3;
                num.push_back(1);
                c['o'-'a']--;
                c['n'-'a']--;
                c['e'-'a']--;

            }
        }
        sort(num.begin() , num.end());
        
        for(int i=0 ; i<num.size() ; i++)
            output<<num[i];
        output<<endl;
        
    }
    
    output.close();
    
    input.close();
    
    return 0;
    
} 

