//
//  main.cpp
//  first
//
//  Created by Tingting Cao on 11/05/2014.
//  Copyright (c) 2014 Tingting Cao. All rights reserved.
//

//
//  main.cpp
//  R1A_A
//
//  Created by Tingting Cao on 4/26/14.
//  Copyright (c) 2014 ___CIS___. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <sstream>
using namespace std;

void printVectorInt(vector<int> ints)
{
    
    for(int i=0;i<ints.size()-1;i++)
    {
        cout<<ints[i]<<" ";
    }
    
    cout<<ints[ints.size()-1];
    cout<<endl;
}

void printVectorString(vector<string> strings)
{
    for(int i=0;i<strings.size()-1;i++)
    {
        cout<<strings[i]<<" ";
    }
    cout<<strings[strings.size()-1];
    cout<<endl;
}

void printPermutations(vector<int> ints)
{
    cout<<"Following permutaions:"<<endl;
    do
    {
        printVectorInt(ints);
    }
    while (next_permutation(ints.begin(), ints.end()));
}

//has an extra space at the end of each line
void print2DVectorInt(vector<vector<int> > intss)
{
    for(int i=0;i<intss.size();i++)
    {
        for(int j=0;j<intss[i].size();j++)
        {
            cout<<intss[i][j]<<" ";
        }
        cout<<endl;
    }
}

long find_gcd_long(long a,long b)
{
    long up=long(max(a,b));
    long down=min(a,b);
    long remainder=up%down;
    
    while(remainder!=0)
    {
        up=down;
        down=remainder;
        remainder=up%down;
    }
    
    long gcd=down;
    
    return gcd;
}

int find_gcd_int(int a,int b)
{
    int up=int(max(a,b));
    int down=min(a,b);
    int remainder=up%down;
    
    while(remainder!=0)
    {
        up=down;
        down=remainder;
        remainder=up%down;
    }
    
    int gcd=down;
    
    return gcd;
}

/* Define 2D vector
 *
 * vector< vector<bool> > Seen(R, 	vector<bool>(C));
 */

/*  Get a line and spit
 
 int case_num;
 cin>>case_num;
 
 vector<vector<string> > sentences(case_num);
 
 string nothing;
 getline(cin, nothing);
 
 for(int i=0;i<case_num;i++)
 {
 string line;
 getline(cin, line);
 
 stringstream ss(line);
 
 string sub;
 
 //split by space
 while (getline(ss,sub,' '))
 {
    sentences[i].push_back(sub);
 }
 
 }
 
 */

/*  Use of map
 
 map<int,int> index_price;
 map<int,int> price_index;
 
 index_price.insert(make_pair(j+1, cur_price));
 
 while(price_index.find(rest)!=price_index.end())
 {
 
 map<int,int>::iterator pos=price_index.find(rest);
 
 pair<int,int> p=*price_index.find(rest);
 
 another_index=p.second;
 
 if(k<another_index)
 {
     cout<<"Case #"<<i+1<<": "<<k<<" "<<another_index<<endl;
     solved=true;
     break;
 }
 else if(k>another_index)
 {
 cout<<"Case #"<<i+1<<": "<<another_index<<" "<<k<<endl;
 solved=true;
 break;
 }
 else if(k==another_index)
 {
 ++pos;
 pair<int, int> next=*pos;
 
 if(next.first==rest)
 {
 cout<<"Case #"<<i+1<<": "<<k<<" "<<next.second<<endl;
 solved=true;
 break;
 }
 else
 {
     break;
 }
 }
 }
 */

/*
 printf("%.3f",variable);  //double
 printf("%.3Lf,variable"); //long double
 */


bool isTimesOftwo(int num)
{
    bool valid=false;
    
    for (int i=1;i<=10;i++)
    {
        if (num==pow(2, i))
        {
            valid=true;
        }
    }
    
    return valid;
}

int main(int argc, const char * argv[])
{
    int case_num;
    cin>>case_num;
    
    string nothing;
    getline(cin, nothing);
    
    for (int c=0;c<case_num;c++)
    {
        string line;
        getline(cin, line);
//        cout<<line<<endl;
        
        stringstream ss(line);
        
        string sub;
        
        int upper,down;
        
        vector<int> test;
        
        //split by space
        while (getline(ss,sub,'/'))
        {
            int temp=atoi(sub.c_str());
            test.push_back(temp);
        }
        
        upper=test[0];
        down=test[1];
        
//        cout<<upper<<" "<<down<<endl;
        
        
        cout<<"Case #"<<c+1<<": ";
        
        int count=0;
        bool impossible=false;
        
        while(upper<down)
        {
            if(down%2!=0)
            {
                cout<<"impossible"<<endl;
                impossible=true;
                break;
            }
            else
            {
                down=down/2;
                count++;
            }
        }
        
        if(upper-down>0 && down>1 &&!isTimesOftwo(down) && impossible==false)
        {
            cout<<"impossible"<<endl;
            impossible=true;
        }
        
        if (!impossible)
        {
            cout<<count<<endl;
        }
        
        
    }
        

//        Print Output for each case
        

    
    return 0;
}

