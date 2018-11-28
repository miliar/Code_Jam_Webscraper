#include <string>
#include <fstream>
#include <iostream>
using namespace std;

bool digit[10];
bool finish;

string Add(string a, string b)
{
    int ai = a.length() - 1, bi = b.length() - 1;
    string res = "", temp = "0";
    
    while(ai >= 0 && bi >= 0)
    {
        temp[0] = (a.at(ai) + b.at(bi) - '0');
        res = temp + res;
        --ai, --bi;
    }
    
    while(ai >= 0)
    {
        res = a.at(ai) + res;
        --ai;
    }
    
    while(bi >= 0)
    {
        res = b.at(bi) + res;
        --bi;
    }
    
    int carry = 0;
    for(int ci = res.length() - 1; ci >= 0; --ci)
    {
        if(res.at(ci) > '9')
        {
            res.at(ci) -= 10;    
            
            if(ci == 0)
                carry = 1;
            else
                res.at(ci - 1) += 1;
        }
    }
    
    if(carry == 1)
        res = "1" + res;
        
    return res;
}

void check(string str)
{
    for(int i = 0; i < str.length(); ++i)
        digit[str[i] - '0'] = true;
        
    finish = true;
    for(int i = 0; i < 10; ++i)
        finish = finish & digit[i];
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("AF.txt");
    
  int T;
  while(fin >> T)
  {
    for(int t = 1; t <= T; ++t)
    {
        string N;
        fin >> N;
        
        finish = false;
        for(int i = 0; i < 10; ++i)
          digit[i] = false;
        
        string num = "0";
        if(N == "0")
        {
            fout << "Case #" << t << ": " << "INSOMNIA" << endl;
        }
        else
        {
            while(!finish)
            {
                num = Add(num, N);
                check(num);
            }

            fout << "Case #" << t << ": " << num << endl;
        }
    }
  }
    
  return 0;    
}
