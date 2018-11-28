#include <string>
#include <fstream>
#include <iostream>
using namespace std;

long long is_prime(long long n)
{
    if(n % 2 == 0)
        return 2;
        
    for(long long i = 3; i * i <= n; i += 2)
        if(n % i == 0)
            return i;
            
    return 0;
}

string Init(string str, int n)
{
    str[0] = '1';
    for(int i = 1; i < n - 1; ++i)
        str[i] = '0';
    str[n - 1] = '1';
    
    return str;
}

string Next(string str, int n)
{
    ++str[n - 2];
    for(int i = n - 2; i > 1; --i)
        if(str[i] == '2')
        {
            str[i] = '0';
            if(i != 1)
                ++str[i - 1];
        }
        
    return str;
}

long long convert(string num, int n, int base)
{
    long long res = 0;
    for(int i = 0; i < n; ++i)
        res = res * base + num[i] - '0';
    
    return res;
}

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C.txt");
    
    int T;
    fin >> T;
    
    for(int t = 1; t <= T; ++t)
    {
        fout << "Case #" << t << ": " << endl;
        
        int N, J;
        fin >> N >> J;
        string num = "";
        
        for(int i = 0; i < N; ++i)
            num += "0";
        
        num = Init(num, N);
        
        while(J > 0)
        {
            num = Next(num, N);
            
            int div[9];
            bool jam = true;
            for(int base = 2; base <= 10; ++base)
            {
                div[base - 2] = is_prime(convert(num, N, base));
                
                if(div[base - 2] == 0)
                {
                    jam = false;
                    break;
                }
            }
            
            if(jam)
            {
                fout << num;
                for(int i = 0; i < 9 ; ++i)
                    fout << " " << div[i];
                fout << endl;
                
                --J;
            }
        }
    }
    
    return 0;
}
