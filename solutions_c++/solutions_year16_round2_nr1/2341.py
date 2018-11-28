

#include <cstdio> 
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <list>


using namespace std;


int val(char c)
{
    return c-'A';
}

int main()
{
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        int digit[26] = {0};
        multiset<int> numbers;
        for (int j = 0; j < s.length(); j++)
        {
            digit[s[j] - 'A']++;
        }
        while(digit[val('Z')])
        {
            numbers.insert(0);
            digit[val('Z')]--;
            digit[val('E')]--;
            digit[val('R')]--;
            digit[val('O')]--;
        }        
        while(digit[val('W')])
        {
            numbers.insert(2);
            digit[val('T')]--;
            digit[val('W')]--;
            digit[val('O')]--;
        }        
        while(digit[val('U')])
        {
            numbers.insert(4);
            digit[val('F')]--;
            digit[val('O')]--;
            digit[val('U')]--;
            digit[val('R')]--;
        }        
        while(digit[val('X')])
        {
            numbers.insert(6);
            digit[val('S')]--;
            digit[val('I')]--;
            digit[val('X')]--;
        }        
        while(digit[val('G')])
        {
            numbers.insert(8);
            digit[val('E')]--;
            digit[val('I')]--;
            digit[val('G')]--;
            digit[val('H')]--;
            digit[val('T')]--;
        }        
        while(digit[val('S')])
        {
            numbers.insert(7);
            digit[val('S')]--;
            digit[val('E')]--;
            digit[val('V')]--;
            digit[val('E')]--;
            digit[val('N')]--;
        }        
        while(digit[val('V')])
        {
            numbers.insert(5);
            digit[val('F')]--;
            digit[val('I')]--;
            digit[val('V')]--;
            digit[val('E')]--;
        }        
        while(digit[val('T')])
        {
            numbers.insert(3);
            digit[val('T')]--;
            digit[val('H')]--;
            digit[val('R')]--;
            digit[val('E')]--;
            digit[val('E')]--;
        }       
        while(digit[val('O')])
        {
            numbers.insert(1);
            digit[val('O')]--;
            digit[val('N')]--;
            digit[val('E')]--;
        }       
        while(digit[val('N')] >= 2)
        {
            numbers.insert(9);
            digit[val('N')]--;
            digit[val('I')]--;
            digit[val('N')]--;
            digit[val('E')]--;
        } 

        cout << "Case #"<< i+1<<": ";
        for (auto it : numbers)
        {
            cout << it;
        }
        cout << endl;
        
    }

}
