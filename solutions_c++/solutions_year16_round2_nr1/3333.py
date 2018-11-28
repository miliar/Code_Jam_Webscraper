//
//  main.cpp
//  [Codejam]CountingSheep
//
//  Created by 장형원 on 2016. 4. 9..
//  Copyright © 2016년 jhw. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

unsigned int T;
multiset<char> input;
multiset<int> result;

void eraseChar(multiset<char> &input, char c, int num)
{
    multiset<char>::iterator iter;
    multiset<char>::iterator iter2;
    
    iter = input.find(c);
    for(iter2 = iter; num > 1; num--)
    {
        iter2++;
    }
    if(iter2 != input.end())
        iter2++;
    input.erase(iter, iter2);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    cin >> T;
    
    unsigned int test = T;
    
    while(T)
    {
        string str;
        string::iterator iter_s;
        
        cin >> str;
        for(iter_s = str.begin(); iter_s != str.end(); iter_s++)
        {
            input.insert(*iter_s);
        }
        
        int num = 0;
        multiset<char>::iterator iter;
        multiset<char>::iterator iter2;
        
        iter = input.find('G');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(8);
            }while(*iter == 'G' && iter != input.end());
            
            eraseChar(input, 'E', num);
            eraseChar(input, 'I', num);
            eraseChar(input, 'H', num);
            eraseChar(input, 'T', num);
            num = 0;
        }
        
        iter = input.find('U');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(4);
            }while(*iter == 'U' && iter != input.end());
            
            eraseChar(input, 'F', num);
            eraseChar(input, 'O', num);
            eraseChar(input, 'R', num);
            num = 0;
        }
        
        iter = input.find('W');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(2);
            }while(*iter == 'W' && iter != input.end());
            
            eraseChar(input, 'T', num);
            eraseChar(input, 'O', num);
            num = 0;
        }
        
        iter = input.find('X');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(6);
            }while(*iter == 'X' && iter != input.end());
            
            eraseChar(input, 'S', num);
            eraseChar(input, 'I', num);
            num = 0;
        }
        
        iter = input.find('Z');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(0);
            }while(*iter == 'Z' && iter != input.end());
            
            eraseChar(input, 'E', num);
            eraseChar(input, 'R', num);
            eraseChar(input, 'O', num);
            num = 0;
        }
        
        iter = input.find('F');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(5);
            }while(*iter == 'F' && iter != input.end());
            
            eraseChar(input, 'I', num);
            eraseChar(input, 'V', num);
            eraseChar(input, 'E', num);
            num = 0;
        }
        
        iter = input.find('O');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(1);
            }while(*iter == 'O' && iter != input.end());
            
            eraseChar(input, 'N', num);
            eraseChar(input, 'E', num);
            num = 0;
        }
        
        iter = input.find('R');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(3);
            }while(*iter == 'R' && iter != input.end());
            
            eraseChar(input, 'T', num);
            eraseChar(input, 'H', num);
            eraseChar(input, 'E', num + num);
            num = 0;
        }
        
        iter = input.find('S');
        if(iter != input.end())
        {
            do
            {
                num++;
                iter = input.erase(iter);
                result.insert(7);
            }while(*iter == 'S' && iter != input.end());
            
            eraseChar(input, 'E', num + num);
            eraseChar(input, 'V', num);
            eraseChar(input, 'N', num);
            num = 0;
        }
        
        while(input.size() != 0)
        {
            iter = input.find('N');
            if(iter != input.end())
            {
                do
                {
                    num++;
                    iter = input.erase(iter);
                    
                }while(*iter == 'N' && iter != input.end());
            
                for(int i = 0; i < num/2 ; i++)
                    result.insert(9);
                eraseChar(input, 'I', num/2);
                eraseChar(input, 'E', num/2);
                num = 0;
            }
        }
        
        cout << "Case #" << test - T + 1 << ": ";
        
        multiset<int>::iterator iter_r;
        for(iter_r = result.begin(); iter_r != result.end(); iter_r++)
        {
            cout << *iter_r;
        }
        cout << endl;
        
        T = T - 1;
        input.clear();
        result.clear();
    }
    
    return 0;
}
