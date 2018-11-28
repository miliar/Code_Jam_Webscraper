/*
 * File:   main.cpp
 * Author: Jon la Cour
 *
 * Created on April 13, 2013, 2:09 PM
 */

#include <fstream>
#include <sstream>
#include <iostream>
#include <list>

using namespace std;

list<char> Add (list<char> num1,list<char> num2);
list<char> Sub (list<char> num1,list<char> num2);
list<char> Mul (list<char> num1,list<char> num2);
list<char> Root (list<char> num1);

list<char> Add (list<char> num1,list<char> num2)
{
    list<char> ans;
    list<char>::iterator iter1,iter2;
    iter1 = num1.begin();
    iter2 = num2.begin();
    int sign = 0;
    if((*iter1) == '-' && (*iter2) == '-')
    {
        num1.pop_front();
        num2.pop_front();
        sign = 1;
        ans = Add(num1,num2);
        ans.push_front('-');
    }
    else if((*iter1) == '-' && (*iter2) != '-')
    {
        num1.pop_front();
        ans = Sub(num2,num1);

    }
    else if((*iter1) != '-' && (*iter2) == '-')
    {
        num2.pop_front();
        ans = Sub(num1,num2);
    }
    else
    {
        int len1,len2,i,len,carry;
        len1 = num1.size();
        len2 = num2.size();
        if(len1 >= len2)
        {
            len = len1;
            for(i = 0; i < len1 - len2; i++)
                num2.push_front('0');
        }
        else
        {
            len = len2;
            for(i = 0; i < len2 - len1; i++)
                num1.push_front('0');
        }

        carry = 0;
        iter1 = num1.end();
        iter2 = num2.end();
        iter1--;
        iter2--;
        for(; (iter1 != num1.begin()) && (iter2 != num2.begin()); --iter1,--iter2)
        {
            i = (*iter1 - '0') + (*iter2 - '0') + carry;

            ans.push_front((i % 10) + '0');
            carry = i / 10;
        }
        i = (*iter1 - '0') + (*iter2 - '0') + carry;

        ans.push_front((i % 10) + '0');
        carry = i / 10;
        if(carry)
            ans.push_front(carry+'0');
    }
    return ans;
}

list<char> Sub (list<char> num1,list<char> num2)
{
    list<char> ans;
    int sign = 0;
    list<char>::iterator iter1,iter2;
    int len1,len2,len;
    iter1 = num1.begin();
    iter2 = num2.begin();
    if((*iter1) == '-' && (*iter2) == '-')
    {
        num2.pop_front();
        num1.pop_front();
        ans = Sub(num2,num1);

    }
    else if( (*iter1) == '-' && (*iter2) != '-')
    {
        num1.pop_front();
        ans = Add(num1,num2);
        ans.push_front('-');
    }
    else if( (*iter1) != '-' && (*iter2) == '-')
    {
        num2.pop_front();
        ans = Add(num1,num2);

    }
    else
    {
        len1 = num1.size();
        len2 = num2.size();
        if(len1 >= len2)
        {
            len = len1;
            for(int i = 0; i < len1 - len2; i++)
                num2.push_front('0');
        }
        else
        {
            len = len2;
            for(int i = 0; i < len2 - len1; i++)
                num1.push_front('0');
        }

        int carry = 0,i;
        iter1 = num1.end();
        iter2 = num2.end();
        iter1--;
        iter2--;
        for(; (iter1 != num1.begin()) && (iter2 != num2.begin()); --iter1,--iter2)
        {
            i = (*iter1 - '0' - carry) - (*iter2 - '0');
            carry = 0;
            if( i < 0)
            {
                i += 10;
                carry = 1;
            }

            ans.push_front((i % 10) + '0');
        }
        i = (*iter1 - '0' - carry) - (*iter2 - '0');
        if(i < 0)
        {
            i += 10;
            sign = 1;
        }

        if(i) ans.push_front(i + '0');
        if(sign)
            ans.push_front('-');
    }
    return ans;
}

list<char> Mul (list<char> num1,list<char> num2)
{
    list<char> ans;
    int sign = 0;
    int len1,len2,len;
    list<char>::iterator iter1,iter2,iter;
    list<char> high,low;
    list<char> anshigh,anslow;
    int th,tl;
    int i,j,k;

    if(num1.size() == 1 && num2.size() == 1)
    {
        th = *(num1.begin()) - '0';
        tl = *(num2.begin()) - '0';
        th *= tl;
        ans.push_front( th % 10 + '0');
        ans.push_front( th / 10 + '0');
        return ans;
    }
    else if(num1.size() == 1 && num2.size() > 1)
    {
        if(*(num2.begin()) == '-')
        {
            sign = 1;
            num2.pop_front();
        }
        len2 = num2.size();
        if(len2 == 1)
        {
            ans = Mul(num1,num2);
            if(sign)
                ans.push_front('-');
        }
        else
        {
            for(iter= num2.begin(),i = 0; i < len2 / 2; i++,iter++)
            {
                high.push_back(*iter);
            }
            for(; iter!=num2.end(); iter++)
            {
                low.push_back(*iter);
            }
            len = low.size();
            anshigh = Mul(num1,high);
            anslow = Mul(num1,low);
            for(i = 0; i < len; i++)
                anshigh.push_back('0');
            ans = Add(anshigh,anslow);
            if(sign)
                ans.push_front('-');
        }
        return ans;
    }
    else if(num2.size() == 1 && num1.size() > 1)
    {
        if(*(num1.begin()) == '-')
        {
            sign = 1;
            num1.pop_front();
        }
        len1 = num1.size();
        if(len2 == 1)
        {
            ans = Mul(num1,num2);
            if(sign)
                ans.push_front('-');
        }
        else
        {
            for(iter= num1.begin(),i = 0; i < len1 / 2; i++,iter++)
            {
                high.push_back(*iter);
            }
            for(; iter!=num1.end(); iter++)
            {
                low.push_back(*iter);
            }
            len = low.size();
            anshigh = Mul(num2,high);
            anslow = Mul(num2,low);
            for(i = 0; i < len; i++)
                anshigh.push_back('0');
            ans = Add(anshigh,anslow);
            if(sign)
                ans.push_front('-');
        }
        return ans;
    }
    else
    {
        list<char> num1high,num1low,num2high,num2low;
        int flag1 = 0,flag2 = 0;
        if(*(num1.begin()) == '-')
        {
            flag1 = 1;
            num1.pop_front();
        }
        if(*(num2.begin()) == '-')
        {
            flag2 = 1;
            num2.pop_front();
        }
        if((flag1 == 1 && flag2 == 0)||(flag1 == 0 && flag2 == 1))
        {
            sign = 1;
        }
        len1 = num1.size();
        len2 = num2.size();
        if(len1 == 1 || len2 == 1)
        {
            ans = Mul(num1,num2);
            if(sign)
                ans.push_front('-');
        }
        else
        {
            for(iter = num1.begin(),i = 0; i < len1 / 2; iter++,i++)
                num1high.push_back(*iter);
            for( ; iter != num1.end(); iter++)
                num1low.push_back(*iter);
            for(iter = num2.begin(),i = 0; i < len2 / 2; iter++,i++)
                num2high.push_back(*iter);
            for( ; iter != num2.end(); iter++)
                num2low.push_back(*iter);
            int a = (len1 + 1) / 2;
            int b = (len2 + 1) / 2;
            list<char> AC,AD,BC,BD;

            AC = Mul(num1high,num2high);
            AD = Mul(num1high,num2low);
            BC = Mul(num1low,num2high);
            BD = Mul(num1low,num2low);
            for(i = 0; i < a + b; i++)
                AC.push_back('0');
            for(i = 0; i < a; i++)
                AD.push_back('0');
            for(i = 0; i < b; i++)
                BC.push_back('0');
            ans = Add(AC,AD);
            ans = Add(ans,BC);
            ans = Add(ans,BD);
            if(sign)
                ans.push_front('-');
        }
        return ans;
    }
}

list<char> Root (list<char> num1)
{
    list<char> ans, digit, temp;
    int len1 = num1.size();
    int a = len1/2;

    digit.push_back('1');
    ans.push_back('1');

    for(int i = 0; i < a - 1; i++) ans.push_back('0');
    while(true)
    {
        temp = Mul(ans,ans);
        temp = Sub(num1,temp);
        if(*(temp.begin()) == '-') break;
        ans = Add(ans, digit);
    }
    ans = Sub(ans,digit);

    return ans;
}

list<char> translate(string input)
{
    list<char> res;
    int len = input.length();
    for(int i = 0; i < len; i++) res.push_back(input[i]);
    return res;
}

string antitranslate(list<char> num)
{
    string str = "";
    list<char>::iterator it;
    bool zeroHead = true;

    for(it = num.begin() ; it != num.end() ; it++)
    {
        char c = *it;
        if(c == '0')
        {
            if(zeroHead) continue;
            else str += c;
        }
        else
        {
            str += c;
            if(zeroHead) zeroHead = false;
        }
    }
    return str;
}

bool checkPal (string str)
{
    int len = str.length();
    for(int i = 0 ; i < len ; i++)
    {
        if(str[i] != str[len-1-i]) return false;
    }
    return true;
}

int main()
{
    int test, count = 1;
    cin>>test;
    while(test--)
    {
        list<char> num1;
        string input1, input2;

        cin >> input1;
        num1 = translate(input1);

        cin >> input2;

        int answer = 0;
        string now = input1;
        list<char> number = num1;
        list<char> one;
        one.push_back('1');

        while(1)
        {
            if(checkPal(now))
            {
                list<char> tempSqrt = Root(number);
                list<char> tempSquare = Mul(tempSqrt, tempSqrt);

                string temp = antitranslate(tempSqrt);
                string temp2 = antitranslate(tempSquare);

                if(temp2 == now)
                {
                    if(checkPal(temp)) answer++;
                }
            }

            if(now == input2) break;

            number = Add(number, one);
            now = antitranslate(number);
        }

        fstream filestr;
        filestr.open ("output.txt", fstream::in | fstream::out | fstream::app);

        std::ostringstream s;
        s << "Case #" << count++ << ": " << answer;
        std::string result = s.str();

        filestr<<result<<endl;
        filestr.close();
    }
    return 0;
}
